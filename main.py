import quest
import reward
import purchase
import dailies
import file
import battle
import rewinder
import enum
import game_functions as game
import wrappers as event

class image(enum.Enum):
    skill_damage_icon = "C:\\project\\DBG_Automation\\img\\battle\\skillDamageIcon.PNG"
    skill_devastation = "C:\\project\\DBG_Automation\\img\\battle\\skill_devastation.PNG"
    skill_crit_chance = "C:\\project\\DBG_Automation\\img\\battle\\skill_critchance.PNG"
    expedition_hell = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hell.PNG"
    leviathan_button = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\leviathan_button.PNG"
    leviathan_1 = "C:\\project\\DBG_Automation\\img\\battle\\hunt\\leviathan_1.PNG"

#Initialisation
json_dailies = "C:\\project\\DBG_Automation\\data\\dailies.json"
daily_status = file.load_json(json_dailies)

json_rewards = "C:\\project\\DBG_Automation\\data\\rewards.json"
rewards_list = file.load_json(json_rewards)
reward = reward.Rewards(rewards_list)

json_quest_list = "C:\\project\\DBG_Automation\\data\\quests.json"
quest_list = file.load_json(json_quest_list)
quest = quest.Quest(quest_list)

json_purchase_list = "C:\\project\\DBG_Automation\\data\\purchases.json"
purchase_list = file.load_json(json_purchase_list)
purchase = purchase.Purchase(purchase_list)

rewinder = rewinder.Rewinder()

#Main Loop
x = 0

while x == 0:
    try:
        game.check_menu_popups(quest, reward, purchase, daily_status)
        """Battle 1"""
        game.level_battle_skill(image.skill_crit_chance.value)
        battle.campaign()
        game.check_menu_popups(quest, reward, purchase, daily_status)
        #game.level_battle_skill(image.skill_devastation.value)
        game.level_battle_skill(image.skill_crit_chance.value)
        """Battle 2"""
        # battle.campaign()
        # game.check_menu_popups(quest, reward, purchase, daily_status)
        # game.level_battle_skill(image.skill_damage_icon.value)
        """Extra Quest Battle"""
        battle.additional_quest_battles(quest)
        game.check_menu_popups(quest, reward, purchase, daily_status)
        """Extra Dungeon Battle"""
        # battle.dungeon(60)
        # game.check_menu_popups(quest, reward, purchase, daily_status)
        """Extra Excavation Battle"""
        # battle.expedition(image.expedition_hell.value)
        # game.check_menu_popups(quest, reward, purchase, daily_status)
        """Dailies Subroutine"""
        if daily_status["status"]["all_completed"] == False:
            daily_status["status"]["all_completed"] = dailies.update_all(quest, reward, purchase)
            file.save_json(daily_status)
        """Rewind"""
        rewinder.rewind()
        rewinder.level_skill()
    except:
        game.restart_game()