import os
import shutil

# Путь к основной папке
base_dir = './sessions_to_tdata'

# Проходим по всем директориям внутри base_dir
for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)
    # Проверяем, является ли элемент директорией
    if os.path.isdir(item_path):
        # Перемещаем все файлы из этой директории в base_dir
        for file_name in os.listdir(item_path):
            file_path = os.path.join(item_path, file_name)
            # Проверяем, является ли элемент файлом
            if os.path.isfile(file_path):
                shutil.move(file_path, base_dir)
        # Удаляем пустую директорию
        os.rmdir(item_path)

print("Файлы из поддиректорий перемещены в ./sessions_to_tdata")
