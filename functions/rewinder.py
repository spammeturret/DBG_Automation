import enum
import wrappers as event
import pyautogui
import game_functions as game

class image(enum.Enum):
    skill_multi_elixir = "C:\\project\\DBG_Automation\\img\\skills\\elixir_mastery.PNG"
    skill_add_dmg = "C:\\project\\DBG_Automation\\img\\skills\\hidden_strength.PNG"
    skill_multi_dmg = "C:\\project\\DBG_Automation\\img\\skills\\untapped_power.PNG"
    skill_multi_mob_dmg = "C:\\project\\DBG_Automation\\img\\skills\\mob_slayer.PNG"
    skill_multi_boss_dmg = "C:\\project\\DBG_Automation\\img\\skills\\boss_slayer.PNG"
    skill_add_crit_dmg = "C:\\project\\DBG_Automation\\img\\skills\\explosive_strength_scroll.PNG"
    skill_multi_crit_dmg = "C:\\project\\DBG_Automation\\img\\skills\\beautiful_disaster_scroll.PNG"
    skill_multi_hero_dmg = "C:\\project\\DBG_Automation\\img\\skills\\inspire_scroll.PNG"
    skill_multi_gold = "C:\\project\\DBG_Automation\\img\\skills\\hard_labour_scroll.PNG"

    #Rewind Image Paths
    rewind_menu = "C:\\project\\DBG_Automation\\img\\rewind\\rewind.png"
    rewind_menu_active = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_active.png"
    rewind_select = "C:\\project\\DBG_Automation\\img\\rewind\\elixir_icon.png"
    rewind_confirm = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_confirm.png"
    ok_button = "C:\\project\\DBG_Automation\\img\\rewind\\ok.png"
    rewind_locked = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_error4.PNG"
    stat_icon = "C:\\project\\DBG_Automation\\img\\rewind\\Stat.png"
    skill_devastation = "C:\\project\\DBG_Automation\\img\\battle\\skill_devastation.PNG"

    #skills


class Rewinder:
    def __init__(self):
        self.skill_index = 0
        self.skill_list = [
            image.skill_multi_elixir.value
            # image.skill_multi_dmg.value,
            # image.skill_multi_mob_dmg.value,
            # image.skill_multi_boss_dmg.value,
            # image.skill_multi_crit_dmg.value,
            # image.skill_multi_hero_dmg.value,
            # image.skill_multi_gold.value
        ]

# imgMultiElixir,
#         imgMultiDmg,
#         imgMultiMobDmg,
#         imgMultiBossDmg,
#         imgMultiCritDmg,
#         imgMultiHeroDmg,
#         imgMultiGold

    def level_skill(self):
        """
        Input: none
        output: none
        """
        event.search_click(image.rewind_menu.value)
        index = self.skill_index
        array = self.skill_list
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
        #return array back to self
        self.skill_index = index
        return

    def rewind(self):
        event.log("INFO", "event.rewind", "Starting Rewind Loop")
        event.search_click(image.rewind_menu.value)
        event.search_click(image.rewind_select.value)
        event.search_click(image.rewind_confirm.value)
        # while event.find_image(image.rewind_locked.value) == False:
        #     event.search_click(image.rewind_select.value)
        #     event.search_click(image.rewind_confirm.value)
        return