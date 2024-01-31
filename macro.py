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
    # 그 아래거는 리눅스관리
    pyautogui.moveTo(384,362)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    ## 알림 창
    
    pyautogui.moveTo(739,176)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    # 그 아래거는 자료구조
    pyautogui.moveTo(385,387)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    ## 알림 창
    
    pyautogui.moveTo(739,176)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    # 그 아래는 전기전자공학실험
    pyautogui.moveTo(385,409)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    ## 알림 창
    
    pyautogui.moveTo(739,176)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    # 학과별강좌 조회
    pyautogui.moveTo(276,680)
    pyautogui.click()
    pyautogui.click()
    
    if keyboard.is_pressed('esc'):
        break




#     time.sleep(0.5)
#     pyautogui.click()


# while 1:
#     if keyboard.is_pressed('enter'):
#         position = pyautogui.position()
#         print(position)
#         time.sleep(0.2)
#     elif keyboard.is_pressed('esc'):
#         break
    







#무한 클릭 코드(f12, esc 누르면 자동 탈출)











