# uptime_kuma_poller
Small docker container to poll to a remote uptime kuma instance (for closed networks)

# Setup 

ON REMOTE UPTIME KUMA
----------------------
<img width="616" alt="esbfYPTKT3" src="https://github.com/Lehoooo/uptime_kuma_poller/assets/52742690/ce7c818b-df1d-45dd-b3b4-0479a90de577">

<img width="263" alt="qDfKIwTtk2" src="https://github.com/Lehoooo/uptime_kuma_poller/assets/52742690/3de384be-d6e3-4d59-84a1-26d1888b0ca6">

<img width="304" alt="WbRWpauCqY" src="https://github.com/Lehoooo/uptime_kuma_poller/assets/52742690/25572754-dd59-4c3a-8b67-e3c8839df868">

Put that URL into config.json


ON MONITORED SERVER
------------------

1. Clone this repo

2. Make sure the config.json is correct, then:

```docker compose up -d```

3. done have fun :)
