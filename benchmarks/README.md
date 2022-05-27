1. Make sure that all of the pods are running (with injected Environment Variables)
2. Run the following line for benchmarking this project
> locust -H http://127.0.0.1 -f try_p1.py -u 50 -r 2 PasteBin