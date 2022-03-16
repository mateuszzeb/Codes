import time, ctypes

for i in range(10):
    time.sleep(1)
    exec('ctypes.windll.WINMM.mciSendStringW(u"open L: type CDAudio alias L_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set L_drive door open", None, 0, None')
    time.sleep(1)
    exec('ctypes.windll.WINMM.mciSendStringW(u"open L: type CDAudio alias L_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set L_drive door closed", None, 0, None)')
