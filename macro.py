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
    # �� �Ʒ��Ŵ� ����������
    pyautogui.moveTo(384,362)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    ## �˸� â
    
    pyautogui.moveTo(739,176)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    # �� �Ʒ��Ŵ� �ڷᱸ��
    pyautogui.moveTo(385,387)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    ## �˸� â
    
    pyautogui.moveTo(739,176)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    # �� �Ʒ��� �������ڰ��н���
    pyautogui.moveTo(385,409)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    ## �˸� â
    
    pyautogui.moveTo(739,176)
    time.sleep(0.3)
    pyautogui.click()
    pyautogui.click()
    
    
    # �а������� ��ȸ
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
    







#���� Ŭ�� �ڵ�(f12, esc ������ �ڵ� Ż��)











