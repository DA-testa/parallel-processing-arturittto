#Artūrs Čubukovs 16.grupa 221RDB127
from threading import Thread, Lock

def process_job(thread_idx, job_idx, job_time, start_time, results, lock):
    time.sleep(job_time)
    with lock:
        results[job_idx] = (thread_idx, start_time)

def assign_jobs(n, m, times):
    results = [None] * m
    start_times = [0] * n
    lock = Lock()
    threads = []
    for i in range(m):
        thread_idx = start_times.index(min(start_times))
        thread = Thread(target=process_job, args=(thread_idx, i, times[i], start_times[thread_idx], results, lock))
        threads.append(thread)
        thread.start()
        start_times[thread_idx] += times[i]
    for thread in threads:
        thread.join()
    for result in results:
        print(result[0], result[1])
