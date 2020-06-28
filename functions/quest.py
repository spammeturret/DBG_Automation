import enum
import time
import pyautogui
#import file
#import image
import wrappers as event
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop


class image(enum.Enum):
    quest_icon = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_icon.PNG"
    quest_claim = "C:\\project\\DBG_Automation\\img\\daily\\quests\\questClaim.PNG"
    quest_dungeon = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_dungeon.PNG"
    quest_spells =  "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_spells.PNG"
    quest_expedition = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_expedition.PNG"
    quest_leviathan = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_leviathan.PNG"
    quest_asmodeus = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_asmodeus.PNG"
    quest_claim_x5 = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_claim_x5.PNG"
    quest_claim_x15 = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_claim_x15.PNG"
    quest_scroll_down = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_scroll_down.PNG"
    close_quest = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_close.PNG"
    quest_completed_all = "C:\\project\\DBG_Automation\\img\\daily\\quests\\all_quests_completed.PNG"
    quest_window_title = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_window_title.PNG"

class Quest:
    def __init__(self,quest_list):
        self.quest_list = quest_list
        
    def is_completed(self):
        print('quest is_completed: ',self.quest_list["status"]["quests_completed"])
        return self.quest_list["status"]["quests_completed"]
        # outcome = False
        # event.search_click(image.quest_icon.value)
        # if event.find_image(image.quest_completed_all.value) == True:
        #     outcome = True
        # #event.search_click(image.close_quest.value)
        # print('quest outcome is:', outcome)
        # event.search_click(image.close_quest.value)
        # return outcome

    def check_quests(self):
        """
        Input: none
        Output: (Dictionary) full updated quest dictionary 
        """
        #active_quests = []
        # print('quest list - status - quest_checked', self.quest_list["status"]["quest_checked"])
        if event.find_image(image.quest_window_title.value) == False:
            event.search_click(image.quest_icon.value)
            time.sleep(1)
        if event.find_image(image.quest_dungeon.value):
            self.quest_list["status"]["dungeon"] = True
        if event.find_image(image.quest_spells.value):
            self.quest_list["status"]["spells"] = True
        if event.find_image(image.quest_expedition.value):
            self.quest_list["status"]["expedition"] = True
        if event.find_image(image.quest_leviathan.value):
            self.quest_list["status"]["leviathan"] = True
        if event.find_image(image.quest_asmodeus.value):
            self.quest_list["status"]["asmodeus"] = True
        self.quest_list["status"]["quest_checked"] = True
        #event.search_click(image.close_quest.value)
        print('quest list is:', self.quest_list)
        return self.quest_list

    def claim_quests(self):
        """
        Description: Check quests and check off any quests that can be completed.
        Input: none
        Output: (Boolean) true or false
        """
        outcome = False
        #if self.quest_list["status"]["daily_quests"] != True: 
        if event.find_image(image.quest_window_title.value) == False:
            event.search_click(image.quest_icon.value)
        time.sleep(1)
        pyautogui.moveTo(1017, 419)
        pyautogui.dragTo(1017,438,0.5, button='left')
        while imagesearch(image.quest_claim_x5.value, 0.9)[0] != -1:
            event.search_click(image.quest_claim_x5.value)
        if imagesearch(image.quest_claim_x15.value, 0.9)[0] != -1:
            event.search_click(image.quest_claim_x15.value)
            outcome = True
        event.click_button_validate(image.close_quest.value)
        print('All quest claimed:', outcome)
        return outcome

    def reset_all(self):
        new_quests = {}
        for key in self.quest_list["status"]:
            new_quests[key] = False
        return new_quests

#{"quest_checked": false, "dungeon": false, "expedition": false, "spells": false}