with open(r'Folder_task3/1.txt', 'r', encoding='utf-8') as file1:
    with open(r'Folder_task3/2.txt', 'r', encoding='utf-8') as file2:
        with open(r'Folder_task3/3.txt', 'r', encoding='utf-8') as file3:
            data = {
                    '1.txt': [i for i in file1.readlines()],
                    '2.txt': [i for i in file2.readlines()],
                    '3.txt': [i for i in file3.readlines()],
                    }
            sorted_keys = sorted(data, key=lambda x: len(data[x]))

with open(r'Folder_task3/res.txt', 'w', encoding='utf-8') as file:
    for i in sorted_keys:
        file.write(f"{i}\n{len(data[i])}\n")
        for j in data[i]:
            file.write(j)
        file.write('\n')

# Результат запуска программы в файле res.txt репозитория Folder_task3