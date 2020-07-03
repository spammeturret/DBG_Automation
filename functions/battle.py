import enum
import quest
import time
import pyautogui
import file
import game_functions as game
#import image
import wrappers as event
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

class image(enum.Enum):
    #Campaign Image Paths
    battle_button = "C:\\project\\DBG_Automation\\img\\battle\\battle.PNG"
    campaign_button = "C:\\project\\DBG_Automation\\img\\battle\\campaign.PNG"
    ad_2x_gold = "C:\\project\\DBG_Automation\\img\\ads\\ad2xGold.PNG"
    gold_prompt = "C:\\project\\DBG_Automation\\img\\battle\\x2_gold_prompt.PNG"
    health_bar = "C:\\project\\DBG_Automation\\img\\battle\\health.PNG"
    start_macro = "C:\\project\\DBG_Automation\\img\\battle\\macro_play.PNG"
    stop_macro = "C:\\project\\DBG_Automation\\img\\battle\\macro_stop.PNG"
    defeat_prompt = "C:\\project\\DBG_Automation\\img\\battle\\defeat.PNG"
    back_button = "C:\\project\\DBG_Automation\\img\\battle\\back.PNG"
    skill_damage = "C:\\project\\DBG_Automation\\img\\battle\\skillDamage.PNG"
    skill_damage_icon = "C:\\project\\DBG_Automation\\img\\battle\\skillDamageIcon.PNG"
    weapon_crate = "C:\\project\\DBG_Automation\\img\\battle\\weapons_crate.PNG"
    x2_Battle = "C:\\project\\DBG_Automation\\img\\battle\\x2_battle.PNG"
    battle_next = "C:\\project\\DBG_Automation\\img\\battle\\battle_next.PNG"
    victory_prompt = "C:\\project\\DBG_Automation\\img\\battle\\victory.PNG"
    skill_knockback_icon = "C:\\project\\DBG_Automation\\img\\battle\\skill_knock_back.PNG"
    ok_button = "C:\\project\\DBG_Automation\\img\\rewind\\ok.png"
    normal_macro = "C:\\project\\DBG_Automation\\img\\macro\\battle_normal.PNG"
    spell_macro = "C:\\project\\DBG_Automation\\img\\macro\\battle_spell.PNG"

    #Dungeon Image Paths
    dungeon = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon.PNG"
    dungeon_down = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_down.PNG"
    dungeon_enter = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_enter.PNG"
    dungeon_leave = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_leave.PNG"
    dungeon_pause = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_pause.PNG"

    #Expedition Image Paths
    expedition = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition.PNG"
    expedition_easy = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_easy.PNG"
    expedition_normal = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_normal.PNG"
    expedition_hard = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hard.PNG"
    expedition_hell = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hell.PNG"
    small_back = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_back.PNG"

    #Hunt Image Paths
    hunt = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\hunt_button.PNG"
    hunt_over = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\hunt_over.PNG"
    hunt_close = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\hunt_close.PNG"
    insufficient_slots = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\insufficient_slots.PNG"
    asmodeus_button = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\asmodeus_button.PNG"
    asmodeus_1 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\asmodeus_1.PNG"
    asmodeus_2 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\asmodeus_2.PNG"
    leviathan_button = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\leviathan_button.PNG"
    leviathan_1 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\leviathan_1.PNG"
    leviathan_2 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\leviathan_2.PNG"
    belphegor_button = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\belphegor_button.PNG"
    belphegor_1 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\belphegor_1.PNG"
    mammon_button = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\mammon_button.PNG"
    mammon_1 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\mammon_1.PNG"




def campaign():
    event.log("FUNCTION", "battle.campaign", "Starting Campaign Function")
    event.search_click(image.battle_button.value)
    event.search_click(image.campaign_button.value)
    #print (event.find_image(image.ad_2x_gold.value))
    time.sleep(0.2)
    if event.find_image(image.ad_2x_gold.value) == True:
        game.watchAds(image.ad_2x_gold.value, image.health_bar.value)
    elif event.find_image(image.ok_button.value) != False:
        event.search_click(image.ok_button.value)
    game.macro_start(image.normal_macro.value)
    while event.find_image(image.defeat_prompt.value, True) == False:
        if imagesearch(image.weapon_crate.value)[0] != -1:
            print("Weapons crate found")
            event.search_click(image.stop_macro.value, 0)
            game.watchAds(image.x2_Battle.value, image.victory_prompt.value)
            time.sleep(3)
            event.search_click(image.battle_next.value)
            game.macro_start(image.normal_macro.value)
    exit_battle(image.back_button.value)

