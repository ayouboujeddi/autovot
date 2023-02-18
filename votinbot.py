import pyautogui
import time

position = [(1391, 983),(1247, 361),(1299, 491),(1265, 638),(1336, 790),(1114, 918),(953, 1013)]

time.sleep(5)


email = 2200

while True:
    # time.sleep(1)
    # print(pyautogui.position())
    time.sleep(1)
    pyautogui.click(position[0][0], position[0][1])
    time.sleep(1)
    pyautogui.click(position[5][0],position[5][1])
    time.sleep(0.5)
    pyautogui.click(position[1][0], position[1][1])
    pyautogui.write('omari')
    time.sleep(0.5)
    pyautogui.click(position[2][0], position[2][1])
    pyautogui.write('adam')
    time.sleep(0.5)
    pyautogui.click(position[3][0], position[3][1])
    pyautogui.write("0676342213")
    time.sleep(0.5)
    pyautogui.click(position[4][0], position[4][1])
    text = "omariadam"+str(email)+"@gmail.com"
    email+=1
    print(email)
    pyautogui.write(text)
    time.sleep(0.5)
    pyautogui.click(position[6][0], position[6][1])
    



