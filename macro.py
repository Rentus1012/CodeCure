import pyautogui
import keyboard
import time

#pyautogui.moveTo(960,540,3
#���� ����, ���ʵ���??

#position = pyautogui.position() #postion �Լ��� �̿��ؼ� ���콺�� ��ġ�� ������ ����.
#print(position)


# ��ü�ּ�: Ctrl+/
# C ���: Ctrl+K => C , Ctrl+K => U


while 1:
    if keyboard.is_pressed('enter'):
        position = pyautogui.position()
        print(position)
        time.sleep(0.2)
    elif keyboard.is_pressed('esc'):
        break



#���� Ŭ�� �ڵ�(f12, esc ������ �ڵ� Ż��)


while 1:
    if keyboard.is_pressed('enter'):
        position = pyautogui.position()
        while 1:
            pyautogui.click(position)
            if keyboard.is_pressed('esc'):
                break
    elif keyboard.is_pressed('f12'):
        break

