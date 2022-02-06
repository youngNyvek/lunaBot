import pyautogui
import time

def moveMouseTo(imageFound):
    imgX, imgY = pyautogui.center(imageFound)
    pyautogui.moveTo(imgX, imgY, 2)
    pyautogui.click()

def huntAreStarted():
    victory = pyautogui.locateOnScreen('./targets/victory.png', confidence=0.9)
    defeat = pyautogui.locateOnScreen('./targets/defeat.png', confidence=0.9)
    if victory :
        print('Vitória!')
        findingOpenChest = pyautogui.locateOnScreen('./targets/openChest.png', confidence=0.9)
        if findingOpenChest :
            moveMouseTo(findingOpenChest)
            findingContinue = pyautogui.locateOnScreen('./targets/tapToContinue.png', confidence=0.9)
            moveMouseTo(findingContinue)
            return True

    if defeat :
        print('Derrota!')
        findingContinue = pyautogui.locateOnScreen('./targets/tapToContinue2.png', confidence=0.9)
        moveMouseTo(findingContinue)
        return True


def main():

   while True :
    findingEnergy = pyautogui.locateOnScreen('./targets/energy.png', confidence=0.9)
    if findingEnergy :
        print('Guerreiros descansados, para a luta!')
        findingHuntButton = pyautogui.locateOnScreen('./targets/bosshunt.png', confidence=0.9)
        if findingHuntButton:
            moveMouseTo(findingHuntButton)
            inHunt = True
            print('Batalha Iniciada!')
            time.sleep(15)
            pyautogui.click()
            while inHunt :
                if huntAreStarted() :
                    inHunt = False
    else : 
        print('Guerreiros ainda não descansaram')
        time.sleep(15)


if __name__ == "__main__":
    main()

    