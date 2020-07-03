import enum
import time
import pyautogui
import file
import game_functions as game
#import image
import wrappers as event
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

class image(enum.Enum):
    #General
    battle_button = "C:\\project\\DBG_Automation\\img\\battle\\battle.PNG"
    weapons_icon = "C:\\project\\DBG_Automation\\img\\daily\\weapons_icon.PNG"
    #Friendship Image Paths
    social_icon = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\social_icon.PNG"
    friends_menu = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\friends.PNG"
    friends_gift_all = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\gift_all.PNG"
    close = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\close.PNG"
    #Ads Image Paths
    ad_ruby = "C:\\project\\DBG_Automation\\img\\ads\\adRuby.PNG"
    ad_ruby_invalid = "C:\\project\\DBG_Automation\\img\\ads\\adRubyInvalid.PNG"
    ad_2x_gold = "C:\\project\\DBG_Automation\\img\\ads\\ad2xGold.PNG"
    bluestacks_logo = "C:\\project\\DBG_Automation\\img\\ads\\bs_logo.PNG"
    store_rubies = "C:\\project\\DBG_Automation\\img\\ads\\storeRubies.PNG"
    ads_close = "C:\\project\\DBG_Automation\\img\\ads\\close.PNG"
    #Store Image Paths
    store_icon = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_icon.PNG"
    store_close = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_close.PNG"
    store_friendship = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship.PNG"
    store_friendship_valid = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship_valid.PNG"
    store_friendship_invalid = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship_invalid.PNG"
    store_friendship_confirm = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship_confirm.PNG"
    #Character Image Paths
    character_icon = "C:\\project\\DBG_Automation\\img\\daily\\character_icon.PNG"
    character_ticket = "C:\\project\\DBG_Automation\\img\\daily\\character_ticket.PNG"
    classic_summon = "C:\\project\\DBG_Automation\\img\\daily\\classic_summon.PNG"
    free_summon = "C:\\project\\DBG_Automation\\img\\daily\\free_summon.PNG"
    summon_confirm = "C:\\project\\DBG_Automation\\img\\daily\\summon_confirm.PNG"
    summon_close = "C:\\project\\DBG_Automation\\img\\daily\\summon_close.PNG"

class Rewards:
    def __init__(self,rewards_list):
        self.rewards_list = rewards_list

    def get_daily_friendships(self):
        #Input: None
        #Output: Success of Operation
        print("Daily Friendship Status:", self.rewards_list["status"]["daily_friendship"])
        if self.rewards_list["status"]["daily_friendship"] == False:
            event.search_click(image.social_icon.value)
            event.search_click(image.friends_menu.value)
            time.sleep(5)
            event.search_click(image.friends_gift_all.value)
            self.rewards_list["status"]["daily_friendship"] = True
            event.click_next_screen_validate(image.close.value, image.battle_button.value)
        return self.rewards_list
            
    def get_daily_gem_ads(self):
        #Input: None
        #Output: Success of Operation

        print("Daily Gem Ads Status:", self.rewards_list["status"]["daily_free_gems"])
        if self.rewards_list["status"]["daily_free_gems"] == False:
            event.search_click(image.store_icon.value)
            time.sleep(1)
            while imagesearch(image.ad_ruby_invalid.value, 0.9)[0] == -1:
                game.watchAds(image.ad_ruby.value, image.store_rubies.value)
                time.sleep(2)
            self.rewards_list["status"]["daily_free_gems"] = True
        event.click_next_screen_validate(image.ads_close.value, image.battle_button.value)
        return self.rewards_list

    def get_daily_summon(self):
        #Input: None
        #Output: Success of Operation
        print("Daily Summon:", self.rewards_list["status"]["daily_free_summon"])
        if self.rewards_list["status"]["daily_free_summon"] == False:
            event.search_click(image.character_icon.value)
            event.search_click(image.character_ticket.value)
            event.search_click(image.classic_summon.value)
            if event.find_image(image.free_summon.value) == True:
                event.search_click(image.free_summon.value)
                event.click_next_screen_validate_offset(image.bluestacks_logo.value, 1272, 73, image.summon_confirm.value)
                event.search_click(image.summon_confirm.value)
                self.rewards_list["status"]["daily_free_summon"] = True
            else:
                self.rewards_list["status"]["daily_free_summon"] = True
            event.click_next_screen_validate(image.summon_close.value, image.weapons_icon.value)
                
                
        return self.rewards_list

    def is_completed(self):
        """
        input: none
        outputs: Boolean - If all requirements are completed
        """
        
        outcome = True
        for value in self.rewards_list["status"].values():
            if value == False:
                outcome = False
        print('reward is_completed:', outcome)
        return outcome

    def reset_all(self):
        new_rewards = {}
        for key in self.rewards_list["status"]:
            new_rewards[key] = False
        return new_rewards