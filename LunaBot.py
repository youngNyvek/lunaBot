import pyautogui
import time

def moveMouseTo(imageFound):
    imgX, imgY = pyautogui.center(imageFound)
    pyautogui.moveTo(imgX, imgY, 2)
    pyautogui.click()
    time.sleep(5)


def resetWarriors():
    findingAreAdded = pyautogui.locateAllOnScreen('./targets/areAdded.png', confidence=0.9)
    for areAdded in findingAreAdded :
        moveMouseTo(areAdded)
        time.sleep(5)


def huntAreStarted():
    time.sleep(10)
    victory = pyautogui.locateOnScreen('./targets/victory.png', confidence=0.9)
    defeat = pyautogui.locateOnScreen('./targets/defeat.png', confidence=0.9)
    if victory :
        print('Vitória!')
        findingOpenChest = pyautogui.locateOnScreen('./targets/openChest.png', confidence=0.9)
        if findingOpenChest :
            moveMouseTo(findingOpenChest)
            findingContinue = pyautogui.locateOnScreen('./targets/tapToContinue.png', confidence=0.9)
            if findingContinue :
                moveMouseTo(findingContinue)
                return True

    if defeat :
        print('Derrota!')
        findingContinue = pyautogui.locateOnScreen('./targets/tapToContinue2.png', confidence=0.9)
        if findingContinue :
            moveMouseTo(findingContinue)
            return True

def maxWarriorsToBeAdded(num):
    if num < 3:
        return num 
    return 3

def main():

   while True :
    resetWarriors()
    findingEnergy = list(pyautogui.locateAllOnScreen('./targets/energy.png', confidence=0.9))
    if findingEnergy :
        for i in range(0, maxWarriorsToBeAdded(len(findingEnergy))):
            moveMouseTo(findingEnergy[i])
        print('To the battle!')
        findingHuntButton = pyautogui.locateOnScreen('./targets/bosshunt.png', confidence=0.9)
        if findingHuntButton:
            moveMouseTo(findingHuntButton)
            inHunt = True
            print('Battle started!')
            time.sleep(15)
            pyautogui.click()
            while inHunt :
                if huntAreStarted() :
                    inHunt = False
    else : 
        print('No warrior with energy')
        time.sleep(15)


if __name__ == "__main__":
    main()

    