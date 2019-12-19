import pyautogui as gui
import webbrowser
import time
from matplotlib import pyplot as plt
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = "tesseract/4.1.0/bin/tesseract"
translator = Translator()

def click(path, after=0):
    time.sleep(after)
    try:
        pos=gui.locateOnScreen(path, grayscale=True, confidence=0.75)
        mid=gui.center(pos)
        gui.moveTo(mid)
        gui.mouseDown()
        gui.mouseUp()
        return True
    except:
        print(path + "button not found")
        return False
        
def getSentence():
    try:
        pos=gui.locateOnScreen('screenshots/sound.png', grayscale=True, confidence=0.5)
        region = (pos[0] + pos[2], pos[1]-10, 800, pos[3] + 20)
    except:
        pos=gui.locateOnScreen('screenshots/write.png', grayscale=True, confidence=0.5)
        region = (pos[0], pos[1] + pos[3] * 1.69, 800, pos[3] + 20)

    
    try:
        
        screenshot = gui.screenshot(region=region)
#         plt.imshow(screenshot)
#         plt.show()
        text = pytesseract.image_to_string(screenshot)
    except TypeError:
        print("no sentence")
    
    return text
        
def openLesson(name, after=0):
    time.sleep(after)
    gui.hotkey('command','f')
    time.sleep(.5)
    gui.typewrite(name)
    time.sleep(.5)
    gui.press('esc')
    click("screenshots/lessons/" + name + ".png", .5)
    click('screenshots/start.png', .5)
    click('screenshots/use-keyboard.png', 1)


def login(user, passwd):
    webbrowser.open('http://duolingo.com/', new=2)
    click('screenshots/sign-in.png', 3)
    click('screenshots/user.png', 2)
    gui.typewrite(user)
    click('screenshots/pass.png')
    gui.typewrite(passwd)
    click('screenshots/submit.png')
    
    
def translate(sentence):
    curLan = translator.detect(sentence).lang
    if(curLan == 'en'):
        translated = translator.translate(sentence, dest='de').text
    elif(curLan == 'de'):
        translated = translator.translate(sentence, dest='en').text
    return translated
    
def inputSentence(sentence):
    gui.typewrite(sentence + "\n", interval= 0.02)
    gui.hotkey('enter')
    
def doLesson():
    while True:
        time.sleep(1)
        sentence = getSentence()
        if sentence == None:
            continue
        time.sleep(.5)
        t = translate(sentence)
        inputSentence(t)

# login("21horspbosk@washk12.org","bobbob11")
webbrowser.open('http://duolingo.com/', new=2)
openLesson('adjectives', 1.3)
doLesson()






