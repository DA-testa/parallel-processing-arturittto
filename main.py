#Artūrs Čubukovs 16.grupa 221RBS127

def parallel_processing(n, m, data):
    threads = [(i, 0) for i in range(n)]
    output = []

    for i in range(m):
        thread_id, finish_time = min(threads, key=lambda x: x[1])
        output.append((thread_id, finish_time))
        threads[thread_id] = (thread_id, finish_time + data[i])

    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_id, start_time in result:
        print(thread_id, start_time)


if __name__ == "__main__":
    main()
