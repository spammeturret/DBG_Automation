import wrappers as event
import dailies
import exceptions
import enum
import time
import pyautogui


class image(enum.Enum):
    #Campaign Image Paths
    bluestacks_logo = "C:\\project\\DBG_Automation\\img\\ads\\bs_logo.PNG"
    stop_macro = "C:\\project\\DBG_Automation\\img\\battle\\macro_stop.PNG"
    battle_button = "C:\\project\\DBG_Automation\\img\\battle\\battle.PNG"
    #Restart Image Paths
    close_app = "C:\\project\\DBG_Automation\\img\\others\\app_close.PNG"
    app_icon = "C:\\project\\DBG_Automation\\img\\others\\app_icon.PNG"
    app_tab = "C:\\project\\DBG_Automation\\img\\others\\app_tab.PNG"
    home_tab = "C:\\project\\DBG_Automation\\img\\others\\home_tab.PNG"
    welcome_prompt = "C:\\project\\DBG_Automation\\img\\others\\welcome_prompt.PNG"
    welcome_text = "C:\\project\\DBG_Automation\\img\\others\\welcome_text.PNG"
    #Daily Image Paths
    title_check_in = "C:\\project\\DBG_Automation\\img\\daily\\titleCheckIn.PNG"
    check_in_claim = "C:\\project\\DBG_Automation\\img\\daily\\checkInClaim.PNG"
    check_in_close = "C:\\project\\DBG_Automation\\img\\daily\\checkInClose.PNG"
    weapons_icon = "C:\\project\\DBG_Automation\\img\\daily\\weapons_icon.PNG"
    confirm_button = "C:\\project\\DBG_Automation\\img\\daily\\summon_confirm.PNG"
    skill_knockback_icon = "C:\\project\\DBG_Automation\\img\\battle\\skill_knock_back.PNG"

    progress_update_popup = "C:\\project\\DBG_Automation\\img\\daily\\progress_update_popup.PNG"
    progress_update_claim = "C:\\project\\DBG_Automation\\img\\daily\\progress_update_claim.PNG"


def watchAds(adButton, verifyImg):
    event.click_button_validate(adButton,exceptions.ad_refresh_error)
    time.sleep(40)
    event.click_next_screen_validate_offset(image.bluestacks_logo.value, 1272, 73, verifyImg, exceptions.ad_refresh_error)
    
def restart_game():
    if event.find_image(image.stop_macro.value) == True:
        event.search_click(image.stop_macro.value)
    event.search_click(image.app_tab.value)
    event.search_click(image.close_app.value)
    event.click_next_screen_validate(image.home_tab.value, image.app_icon.value)
    event.search_click(image.app_icon.value)
    while event.find_image(image.battle_button.value) == False:
        event.search_click(image.welcome_text.value)


# def dailyCompletionEvaluate():
#     flag = True
#     for activity, status in dailyCompletions.items():
#         print(activity, status)
#         if activity != "dailyRewards" and status == False:
#             flag = False
    
#     save_dailyCompletions("dailyRewards", flag)



def check_menu_popups(quest, reward, purchase, json_daily_status):
    """
    input: none
    output: true/false
    """
    while event.find_image(image.skill_knockback_icon.value) == False and event.find_image(image.battle_button.value) == True:
        if event.find_image(image.title_check_in.value) == True:
            clear_daily_popup(quest, reward, purchase, json_daily_status)
        elif event.find_image(image.progress_update_popup.value) == True:
            event.search_click(image.progress_update_claim.value)
        else:
            return "none"

# def check_progress_update():
#     """
#     input: none
#     output: none
#     """
#     if event.find_image(image.progress_update_popup.value) == True:
#         event.search_click(image.progress_update_claim.value)
#     else:
#         return
    
def clear_daily_popup(quest, reward, purchase, json_daily_status):
    """
    input: none
    output: none
    """
    count = 0
    dailies.reset_all(quest, reward, purchase, json_daily_status)
    event.search_click(image.check_in_claim.value)
    if image.check_in_close == False and image.confirm_button.value == False:
        pyautogui.click(560,400)
        time.sleep(2)
    if event.find_image(image.confirm_button.value) != False:
        event.search_click(image.confirm_button.value)
    while event.find_image(image.skill_knockback_icon.value) == False:
        event.search_click(image.check_in_close.value)
        count += 1
        if count == 10:
            raise Exception("Daily Reward Failure - Game Restarted")
    return True

def macro_start(img_path):
    print(img_path)
    pyautogui.hotkey('ctrl', 'shiftleft', '7')
    event.search_click_offset(img_path,457,4)

def level_battle_skill(img_skill):
    "starting level_battle_skill"
    event.search_click_offset(img_skill, 435, 34)
    print("done")

#def sell_gear():