import pyautogui as gui
import time



screen = gui.size()

screenHeight = 93.49 * (screen.height/100)

screenHeight = int(screenHeight)
screenTaskBar = 6.51 * (screen.height/100)
screenTaskBar = int(screenTaskBar)
time.sleep(1)

def AnyDesk():
    deskApp = gui.locateCenterOnScreen('img/anydesk_theme_dark.png', confidence=0.9,region=(0,screenHeight,screen.width,screenTaskBar),)
    time.sleep(3)
    gui.click(deskApp.x,  deskApp.y)
    time.sleep(1)
    gui.press('f5')
    time.sleep(10)

def Browser():
    browser = gui.locateCenterOnScreen('img/chrome_theme_dark.png', confidence=0.9,region=(0,screenHeight,screen.width,screenTaskBar))
    time.sleep(3)
    gui.click(browser.x,  browser.y)
    time.sleep(10)

while True:
    try:
        AnyDesk()
        Browser()
    except gui.ImageNotFoundException:
        print(gui.ImageNotFoundException)