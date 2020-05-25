from process_files import process_files
from delete_folders import delete_folders


if __name__ == "__main__":
    old_path = r"E:\待处理文件"
    new_path = r"E:\处理好的文件"
    process_files(old_path, new_path)
    delete_folders(new_path)
