import pyautogui
import keyboard
import time

#pyautogui.moveTo(960,540,3
#가로 세로, 몇초동안??

#position = pyautogui.position() #postion 함수를 이용해서 마우스의 위치를 변수에 담음.
#print(position)


# 전체주석: Ctrl+/
# C 언어: Ctrl+K => C , Ctrl+K => U


while 1:
    if keyboard.is_pressed('enter'):
        position = pyautogui.position()
        print(position)
        time.sleep(0.2)
    elif keyboard.is_pressed('esc'):
        break



#무한 클릭 코드(f12, esc 누르면 자동 탈출)


while 1:
    if keyboard.is_pressed('enter'):
        position = pyautogui.position()
        while 1:
            pyautogui.click(position)
            if keyboard.is_pressed('esc'):
                break
    elif keyboard.is_pressed('f12'):
        break

