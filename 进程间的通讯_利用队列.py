import multiprocessing


def download_from_web(q):
    data = [11, 22, 33]

    for temp in data:
        q.put(temp)


def data_process(q):

    data_to_process = list()
    if not q.empty():
        data_to_process.append(q.get())
        print(data_to_process)


def main():
    q = multiprocessing.Queue(100)

    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=data_process, args=(q, ))
    p1.start()
    p2.start()




if __name__ == "__main__":
    main()


