import os
import re


def union_files(directory: str):
    union_dict = dict()
    for file in os.listdir(directory):
        if re.match(r'\w+.txt', file) and file != 'res.txt':
            path = f"{directory}/{file}"
            with open(path, 'r', encoding='utf-8') as inner_file:
                content_file = [i for i in inner_file.readlines()]
                union_dict.update({file: (len(content_file), content_file)})
    sorted_keys = sorted(union_dict, key=lambda x: union_dict[x][0])
    path_for_write = f"{directory}/res.txt"
    with open(path_for_write, 'w', encoding='utf-8') as file:
        for i in sorted_keys:
            file.write(f"{i}\n{union_dict[i][0]}\n")
            for j in union_dict[i][1]:
                file.write(j)
            file.write('\n')

union_files('Folder_task3')
# Результат запуска программы в файле res.txt репозитория Folder_task3