def sorting_names():
    with open("list_worker.txt", "r+") as file:
        list_of_str = file.readlines()
        list_of_list =[]
        for line in list_of_str:
            temp = line.split("|")
            list_of_list.append(temp)
        list_of_list = sorted(list_of_list, key = lambda x: x[1])
        file.seek(0)
        for worker in list_of_list:
            file.write("|" .join(worker))
        print('sorted')



def sorting_id():
    with open("list_worker.txt", "r+") as file:
        list_of_str = file.readlines()
        list_of_list =[]
        for line in list_of_str:
            temp = line.split("|")
            list_of_list.append(temp)
        list_of_list = sorted(list_of_list, key = lambda x: x[0])
        file.seek(0)
        for worker in list_of_list:
            file.write("|" .join(worker))
        print('sorted')
