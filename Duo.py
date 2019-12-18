import pyautogui as gui
import webbrowser
import time
from googletrans import Translator

def click(path, after=0):
    time.sleep(after)
    try:
        pos=gui.locateOnScreen(path, grayscale=True, confidence=0.75)
        mid=gui.center(pos)
        gui.moveTo(mid)
        gui.mouseDown()
        gui.mouseUp()
    except:
        print("button not found")
        
def openLesson(name, after=0):
    time.sleep(after)
    gui.hotkey('command','f')
    time.sleep(.5)
    gui.typewrite(name)
    time.sleep(1)
    gui.press('esc')
    click("screenshots/" + name + ".png", 2)
    click('screenshots/start.png', 2)


def login(user, passwd):
    webbrowser.open('http://duolingo.com/', new=2)
    click('screenshots/sign-in.png', 3)
    click('screenshots/user.png', 2)
    gui.typewrite(user)
    click('screenshots/pass.png')
    gui.typewrite(passwd)
    click('screenshots/submit.png')
    
    
def translate(sentance):
    curLan = translator.detect(sentance).lang
    if(curLan == 'en'):
        translated = translator.translate(sentance, dest='de').text
    elif(curLan == 'de'):
        translated = translator.translate(sentance, dest='en').text
    

login("21horspbosk@washk12.org","bobbob11")

openLesson('plurals', 3)

click('screenshots/use-keyboard.png', 2)






