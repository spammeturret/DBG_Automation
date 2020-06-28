import pyautogui
import wrappers as event
import game_functions as game
import enum

class image(enum.Enum):
    rewind_menu = "C:\\project\\DBG_Automation\\img\\rewind\\rewind.png"
    #ok_button = "C:\\project\\DBG_Automation\\img\\rewind\\ok.png"
    skill_damage = "C:\\project\\DBG_Automation\\img\\battle\\skillDamage.PNG"
    skill_damage_icon = "C:\\project\\DBG_Automation\\img\\battle\\skillDamageIcon.PNG"
    #Rewind Image Paths
    #rewind_menu = "C:\\project\\DBG_Automation\\img\\rewind\\rewind.png"
    rewind_menu_active = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_active.png"
    rewind_select = "C:\\project\\DBG_Automation\\img\\rewind\\elixir_icon.png"
    rewind_confirm = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_confirm.png"
    ok_button = "C:\\project\\DBG_Automation\\img\\rewind\\ok.png"
    rewind_locked = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_error4.PNG"
    stat_icon = "C:\\project\\DBG_Automation\\img\\rewind\\Stat.png"

    skill_devastation = "C:\\project\\DBG_Automation\\img\\battle\\skill_devastation.PNG"


def levelSkill(skillproperties):
    event.search_click(image.rewind_menu.value)
    index = skillproperties["index"]
    array = skillproperties["skillList"]
    skill_image_path = array[index]
    #make sure to scroll for skills below default view
    if 'scroll' in skill_image_path:
        pyautogui.moveTo(1234,267)
        pyautogui.dragTo(1234,365,0.5, button='left')
    event.search_click_offset(skill_image_path, 470, 25)
    event.search_click(image.ok_button.value)
    #increment array to select next skill
    if index == len(array)-1:
        index = 0
    else:
        index += 1
    return index

# def levelBattleSkill():
#     while event.find_image(image.skill_damage.value) == False:
#         game.check_daily_popup()
#     event.search_click_offset(image.skill_damage_icon, 435, 34)

def rewind():
    print("rewind start")
    event.search_click(image.rewind_menu.value)
    while event.find_image(image.rewind_locked.value) == False:
        event.search_click(image.rewind_select.value)
        event.search_click(image.rewind_confirm.value)
        event.search_click(image.stat_icon.value)
        game.level_battle_skill(image.skill_devastation.value)
        event.search_click(image.rewind_menu.value)