def dungeon(timeLimit):
    event.log("FUNCTION", "battle.dungeon", "Starting Dungeon Function")
    timer = 0
    event.search_click(image.battle_button.value)
    event.search_click(image.dungeon.value)
    event.search_click(image.dungeon_down.value)
    event.search_click(image.dungeon_down.value)
    event.search_click(image.dungeon_down.value)
    event.search_click(image.dungeon_down.value)
    event.search_click(image.dungeon_enter.value)
    time.sleep(1)
    game.watchAds(image.ad_2x_gold.value, image.health_bar.value)
    game.macro_start(image.spell_macro.value)
    #if (30 minutes or defeat shows up:)
    while event.find_image(image.small_back.value, True) == False and timer <= timeLimit:
        time.sleep(60)
        timer += 1
        print("Time Elapsed: ", timer)
    if event.find_image(image.small_back.value) != False:
        print("defeated!")
    elif timer >= timeLimit:
        event.search_click(image.stop_macro.value)
        event.search_click(image.dungeon_pause.value)
        event.search_click(image.dungeon_leave.value)
        event.search_click(image.ok_button.value)
    exit_battle(image.small_back.value)

def expedition(imgPathDifficulty):
    event.log("FUNCTION", "battle.expedition", "Starting Expedition Function")
    event.search_click(image.battle_button.value,1)
    event.search_click(image.expedition.value, 1)
    event.search_click(imgPathDifficulty)
    event.search_click(image.ok_button.value)
    game.macro_start(image.spell_macro.value)
    while event.find_image(image.small_back.value, True) == False:
        time.sleep(0.5)
    #imagesearch_loop(image.small_back.value, 1)
    exit_battle(image.small_back.value)

def exit_battle (exit_button):
    event.search_click(image.stop_macro.value)
    while event.find_image(image.battle_button.value) == False:
        event.search_click(exit_button)
        time.sleep(3)

def hunt(boss_type, level, repeat_number):
    """Input: What Boss to fight, what level to fight at, how many times to fight"""
    exit_flag = False
    inventory_full_flag = False
    i = 0
    event.search_click(image.battle_button.value)
    event.search_click(image.hunt.value)
    event.search_click(boss_type)
    event.search_click(level)
    time.sleep(0.5)
    if event.find_image(image.insufficient_slots.value) == True:
        print("test")
        inventory_full_flag = True
        event.search_click(image.ok_button.value)
        event.search_click(image.hunt_close.value)
    
    print(inventory_full_flag)

    if inventory_full_flag == False:
        event.search_click(image.ok_button.value)
        game.macro_start(image.normal_macro.value)
        while i < repeat_number or exit_flag == True:
            if event.find_image(image.hunt_over.value, True) == True:
                i += 1
                print("Hunt Count:", i)
                while event.find_image(image.hunt_over.value, True) == True:
                #If it has repeated enough, exit battle
                    if i == repeat_number:
                        exit_flag = True
                        print("loop - exit")
                        event.search_click(image.stop_macro.value, 0)
                        exit_battle(image.back_button.value)
                        #event.click_next_screen_validate(image.back_button.value,image.battle_button.value,click_limit= 20)
                    #if it hasnt repeated enough times, check for items full
                    elif event.find_image(image.insufficient_slots.value, True) == True:
                        inventory_full_flag = True
                        exit_flag = True
                        event.search_click(image.stop_macro.value)
                        exit_battle(image.ok_button.value)
                        #exit_battle(image.back_button.value)
            
    if inventory_full_flag == True:
        game.sell_hunt_gear()

def additional_quest_battles(quest):
    if quest.is_completed() == False:
        if quest.quest_list["status"]["dungeon"] == True:
            print("dungeon quest: True")
            dungeon(30)
        if quest.quest_list["status"]["expedition"] or quest.quest_list["status"]["spells"] == True:
            print("expedition/spells quest: True")
            expedition(image.expedition_hell.value)
        if quest.quest_list["status"]["leviathan"] == True:
            print("leviathan hunt quest: True")
            hunt(image.leviathan_button.value, image.leviathan_1.value, 1)
        if quest.quest_list["status"]["asmodeus"] == True:
            print("asmodeus hunt quest: True")
            hunt(image.asmodeus_button.value, image.asmodeus_1.value, 3)