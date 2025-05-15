import os, time, winsound, random

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


def set_volume_to_max(): # Функция для установки громкости
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(1.0, None)


def RandTimeSound():
    while True:
        sound_list = ['wind_alert.wav', 'hub.wav']
        time.sleep(random.randint(180, 3200)) # таймер 3 мин - 60 мин
        set_volume_to_max()
        winsound.PlaySound(f'{os.path.join(os.path.expanduser("~"), "chach\\media")}\\{random.choice(sound_list)}', winsound.SND_FILENAME)


if __name__ == '__main__':
    RandTimeSound()
