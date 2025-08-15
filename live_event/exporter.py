import os, json, time, asyncio
    from prometheus_client import start_http_server, Gauge, Enum
    from nats.aio.client import Client as NATS

    # Gauges = live needles
    V  = Gauge('bus_supply_voltage_volts', 'Main bus voltage (V)', ['bus_id'])
    SOC= Gauge('bus_battery_soc_percent', 'Battery state of charge (%)', ['bus_id'])
    TMP= Gauge('bus_imu_temp_celsius', 'IMU temp (C)', ['bus_id'])
    HB = Gauge('bus_last_heartbeat_unixtime', 'Heartbeat unixtime', ['bus_id'])
    MODE = Enum('bus_mode', 'Bus mode', states=['idle','safe','nominal','highrate'])

    BUS_ID  = os.getenv('BUS_ID','bus-1')
    SUBJECT = os.getenv('NATS_SUBJECT','telemetry.bus.housekeeping')
    NATS_URL= os.getenv('NATS_URL','nats://nats.svc.cluster.local:4222')

    start_http_server(8000)  # /metrics

    async def main():
      nc = NATS()
      await nc.connect(servers=[NATS_URL])

      async def handler(msg):
        try:
          d = json.loads(msg.data.decode('utf-8'))
          # Expect fields like: {"v":7.2,"soc":83.1,"temp":27.4,"mode":"nominal","ts":1712345678}
          V.labels(BUS_ID).set(float(d.get('v', 'nan')))
          SOC.labels(BUS_ID).set(float(d.get('soc', 'nan')))
          TMP.labels(BUS_ID).set(float(d.get('temp', 'nan')))
          HB.labels(BUS_ID).set(float(d.get('ts', time.time())))
          if 'mode' in d and d['mode'] in MODE._states:
            MODE.state(d['mode'])
        except Exception as e:
          # minimalist: ignore bad packets; consider logging
          pass

      await nc.subscribe(SUBJECT, cb=handler)
      while True:
        await asyncio.sleep(1)

    asyncio.run(main())
