import os, time, winsound, random

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

import tkinter as tk
from tkinter import messagebox

def show_popup(title="епт", message="блятб"):
    root = tk.Tk()
    root.withdraw()  # Прячем основное окно
    messagebox.showinfo(title, message)
    root.destroy()


def set_volume_to_max(): # Функция для установки громкости
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(1.0, None)


def RandTimeSound():
    while True:
        sound_list = ['wind_alert.wav', 'hub.wav']
        set_volume_to_max()
        time.sleep(random.randint(180, 3200)) # таймер 3 мин - 60 мин
        show_popup("Брооо!", "Опять ты звук не выключил :)")
        set_volume_to_max()
        winsound.PlaySound(f'C:/Users/{os.getlogin()}/AppData/Roaming/chache/{random.choice(sound_list)}', winsound.SND_FILENAME)


if __name__ == '__main__':
    RandTimeSound()