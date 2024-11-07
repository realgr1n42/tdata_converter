import os
import shutil

def main():
    current_dir = os.path.join(os.getcwd(), 'res_sessions')
    json_files = [f for f in os.listdir(current_dir) if f.endswith('.json')]
    session_files = [f for f in os.listdir(current_dir) if f.endswith('.session')]
    json_basenames = set(os.path.splitext(f)[0] for f in json_files)
    session_basenames = set(os.path.splitext(f)[0] for f in session_files)
    common_basenames = json_basenames.intersection(session_basenames)
    if not common_basenames:
        print("Не найдено пар файлов с одинаковыми именами и расширениями .json и .session.")
    else:
        for basename in common_basenames:
            folder_path = os.path.join(current_dir, basename)
            os.makedirs(folder_path, exist_ok=True)
            json_file = basename + '.json'
            session_file = basename + '.session'
            shutil.move(os.path.join(current_dir, json_file), folder_path)
            shutil.move(os.path.join(current_dir, session_file), folder_path)
            shutil.make_archive(basename, 'zip', folder_path)
            shutil.rmtree(folder_path)
            print(f"Файлы '{json_file}' и '{session_file}' перемещены в архив '{basename}.zip', исходная папка удалена.")
    print("Работа завершена.")

if __name__ == "__main__":
    main()
