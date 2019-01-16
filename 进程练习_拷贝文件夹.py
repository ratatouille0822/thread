import os
import multiprocessing


def copy_file(file_name, folder_name, new_folder_name, queue):
    # 完成文件的复制
    # print("把 [%s] 从 [%s] 复制到 [%s] ..." % (file_name, folder_name, new_folder_name))
    old_f = open(folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()
    # 新文件的写
    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()
    # 写入队列
    queue.put(file_name)


def main():

    # 1. 获取新的文件夹的名字
    folder_name = input("请输入要拷贝的文件夹的名字： ")
    new_folder_name = folder_name + "复件"

    # 1.1 创建队列
    queue = multiprocessing.Manager().Queue(10)

    # 2. 建立一个新的文件夹
    try:
        os.mkdir(new_folder_name)
    except FileExistsError:
        print("已经有了这个文件夹")

    # 3. 获取所有要拷贝的文件的名字
    name_list = os.listdir(folder_name)
    print(name_list)

    # 4. 建立进程，完成拷贝
    pool = multiprocessing.Pool(10)
    for file_name in name_list:
        pool.apply_async(copy_file, args=(file_name, folder_name, new_folder_name, queue))

    pool.close()

    num = 0
    file_num = len(name_list)

    while True:
        file_name_copied = queue.get()
        num += 1
        print("\r %.2f%% 已完成" % (num/file_num * 100), end="")
        if num >= file_num:
            print("拷贝完成")
            break
    # pool.join()

# 复制文件到新的文件夹


if __name__ == "__main__":
    main()
