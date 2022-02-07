import os
import pyautogui
import time
from rich.console import Console

console = Console()

victoriesCount = 0
defeatsCount = 0

def moveMouseTo(imageFound):
    imgX, imgY = pyautogui.center(imageFound)
    pyautogui.moveTo(imgX, imgY, 1)
    pyautogui.click()
    time.sleep(5)

def clear():
    os.system( 'cls' )

def consoleLog(message):
    clear()
    mainPrint = """  
    ________________________________________________________________
    |            hope i helped, please make a donation              |
    |                                                               |
    |                           PayPal                              |
    |     https://www.paypal.com/donate/?business=DCT8ZXRZYRJM4     |                                
    |                                                               |
    |                      BUSD - LUS - BNB                         |
    |           0x1128731221df2C7BF61736068004550C87B2880A          |                                
    |_______________________________________________________________|
     ________________________________________________________________
    |                                                               |                                
    |          In case the bot reading is wrong                     |
    |          try to change some image in the target folder        |                                
    |_______________________________________________________________|                                                              
    
    Infos (obtained since bot startup)      
                                                        
    🎉 Victories = {}                     
                                                        
    🧨 Defeats =  {}                         
       
    """.format(victoriesCount, defeatsCount, message)

    console.print(mainPrint)
    
    console.log(f"[blue]{message}")

def resetWarriors():
    consoleLog("Unchecking warriors for error prevention")
    findingAreAdded = pyautogui.locateAllOnScreen('./targets/areAdded.png', confidence=0.9)
    for areAdded in findingAreAdded :
        moveMouseTo(areAdded)
        time.sleep(5)

def maxWarriorsToBeAdded(num):
    if num < 3:
        return num 
    return 3

def huntAreStarted():
    global victoriesCount
    global defeatsCount
    time.sleep(10)
    victory = pyautogui.locateOnScreen('./targets/victory.png', confidence=0.9)
    defeat = pyautogui.locateOnScreen('./targets/defeat.png', confidence=0.9)
    if victory :
        victoriesCount += 1
        consoleLog('Victory!')
        findingOpenChest = pyautogui.locateOnScreen('./targets/openChest.png', confidence=0.9)
        if findingOpenChest :
            moveMouseTo(findingOpenChest)
            findingContinue = pyautogui.locateOnScreen('./targets/tapToContinue.png', confidence=0.9)
            if findingContinue :
                moveMouseTo(findingContinue)
                return True

    if defeat :
        defeatsCount += 1
        consoleLog('Defeat!')
        findingContinue = pyautogui.locateOnScreen('./targets/tapToContinue2.png', confidence=0.9)
        if findingContinue :
            moveMouseTo(findingContinue)
            return True


def main():
    with console.status("[bold green]LunaBot is running...") as status:
        while True :
            resetWarriors()
            findingEnergy = list(pyautogui.locateAllOnScreen('./targets/energy.png', confidence=0.9))
            if findingEnergy :
                consoleLog('Selecting warriors!')
                for i in range(0, maxWarriorsToBeAdded(len(findingEnergy))):
                    moveMouseTo(findingEnergy[i])
                consoleLog('To the battle!')
                findingHuntButton = pyautogui.locateOnScreen('./targets/bosshunt.png', confidence=0.9)
                if findingHuntButton:
                    moveMouseTo(findingHuntButton)
                    inHunt = True
                    consoleLog('Battle started!')
                    time.sleep(15)
                    pyautogui.click()
                    while inHunt :
                        if huntAreStarted() :
                            inHunt = False
            else : 
                consoleLog('No warriors with energy were found.')
                time.sleep(15)


if __name__ == "__main__":

    main()

    