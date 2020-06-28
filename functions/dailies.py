import pyautogui
import time
import json
import wrappers as event
import file
import reward
import quest
import purchase
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

def update_all(quest, reward, purchase):
    """
    Inputs: all daily objects (quest, reward, purchase)
    Outputs: 
    If update is all completed: Return true
    If not all tasks are completed: Return false
    """
    completed_dailies=[]

    if quest.is_completed() == False:
        event.log("INFO", "dailies.update_all", "Started Quest Update")
        completed_dailies.append(update_quests(quest))
    else:
        completed_dailies.append(True)

    if reward.is_completed() == False:
        event.log("INFO", "dailies.update_all", "Started Rewards Update")
        completed_dailies.append(update_rewards(reward))
    else:
        completed_dailies.append(True)

    if purchase.is_completed() == False:
        event.log("INFO", "dailies.update_all", "Started Purchases Update")
        completed_dailies.append(update_purchases(purchase))
    else:
        completed_dailies.append(True)

    print(completed_dailies)
    for outcome in completed_dailies:
        print('update all evaluation: ',outcome)
        if outcome == False:
            return False
    #print(len(completed_dailies))
    if len(completed_dailies) == 3:
        return True
    else:
        return False


def update_rewards(rewards):
    """
    input: rewards
    output: true/false
    """
    status = rewards.get_daily_friendships()
    print(status)
    if status != False:
        file.save_json(status)
    
    status = rewards.get_daily_gem_ads()
    print(status)
    if status != False:
        file.save_json(status)

    status = rewards.get_daily_summon()
    print(status)
    if status != False:
        file.save_json(status)
    
    for value in status.values():
        if value == False:
            return False
    
    return True
        
def update_quests(quest):
    """
    input: quests
    output: true/false
    """
    txt_var = "All quests completed? "+ str(quest.quest_list["status"]["quest_checked"])
    event.log("DEBUG", "dailies.update_quests", txt_var)
    if quest.quest_list["status"]["quest_checked"] == False:
        event.log("DEBUG", "dailies.update_quests", "Checking quests Loop Start")
        quest.quest_list = quest.check_quests()
    quest.quest_list["status"]["quests_completed"] = quest.claim_quests()
    file.save_json(quest.quest_list)
    return quest.quest_list["status"]["quests_completed"]


def update_purchases(purchase):
    """
    input: purchases
    output: true/false
    """
    status = purchase.spend_friendship()
    print(status)
    if status != False:
        file.save_json(status)
    
    status = purchase.spend_fossils()
    print(status)
    if status != False:
        file.save_json(status)
    
    for value in status.values():
        if value == False:
            return False
    
    return True

def reset_all(quest, reward, purchase, json_daily_status):
    quest.quest_list["status"] = quest.reset_all()
    reward.rewards_list["status"] = reward.reset_all()
    purchase.purchase_list["status"] = purchase.reset_all()
    json_daily_status["status"]["all_completed"] = False
    file.save_json(quest.quest_list)
    file.save_json(reward.rewards_list)
    file.save_json(purchase.purchase_list)
    file.save_json(json_daily_status)


# def evaluate_progress():
#     """
#     input: an array
#     output: a dictionary/json object
#     """
#     print("test")

# class Dailies:
#     def __init__(self,dailies_list):
#         self.dailies_list = dailies_list
    
#     def check_rewards(self, rewards, quests, ):
#         if rewards.is_completed == False:
#             file.save_json(rewards.get_daily_friendships())
#             file.save_json(rewards.get_daily_gem_ads())
#             file.save_json(rewards.get_daily_summon())

#         if quest
#     def check_quests(self):
#         print("test")

#     def check_purchases(self):
#         print("test")

#     def is_completed(self):
#         print("test")