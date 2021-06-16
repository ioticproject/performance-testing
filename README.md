#### Build integration_tests image

    docker build -t performance-testing:latest .

### Run tests
    docker-compose up && docker-compose down

    docker run --rm --env-file=.env --network=backend performance-testing pytest


Teia@LAPTOP-G2CPH591 MINGW64 ~/Desktop/Licenta/performance-testing (master)
$ docker-compose up && docker-compose down
WARNING: Some networks were defined but are not used by any service: backend
Docker Compose is now in the Docker CLI, try `docker compose up`

Creating network "performance-testing_default" with the default driver
Creating performance-testing_performance_testing_1 ... done
Attaching to performance-testing_performance_testing_1
performance_testing_1  | 
performance_testing_1  | ---------------------------- live log sessionstart -----------------------------
performance_testing_1  | 2021-06-16 15:47:53 [    INFO] Added user for testing. (conftest.py:36)
performance_testing_1  | 2021-06-16 15:47:53 [    INFO] Got the user access token: jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjM4OTQ0NzMsImlhdCI6MTYyMzg1ODQ3MywibmJmIjoxNjIzODU4NDczLCJpZGVudGl0eSI6ImRjZGMzNGUxY2YzZjQzMzQ4NDViMmJjM2IyMmI5Y2EzIn0.UDH6LiaR9uza3N1jcsK_HllpPsu1v3xSnKBT_oeauzk (utils.py:50)
performance_testing_1  | 2021-06-16 15:47:53 [    INFO] Got the ADMIN access token: jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjM4OTQ0NzMsImlhdCI6MTYyMzg1ODQ3MywibmJmIjoxNjIzODU4NDczLCJpZGVudGl0eSI6IjI2OTNiMWVlYTVkMjQxZjBiYWE1ZmIzMjMyYmRiNTUxIn0.oZldH2pkq8cbnYdgfAQENiEKunr9WWimY7d-A2irxro (utils.py:64)
performance_testing_1  | 2021-06-16 15:47:53 [    INFO] Device ApiKey: 1d4111fbe6974821a780b8ad6fe584b1 (conftest.py:56)
performance_testing_1  | 2021-06-16 15:47:53 [    INFO] Added device for testing. (conftest.py:57)
performance_testing_1  | 2021-06-16 15:47:54 [    INFO] Added sensor for testing. (conftest.py:77)
performance_testing_1  | ============================= test session starts ==============================
performance_testing_1  | platform linux -- Python 3.8.10, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
performance_testing_1  | rootdir: /root/test, inifile: pytest.ini
performance_testing_1  | plugins: html-2.1.1, metadata-1.10.0
performance_testing_1  | collected 17 items
performance_testing_1  |
performance_testing_1  | test/test_data.py::test_get_data 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:47:55 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:47:57 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:47:59 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:01 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:03 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:05 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:07 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:09 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:12 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] Drawing plot get_data (utils.py:201)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] rq per s [23.32, 23.52, 24.23, 24.58, 24.04, 25.24, 23.45, 22.08, 23.91] (utils.py:205)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] time per rq [214.399, 212.599, 206.392, 203.438, 208.02, 198.067, 213.218, 226.405, 209.158] (utils.py:206)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] time per rq c [42.88, 42.52, 41.278, 40.688, 41.604, 39.613, 42.644, 45.281, 41.832] (utils.py:207)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] transfer rate [1095.77, 1105.05, 1138.28, 1154.81, 1129.37, 1186.12, 1101.84, 1037.66, 1123.23] (utils.py:208)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] Avg connection time: 2.0[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] Avg processing time: 189.22222222222223[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] Avg waiting time: 178.11111111111111[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_data.py::test_get_sensor_data 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:48:14 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:16 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:17 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:19 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:20 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:22 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:23 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:25 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:26 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] Drawing plot get_sensor_data (utils.py:201)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] rq per s [32.47, 36.03, 30.67, 34.72, 31.66, 36.54, 30.92, 35.51, 26.34] (utils.py:205)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] time per rq [154.001, 138.759, 163.037, 144.025, 157.913, 136.841, 161.684, 140.811, 189.842] (utils.py:206)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] time per rq c [30.8, 27.752, 32.607, 28.805, 31.583, 27.368, 32.337, 28.162, 37.968] (utils.py:207)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] transfer rate [5.99, 6.65, 5.66, 6.41, 5.84, 6.74, 5.71, 6.55, 4.86] (utils.py:208)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] Avg connection time: 3.111111111111111[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] Avg processing time: 135.66666666666666[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] Avg waiting time: 135.0[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:48:28 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_data.py::test_add_data 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:48:30 [    INFO] Drawing plot add_data (utils.py:201)
performance_testing_1  | 2021-06-16 15:48:30 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:48:30 [    INFO] rq per s [282.45, 258.68, 328.46, 318.81, 230.56, 245.74, 266.44, 269.76, 398.6] (utils.py:205)
performance_testing_1  | 2021-06-16 15:48:30 [    INFO] time per rq [17.702, 19.329, 15.222, 15.684, 21.686, 20.347, 18.766, 18.535, 12.544] (utils.py:206)
performance_testing_1  | 2021-06-16 15:48:30 [    INFO] time per rq c [3.54, 3.866, 3.044, 3.137, 4.337, 4.069, 3.753, 3.707, 2.509] (utils.py:207)
performance_testing_1  | 2021-06-16 15:48:30 [    INFO] transfer rate [94.89, 86.9, 110.34, 107.1, 77.45, 82.55, 89.51, 90.62, 133.9] (utils.py:208)
performance_testing_1  | 2021-06-16 15:48:31 [    INFO] Avg connection time: 3.7777777777777777[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:48:31 [    INFO] Avg processing time: 12.777777777777779[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:48:31 [    INFO] Avg waiting time: 11.11111111111111[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:48:31 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_device.py::test_get_devices 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:48:31 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:32 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:33 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:34 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:35 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:36 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:37 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:38 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:39 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] Drawing plot get_devices (utils.py:201)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] rq per s [48.74, 53.08, 48.67, 48.09, 50.69, 50.22, 49.33, 51.67, 47.47] (utils.py:205)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] time per rq [102.593, 94.199, 102.724, 103.965, 98.637, 99.562, 101.357, 96.773, 105.34] (utils.py:206)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] time per rq c [20.519, 18.84, 20.545, 20.793, 19.727, 19.912, 20.271, 19.355, 21.068] (utils.py:207)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] transfer rate [140.59, 153.12, 140.41, 138.74, 146.23, 144.87, 142.31, 149.05, 136.93] (utils.py:208)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] Avg connection time: 3.4444444444444446[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] Avg processing time: 87.44444444444444[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] Avg waiting time: 85.77777777777777[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:48:40 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_device.py::test_get_device
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:48:41 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:43 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:45 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:47 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:49 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:51 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:53 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:55 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:57 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] Drawing plot get_device (utils.py:201)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] rq per s [24.77, 24.73, 25.02, 24.36, 24.31, 24.9, 24.67, 24.81, 25.43] (utils.py:205)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] time per rq [201.852, 202.218, 199.861, 205.284, 205.697, 200.818, 202.712, 201.562, 196.599] (utils.py:206)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] time per rq c [40.37, 40.444, 39.972, 41.057, 41.139, 40.164, 40.542, 40.312, 39.32] (utils.py:207)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] transfer rate [22.4, 22.36, 22.62, 22.03, 21.98, 22.52, 22.3, 22.43, 23.0] (utils.py:208)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] Avg connection time: 3.7777777777777777[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] Avg processing time: 180.0[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] Avg waiting time: 178.88888888888889[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_device.py::test_get_user_devices 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:48:59 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:01 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:03 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:04 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:06 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:07 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:09 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:10 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:12 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:13 [    INFO] Drawing plot get_user_devices (utils.py:201)
performance_testing_1  | 2021-06-16 15:49:13 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:49:13 [    INFO] rq per s [32.92, 30.63, 36.83, 30.28, 36.32, 27.09, 37.79, 29.88, 37.21] (utils.py:205)
performance_testing_1  | 2021-06-16 15:49:13 [    INFO] time per rq [151.877, 163.254, 135.754, 165.122, 137.683, 184.592, 132.322, 167.355, 134.386] (utils.py:206)
performance_testing_1  | 2021-06-16 15:49:13 [    INFO] time per rq c [30.375, 32.651, 27.151, 33.024, 27.537, 36.918, 26.464, 33.471, 26.877] (utils.py:207)
performance_testing_1  | 2021-06-16 15:49:13 [    INFO] transfer rate [14.4, 13.4, 16.11, 13.25, 15.89, 11.85, 16.53, 13.07, 16.28] (utils.py:208)
performance_testing_1  | 2021-06-16 15:49:14 [    INFO] Avg connection time: 3.888888888888889[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:49:14 [    INFO] Avg processing time: 132.77777777777777[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:49:14 [    INFO] Avg waiting time: 131.66666666666666[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:49:14 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_device.py::test_add_device 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:49:18 [    INFO] Drawing plot add_device (utils.py:201)
performance_testing_1  | 2021-06-16 15:49:18 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:49:18 [    INFO] rq per s [72.92, 97.34, 102.31, 103.61, 99.77, 100.65, 104.59, 98.45, 100.93] (utils.py:205)
performance_testing_1  | 2021-06-16 15:49:18 [    INFO] time per rq [68.564, 51.364, 48.87, 48.256, 50.114, 49.678, 47.807, 50.785, 49.541] (utils.py:206)
performance_testing_1  | 2021-06-16 15:49:18 [    INFO] time per rq c [13.713, 10.273, 9.774, 9.651, 10.023, 9.936, 9.561, 10.157, 9.908] (utils.py:207)
performance_testing_1  | 2021-06-16 15:49:18 [    INFO] transfer rate [19.51, 26.05, 27.38, 27.72, 26.7, 26.93, 27.99, 26.34, 27.01] (utils.py:208)
performance_testing_1  | 2021-06-16 15:49:19 [    INFO] Avg connection time: 2.4444444444444446[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:49:19 [    INFO] Avg processing time: 42.77777777777778[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:49:19 [    INFO] Avg waiting time: 42.111111111111114[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:49:19 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_sensor.py::test_get_sensors 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:49:19 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:20 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:21 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:22 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:24 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:25 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:26 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:27 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:28 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:29 [    INFO] Drawing plot get_sensors (utils.py:201)
performance_testing_1  | 2021-06-16 15:49:29 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:49:29 [    INFO] rq per s [45.94, 45.23, 44.3, 39.05, 39.27, 43.7, 46.36, 46.62, 45.93] (utils.py:205)
performance_testing_1  | 2021-06-16 15:49:29 [    INFO] time per rq [108.849, 110.546, 112.873, 128.044, 127.316, 114.41, 107.855, 107.241, 108.873] (utils.py:206)
performance_testing_1  | 2021-06-16 15:49:29 [    INFO] time per rq c [21.77, 22.109, 22.575, 25.609, 25.463, 22.882, 21.571, 21.448, 21.774] (utils.py:207)
performance_testing_1  | 2021-06-16 15:49:29 [    INFO] transfer rate [272.65, 268.47, 262.93, 231.78, 233.1, 259.4, 275.16, 276.74, 272.59] (utils.py:208)
performance_testing_1  | 2021-06-16 15:49:30 [    INFO] Avg connection time: 3.5555555555555554[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:49:30 [    INFO] Avg processing time: 99.33333333333333[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:49:30 [    INFO] Avg waiting time: 94.88888888888889[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:49:30 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_sensor.py::test_get_sensor 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:49:30 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:31 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:33 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:35 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:36 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:38 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:39 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:41 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:42 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:44 [    INFO] Drawing plot get_sensor (utils.py:201)
performance_testing_1  | 2021-06-16 15:49:44 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:49:44 [    INFO] rq per s [32.49, 36.49, 26.53, 31.72, 37.08, 30.41, 36.61, 30.19, 32.31] (utils.py:205)
performance_testing_1  | 2021-06-16 15:49:44 [    INFO] time per rq [153.901, 137.024, 188.501, 157.639, 134.831, 164.41, 136.575, 165.644, 154.746] (utils.py:206)
performance_testing_1  | 2021-06-16 15:49:44 [    INFO] time per rq c [30.78, 27.405, 37.7, 31.528, 26.966, 32.882, 27.315, 33.129, 30.949] (utils.py:207)
performance_testing_1  | 2021-06-16 15:49:44 [    INFO] transfer rate [12.82, 14.4, 10.46, 12.51, 14.63, 12.0, 14.44, 11.91, 12.75] (utils.py:208)
performance_testing_1  | 2021-06-16 15:49:45 [    INFO] Avg connection time: 3.3333333333333335[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:49:45 [    INFO] Avg processing time: 135.33333333333334[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:49:45 [    INFO] Avg waiting time: 134.44444444444446[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:49:45 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_sensor.py::test_get_user_sensors 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:49:45 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:46 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:48 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:49 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:51 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:52 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:54 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:55 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:57 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:49:58 [    INFO] Drawing plot get_user_sensors (utils.py:201)
performance_testing_1  | 2021-06-16 15:49:58 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:49:58 [    INFO] rq per s [32.68, 33.77, 33.4, 35.26, 30.47, 36.55, 31.23, 36.59, 30.04] (utils.py:205)
performance_testing_1  | 2021-06-16 15:49:58 [    INFO] time per rq [153.011, 148.058, 149.714, 141.794, 164.102, 136.813, 160.089, 136.651, 166.442] (utils.py:206)
performance_testing_1  | 2021-06-16 15:49:58 [    INFO] time per rq c [30.602, 29.612, 29.943, 28.359, 32.82, 27.363, 32.018, 27.33, 33.288] (utils.py:207)
performance_testing_1  | 2021-06-16 15:49:58 [    INFO] transfer rate [14.87, 15.37, 15.2, 16.05, 13.87, 16.63, 14.21, 16.65, 13.67] (utils.py:208)
performance_testing_1  | 2021-06-16 15:49:59 [    INFO] Avg connection time: 3.5555555555555554[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:49:59 [    INFO] Avg processing time: 133.66666666666666[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:49:59 [    INFO] Avg waiting time: 132.66666666666666[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:49:59 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_sensor.py::test_get_device_sensors 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:49:59 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:00 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:02 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:04 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:05 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:07 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:08 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:10 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:11 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] Drawing plot get_device_sensors (utils.py:201)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] rq per s [31.72, 35.53, 30.5, 30.61, 36.18, 30.55, 37.83, 29.83, 35.63] (utils.py:205)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] time per rq [157.634, 140.738, 163.933, 163.331, 138.179, 163.644, 132.174, 167.603, 140.32] (utils.py:206)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] time per rq c [31.527, 28.148, 32.787, 32.666, 27.636, 32.729, 26.435, 33.521, 28.064] (utils.py:207)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] transfer rate [14.43, 16.17, 13.88, 13.93, 16.47, 13.9, 17.22, 13.58, 16.22] (utils.py:208)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] Avg connection time: 3.0[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] Avg processing time: 134.88888888888889[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] Avg waiting time: 134.44444444444446[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:50:13 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_sensor.py::test_add_sensor 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] Drawing plot add_sensor (utils.py:201)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] rq per s [186.1, 286.79, 234.32, 244.91, 184.81, 293.0, 262.41, 282.26, 326.97] (utils.py:205)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] time per rq [26.868, 17.435, 21.339, 20.416, 27.055, 17.065, 19.054, 17.714, 15.292] (utils.py:206)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] time per rq c [5.374, 3.487, 4.268, 4.083, 5.411, 3.413, 3.811, 3.543, 3.058] (utils.py:207)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] transfer rate [62.52, 96.34, 78.72, 82.27, 62.08, 98.43, 88.15, 94.82, 109.84] (utils.py:208)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] Avg connection time: 4.666666666666667[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] Avg processing time: 14.666666666666666[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] Avg waiting time: 12.555555555555555[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_user.py::test_health 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:50:15 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:16 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:16 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:16 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:16 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:16 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:16 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Drawing plot health (utils.py:201)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] rq per s [296.49, 304.96, 403.22, 394.48, 349.83, 258.36, 386.5, 305.93, 404.04] (utils.py:205)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] time per rq [16.864, 16.396, 12.4, 12.675, 14.293, 19.353, 12.936, 16.344, 12.375] (utils.py:206)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] time per rq c [3.373, 3.279, 2.48, 2.535, 2.859, 3.871, 2.587, 3.269, 2.475] (utils.py:207)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] transfer rate [57.62, 59.26, 78.36, 76.66, 67.98, 50.21, 75.11, 59.45, 78.52] (utils.py:208)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Avg connection time: 5.111111111111111[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Avg processing time: 9.0[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Avg waiting time: 7.555555555555555[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:50:17 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_user.py::test_login 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] Drawing plot user_login (utils.py:201)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] rq per s [98.37, 108.59, 107.04, 109.41, 94.05, 105.43, 87.42, 96.04, 100.83] (utils.py:205)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] time per rq [50.828, 46.045, 46.711, 45.698, 53.165, 47.427, 57.196, 52.063, 49.588] (utils.py:206)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] time per rq c [10.166, 9.209, 9.342, 9.14, 10.633, 9.485, 11.439, 10.413, 9.918] (utils.py:207)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] transfer rate [21.9, 24.18, 23.83, 24.36, 20.94, 23.47, 19.46, 21.38, 22.45] (utils.py:208)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] Avg connection time: 2.888888888888889[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] Avg processing time: 41.77777777777778[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] Avg waiting time: 41.22222222222222[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_user.py::test_get_users 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:50:22 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:24 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:25 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:26 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:27 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:28 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:29 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:30 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:31 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] Drawing plot get_users (utils.py:201)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] rq per s [43.5, 41.85, 51.71, 39.94, 49.08, 43.99, 50.1, 42.53, 37.2] (utils.py:205)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] time per rq [114.935, 119.464, 96.698, 125.199, 101.876, 113.654, 99.81, 117.572, 134.407] (utils.py:206)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] time per rq c [22.987, 23.893, 19.34, 25.04, 20.375, 22.731, 19.962, 23.514, 26.881] (utils.py:207)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] transfer rate [261.91, 251.98, 311.3, 240.44, 295.48, 264.86, 301.6, 256.03, 223.96] (utils.py:208)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] Avg connection time: 3.0[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] Avg processing time: 97.11111111111111[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] Avg waiting time: 94.44444444444444[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:50:33 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED
performance_testing_1  | test/test_user.py::test_get_user 
performance_testing_1  | -------------------------------- live log call ---------------------------------
performance_testing_1  | 2021-06-16 15:50:34 [    INFO] Send 5 requests, concurrency 5 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:35 [    INFO] Send 10 requests, concurrency 10 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:38 [    INFO] Send 25 requests, concurrency 15 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:40 [    INFO] Send 50 requests, concurrency 20 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:42 [    INFO] Send 100 requests, concurrency 25 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:44 [    INFO] Send 250 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:46 [    INFO] Send 500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:48 [    INFO] Send 1000 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:51 [    INFO] Send 1500 requests, concurrency 50 (utils.py:324)
performance_testing_1  | 2021-06-16 15:50:53 [    INFO] Drawing plot get_user (utils.py:201)
performance_testing_1  | 2021-06-16 15:50:53 [    INFO] reqs [5, 10, 25, 50, 100, 250, 500, 1000, 1500] (utils.py:204)
performance_testing_1  | 2021-06-16 15:50:53 [    INFO] rq per s [27.3, 22.26, 25.64, 19.88, 24.94, 24.25, 22.1, 20.62, 21.58] (utils.py:205)
performance_testing_1  | 2021-06-16 15:50:53 [    INFO] time per rq [183.127, 224.615, 195.009, 251.467, 200.501, 206.162, 226.214, 242.528, 231.668] (utils.py:206)
performance_testing_1  | 2021-06-16 15:50:53 [    INFO] time per rq c [36.625, 44.923, 39.002, 50.293, 40.1, 41.232, 45.243, 48.506, 46.334] (utils.py:207)
performance_testing_1  | 2021-06-16 15:50:53 [    INFO] transfer rate [22.45, 18.3, 21.08, 16.35, 20.51, 19.94, 18.17, 16.95, 17.75] (utils.py:208)
performance_testing_1  | 2021-06-16 15:50:54 [    INFO] Avg connection time: 3.3333333333333335[ms] (utils.py:235)
performance_testing_1  | 2021-06-16 15:50:54 [    INFO] Avg processing time: 190.55555555555554[ms] (utils.py:236)
performance_testing_1  | 2021-06-16 15:50:54 [    INFO] Avg waiting time: 189.22222222222223[ms] (utils.py:237)
performance_testing_1  | 2021-06-16 15:50:54 [    INFO] Failed requests: 0 (utils.py:238)
performance_testing_1  | PASSED