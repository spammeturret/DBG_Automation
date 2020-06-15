import pyautogui ,daily
import time
import json
import error_handler as exception
import file_handler as data
import wrappers as image

from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

#set up variables
x = 0
#Load json states


print(dailyCompletions)
# dailyStatusReset()
# checkDailyStatus()

#campaign()

#print(image.find_image(imgGoldPrompt))
#Run Loop
while x == 0:
    try:
        campaign()
        levelBattleSkill()
        campaign()
        levelBattleSkill()
        additionalQuestBattles()
        checkDailyStatus()
        rewind()
        skillproperties["index"] = levelSkill(skillproperties)
    except:
        restart_game()
        print("An issue has occured, game loop restarted")

#make sure questChecked is only toggled when quest screen is verified

# if quest.is_completed()
#    save_json(quest_list...)

# def is_completed():
#    if self.quest is completed:
#      return true