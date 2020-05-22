#! /usr/bin/python
# -*- coding: utf-8 -*-
"""本程序用于对指定文件夹文件进行归档，各类文件放入不同的问及那夹"""
import os


def process_files(old_path, new_path):

    folder_names_list = []
    for folderName, subfolders, filenames in os.walk(old_path):
        for filename in filenames:
            # 跳过process_files.py
            if filename == 'process_files.py':
                continue
            try:
                suffix = filename.rsplit('.')[-1]
                if suffix not in folder_names_list:
                    folder_names_list.append(suffix)
                    new_folder_name = f'{suffix}文件夹'
                    # 新建文件夹
                    os.makedirs(os.path.join(new_path, new_folder_name))
                    # 将文件存入该文件夹
                    os.rename(os.path.join(folderName, filename),
                                os.path.join(new_path, new_folder_name, filename))
                else:
                    # 将文件存入该文件夹
                    new_folder_name = f'{suffix}文件夹'
                    os.rename(os.path.join(folderName, filename),
                              os.path.join(new_path, new_folder_name, filename))
            except FileExistsError:
                continue


if __name__ == "__main__":
    old_path = r"H:\待处理文件夹"
    new_path = r"H:\经过整理的文件夹"
    process_files(old_path, new_path)
