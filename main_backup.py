import pyautogui, time, json
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

####################################################################################################################
#Image Path#
####################################################################################################################

#filePaths
jsonDailyCompletions = "C:\\project\\DBG_Automation\\dailyCompletions.json"
jsonQuestList = "C:\\project\\DBG_Automation\\questList.json"

#Rewind Image Paths
imgRewindMenu = "C:\\project\\DBG_Automation\\img\\rewind\\rewind.png"
imgRewindMenuActive = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_active.png"
imgRewindSelect = "C:\\project\\DBG_Automation\\img\\rewind\\elixir_icon.png"
imgRewindConfirm = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_confirm.png"
imgOK = "C:\\project\\DBG_Automation\\img\\rewind\\ok.png"
imgRewindLocked = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_error4.PNG"
imgStatIcon = "C:\\project\\DBG_Automation\\img\\rewind\\Stat.png"

#Macro Image Paths
imgMacroNormal = "C:\\project\\DBG_Automation\\img\\macro\\battle_normal.PNG"
imgMacroSpell = "C:\\project\\DBG_Automation\\img\\macro\\battle_spell.PNG"

#Campaign Image Paths
imgBattle = "C:\\project\\DBG_Automation\\img\\battle\\battle.PNG"
imgCampaign = "C:\\project\\DBG_Automation\\img\\battle\\campaign.PNG"
imgGoldPrompt = "C:\\project\\DBG_Automation\\img\\battle\\x2_gold_prompt.PNG"
imgHealthBar = "C:\\project\\DBG_Automation\\img\\battle\\health.PNG"
imgMacroPlay = "C:\\project\\DBG_Automation\\img\\battle\\macro_play.PNG"
imgMacroStop = "C:\\project\\DBG_Automation\\img\\battle\\macro_stop.PNG"
imgDefeat = "C:\\project\\DBG_Automation\\img\\battle\\defeat.PNG"
imgBack = "C:\\project\\DBG_Automation\\img\\battle\\back.PNG"
imgSkillDamage = "C:\\project\\DBG_Automation\\img\\battle\\skillDamage.PNG"
imgSkillDamageIcon = "C:\\project\\DBG_Automation\\img\\battle\\skillDamageIcon.PNG"
imgWeaponCrate = "C:\\project\\DBG_Automation\\img\\battle\\weapons_crate.PNG"
img2xBattle = "C:\\project\\DBG_Automation\\img\\battle\\x2_battle.PNG"
imgBattleNext = "C:\\project\\DBG_Automation\\img\\battle\\battle_next.PNG"
imgVictory = "C:\\project\\DBG_Automation\\img\\battle\\victory.PNG"
imgSkillKnockBack = "C:\\project\\DBG_Automation\\img\\battle\\skill_knock_back.PNG"

#Dungeon Image Paths
imgDungeon = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon.PNG"
imgDungeonDown = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_down.PNG"
imgDungeonEnter = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_enter.PNG"
imgDungeonLeave = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_leave.PNG"
imgDungeonPause = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_pause.PNG"

#Expedition Image Paths
imgExpedition = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition.PNG"
imgExpeditionHard = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hard.PNG"
imgExpeditionHell = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hell.PNG"
imgSmallBack = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_back.PNG"

#Ads Image Paths
imgAdRuby = "C:\\project\\DBG_Automation\\img\\ads\\adRuby.PNG"
imgAdRubyInvalid = "C:\\project\\DBG_Automation\\img\\ads\\adRubyInvalid.PNG"
imgAd2xGold = "C:\\project\\DBG_Automation\\img\\ads\\ad2xGold.PNG"
imgBlueStacks = "C:\\project\\DBG_Automation\\img\\ads\\bs_logo.PNG"
imgStoreRubies = "C:\\project\\DBG_Automation\\img\\ads\\storeRubies.PNG"
imgAdsClose = "C:\\project\\DBG_Automation\\img\\ads\\close.PNG"

#Menu Image Paths
imgMenuSkills = "C:\\project\\DBG_Automation\\img\\screen_check\\menuSkills.PNG"
imgMenuSpells = "C:\\project\\DBG_Automation\\img\\screen_check\\menuSpells.PNG"
imgMenuStats = "C:\\project\\DBG_Automation\\img\\screen_check\\menuStats.PNG"
imgMenuWeapons = "C:\\project\\DBG_Automation\\img\\screen_check\\menuWeapons.PNG"
imgHeroesSkills = "C:\\project\\DBG_Automation\\img\\screen_check\\heroesSkills.PNG"

#Skill Image Paths
imgMultiElixir = "C:\\project\\DBG_Automation\\img\\rewind\\elixir_mastery.PNG"
imgAddDmg = "C:\\project\\DBG_Automation\\img\\skills\\hidden_strength.PNG"
imgMultiDmg = "C:\\project\\DBG_Automation\\img\\skills\\untapped_power.PNG"
imgMultiMobDmg = "C:\\project\\DBG_Automation\\img\\skills\\mob_slayer.PNG"
imgMultiBossDmg = "C:\\project\\DBG_Automation\\img\\skills\\boss_slayer.PNG"
imgAddCritDmg = "C:\\project\\DBG_Automation\\img\\skills\\explosive_strength_scroll.PNG"
imgMultiCritDmg = "C:\\project\\DBG_Automation\\img\\skills\\beautiful_disaster_scroll.PNG"
imgMultiHeroDmg = "C:\\project\\DBG_Automation\\img\\skills\\inspire_scroll.PNG"
imgMultiGold = "C:\\project\\DBG_Automation\\img\\skills\\hard_labour_scroll.PNG"

#Friendship Image Paths
imgSocialIcon = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\social_icon.PNG"
imgFriendsMenu = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\friends.PNG"
imgGiftAll = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\gift_all.PNG"
imgClose = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\close.PNG"

#Store Image Paths
imgStoreIcon = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_icon.PNG"
imgStoreClose = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_close.PNG"
imgStoreFriendship = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship.PNG"
imgStoreFriendshipValid = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship_valid.PNG"
imgStoreFriendshipInvalid = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship_invalid.PNG"
imgStoreFriendshipConfirm = "C:\\project\\DBG_Automation\\img\\daily\\store\\store_friendship_confirm.PNG"

#Quest Image Paths
imgQuestIcon = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_icon.PNG"
imgQuestClaim = "C:\\project\\DBG_Automation\\img\\daily\\quests\\questClaim.PNG"
imgQuestDungeon = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_dungeon.PNG"
imgQuestSpells = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_spells.PNG"
imgQuestExpedition = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_expedition.PNG"
imgQuestClaimx5 = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_claim_x5.PNG"
imgQuestClaimx15 = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_claim_x15.PNG"
imgQuestScrollDown = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_scroll_down.PNG"
imgQuestClose = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_close.PNG"

#Character Image Paths
imgCharacterIcon = "C:\\project\\DBG_Automation\\img\\daily\\character_icon.PNG"
imgCharacterTicket = "C:\\project\\DBG_Automation\\img\\daily\\character_ticket.PNG"
imgClassicSummon = "C:\\project\\DBG_Automation\\img\\daily\\classic_summon.PNG"
imgFreeSummon = "C:\\project\\DBG_Automation\\img\\daily\\free_summon.PNG"
imgSummonConfirm = "C:\\project\\DBG_Automation\\img\\daily\\summon_confirm.PNG"
imgSummonClose = "C:\\project\\DBG_Automation\\img\\daily\\summon_close.PNG"

#Daily Image Paths
imgTitleCheckIn = "C:\\project\\DBG_Automation\\img\\daily\\titleCheckIn.PNG"
imgCheckInClaim = "C:\\project\\DBG_Automation\\img\\daily\\checkInClaim.PNG"
imgCheckInClose = "C:\\project\\DBG_Automation\\img\\daily\\checkInClose.PNG"
imgWeaponsIcon = "C:\\project\\DBG_Automation\\img\\daily\\weapons_icon.PNG"

#Restart Image Paths
imgCloseApp = "C:\\project\\DBG_Automation\\img\\others\\app_close.PNG"
imgAppIcon = "C:\\project\\DBG_Automation\\img\\others\\app_icon.PNG"
imgAppTab = "C:\\project\\DBG_Automation\\img\\others\\app_tab.PNG"
imgHomeTab = "C:\\project\\DBG_Automation\\img\\others\\home_tab.PNG"
imgWelcomePrompt = "C:\\project\\DBG_Automation\\img\\others\\welcome_prompt.PNG"
imgWelcomeText = "C:\\project\\DBG_Automation\\img\\others\\welcome_text.PNG"


####################################################################################################################
#file interaction functions#
####################################################################################################################

def load_file(file_path):
    with open(file_path, 'r') as my_data_file:
        dict = json.load(my_data_file)
        return dict

def save_dailyCompletions(key, value):
    dailyCompletions[key] = value
    with open(jsonDailyCompletions, 'w') as json_file:
        json.dump(dailyCompletions, json_file)

def save_questList(key, value):
    questList[key] = value
    with open(jsonQuestList, 'w') as json_file:
        json.dump(questList, json_file)


####################################################################################################################
#Custom image recognition wrappers#
####################################################################################################################

def findImage(imagePath):
    time.sleep(0.5)
    pos = imagesearch(imagePath)
    if pos[0] != -1:
        return pos
    else:
        return False

def imgSearchClick(imagePath):
    time.sleep(0.5)
    pos = findImage(imagePath)
    print(pos)
    if pos != False:
        click_image(imagePath, pos, "left", 0, offset=0)
    else:
        return False
        
def imgSearchClickOffset(imagePath, offsetX, offsetY):
    time.sleep(0.5)
    pos = findImage(imagePath)
    print(pos)
    if pos != False:
        click_image_offset(imagePath, pos, offsetX, offsetY, "left", 0, offset=0)
    else:
        return False

def imgSearchClickOffsetAccurate(imagePath, offsetX, offsetY, index):
    time.sleep(0.5)
    pos = imagesearch(imagePath, index)
    print(pos)
    if pos != False:
        click_image_offset(imagePath, pos, offsetX, offsetY, "left", 0, offset=0)
    else:
        return False

####################################################################################################################
#Global Variable#
####################################################################################################################

skillproperties = {
    "index" : 0,
    "skillList" : [
        imgMultiElixir,
        imgMultiDmg,
        imgMultiCritDmg,
        imgMultiHeroDmg,
        imgMultiGold
    ]
}

####################################################################################################################
#Days Bygone Functions#
####################################################################################################################

def levelSkill(skillproperties):
    imgSearchClick(imgRewindMenu)
    index = skillproperties["index"]
    array = skillproperties["skillList"]
    skillImgPath = array[index]
    if 'scroll' in skillImgPath:
        pyautogui.moveTo(1234,267)
        pyautogui.dragTo(1234,365,0.5, button='left')
    imgSearchClickOffset(skillImgPath, 470, 25)
    imgSearchClick(imgOK)
    if index == len(array)-1:
        index = 0
    else:
        index += 1
    return index

def levelBattleSkill():
    while findImage(imgSkillDamage) == False:
        checkDailyPopUp()
    imgSearchClickOffset(imgSkillDamageIcon, 435, 34)

def rewind():
    print("rewind start")
    imgSearchClick(imgRewindMenu)
    while findImage(imgRewindLocked) == False:
        imgSearchClick(imgRewindSelect)
        imgSearchClick(imgRewindConfirm)

def watchAds(adButton, verifyImg):
    clickCount = 0
    imgSearchClick(adButton)
    while findImage(adButton) != False:
        imgSearchClick(adButton)
        clickCount += 1
        print("ClickCount", clickCount)
        time.sleep(5)
        if clickCount == 10:
            restartGame()
            return
    time.sleep(40)
    while findImage(verifyImg) == False:
        imgSearchClickOffset(imgBlueStacks, 1272, 73)
        time.sleep(1)
        clickCount += 1
        print("ClickCount: ", clickCount,"/10")
        if clickCount == 10:
            restartGame()
            raise Exception("Ad Failure - Game Restarted")

def restartGame():
    if findImage(imgMacroStop) != False:
        imgSearchClick(imgMacroStop)
    imgSearchClick(imgAppTab)
    imgSearchClick(imgCloseApp)
    time.sleep(2)
    imgSearchClick(imgHomeTab)
    imgSearchClick(imgAppIcon)
    while findImage(imgBattle) == False:
        imgSearchClick(imgWelcomeText)
####################################################################################################################
#Battle Functions#
####################################################################################################################

def campaign():
    imgSearchClick(imgBattle)
    imgSearchClick(imgCampaign)
    if findImage(imgGoldPrompt) != False:
        watchAds(imgAd2xGold, imgHealthBar)
    elif findImage(imgOK) != False:
        imgSearchClick(imgOK)
        time.sleep(2)
    time.sleep(1)
    macroStart(imgMacroNormal)
    while findImage(imgDefeat) == False:
        if imagesearch(imgWeaponCrate)[0] != -1:
            print("Weapons crate found")
            imgSearchClick(imgMacroStop)
            watchAds(img2xBattle, imgVictory)
            time.sleep(3)
            imgSearchClick(imgBattleNext)
            macroStart(imgMacroNormal)
    exitBattle(imgBack)
    #imagesearch_loop(imgDefeat, 1)

def dungeon(timeLimit):
    timer = 0
    imgSearchClick(imgBattle)
    imgSearchClick(imgDungeon)
    imgSearchClick(imgDungeonDown)
    imgSearchClick(imgDungeonEnter)
    watchAds(imgAd2xGold, imgHealthBar)
    macroStart(imgMacroSpell)
    #if (30 minutes or defeat shows up:)
    while findImage(imgSmallBack) == False and timer <= timeLimit:
        time.sleep(60)
        timer += 1
        print(findImage(imgSmallBack))
        print(timer)
    if findImage(imgSmallBack) != False:
        print("defeated!")
    elif timer >= timeLimit:
        imgSearchClick(imgMacroStop)
        imgSearchClick(imgDungeonPause)
        imgSearchClick(imgDungeonLeave)
        imgSearchClick(imgOK)
    exitBattle(imgSmallBack)

def expedition(imgPathDifficulty):
    imgSearchClick(imgBattle)
    imgSearchClick(imgExpedition)
    time.sleep(1)
    imgSearchClick(imgPathDifficulty)
    imgSearchClick(imgOK)
    macroStart(imgMacroSpell)
    imagesearch_loop(imgSmallBack, 1)
    exitBattle(imgSmallBack)

def exitBattle (exitButton):
    imgSearchClick(imgMacroStop)
    while findImage(imgBattle) == False:
        imgSearchClick(exitButton)
        time.sleep(3)
####################################################################################################################
#Daily Reward Functions#
####################################################################################################################

def getDailyFriendship():
    print("Daily Friendship:", dailyCompletions["dailyFriendship"])
    if dailyCompletions["dailyFriendship"] == False:
        imgSearchClick(imgSocialIcon)
        imgSearchClick(imgFriendsMenu)
        time.sleep(5)
        imgSearchClick(imgGiftAll)
        save_dailyCompletions("dailyFriendship",True)
        imgSearchClick(imgClose)

def getDailyGemAds():
    print("Daily Gem Ads:", dailyCompletions["dailyFreeGems"])
    if dailyCompletions["dailyFreeGems"] == False:
        imgSearchClick(imgStoreIcon)
        time.sleep(1)
        while imagesearch(imgAdRubyInvalid, 0.9)[0] == -1:
            watchAds(imgAdRuby, imgStoreRubies)
        time.sleep(2)
        save_dailyCompletions("dailyFreeGems",True)
        imgSearchClick(imgAdsClose)

def getDailySummon():
    print("Daily Summon:", dailyCompletions["dailyFreeSummon"])
    if dailyCompletions["dailyFreeSummon"] == False:
        imgSearchClick(imgCharacterIcon)
        imgSearchClick(imgCharacterTicket)
        imgSearchClick(imgClassicSummon)
        imgSearchClick(imgFreeSummon)
        imgSearchClickOffset(imgBlueStacks, 1272, 73)
        imgSearchClickOffset(imgBlueStacks, 1272, 73)
        imgSearchClick(imgSummonConfirm)
        while findImage(imgWeaponsIcon) == False:
            imgSearchClick(imgSummonClose)
        save_dailyCompletions("dailyFreeSummon", True)

def getDailyFriendshipShop():
    print("Daily Weekly Frienship Shop:", dailyCompletions["dailyFriendshipShop"])
    if dailyCompletions["dailyFriendshipShop"] == False:
        imgSearchClick(imgStoreIcon)
        imgSearchClick(imgStoreFriendship)
        print (imagesearch(imgStoreFriendshipValid, 0.9)[0])
        while imagesearch(imgStoreFriendshipValid, 0.9)[0] != -1:
            imgSearchClick(imgStoreFriendshipValid)
            imgSearchClick(imgStoreFriendshipConfirm)
            time.sleep(0.5)
        save_dailyCompletions("dailyFriendshipShop", True)
        imgSearchClick(imgStoreClose)

def dailyStatusReset():
    print(dailyCompletions)
    for k, v in dailyCompletions.items():
        save_dailyCompletions(k,False)
    for k, v in questList.items():
        save_questList(k,False)
    print(dailyCompletions)

def dailyCompletionEvaluate():
    flag = True
    for activity, status in dailyCompletions.items():
        print(activity, status)
        if activity != "dailyRewards" and status == False:
            flag = False
    
    save_dailyCompletions("dailyRewards", flag)

def checkDailyStatus():
    if dailyCompletions["dailyRewards"] == False:
        getDailyGemAds()
        getDailyFriendship()
        getDailySummon()
        getDailyFriendshipShop()
        getDailyQuests()
        dailyCompletionEvaluate()

def checkDailyPopUp():
    clickCount = 0
    if findImage(imgTitleCheckIn):
        dailyStatusReset()
        imgSearchClick(imgCheckInClaim)
        if imgCheckInClose == False and imgSummonConfirm == False:
            pyautogui.click(560,400)
            time.sleep(2)
        if findImage(imgSummonConfirm) != False:
            imgSearchClick(imgSummonConfirm)
        while findImage(imgSkillKnockBack) == False:
            imgSearchClick(imgCheckInClose)
            clickCount += 1
            if clickCount == 10:
                restartGame()
                raise Exception("Daily Reward Failure - Game Restarted")

####################################################################################################################
#Quests#
####################################################################################################################

def getDailyQuests():
    if questList["questChecked"] == False:
        imgSearchClick(imgQuestIcon)
        if findImage(imgQuestDungeon):
            save_questList("dungeon", True)
        if findImage(imgQuestSpells):
            save_questList("spells", True)
        if findImage(imgQuestExpedition):
            save_questList("expedition", True)
        save_questList("questChecked", True)
    if dailyCompletions["dailyQuests"] != True: 
        imgSearchClick(imgQuestIcon)
        time.sleep(1)
        pyautogui.moveTo(1017, 419)
        pyautogui.dragTo(1017,438,0.5, button='left')
        while imagesearch(imgQuestClaimx5, 0.9)[0] != -1:
            imgSearchClick(imgQuestClaimx5)
        if imagesearch(imgQuestClaimx15, 0.9)[0] != -1:
            imgSearchClick(imgQuestClaimx15)
            save_dailyCompletions("dailyQuests", True)
        imgSearchClick(imgQuestClose)
        print("getDailyQuest End")

def additionalQuestBattles():
    if dailyCompletions["dailyQuests"] == False:
        if questList["dungeon"] == True:
            dungeon(30)
        if questList["expedition"] or questList["spells"] == True:
            expedition(imgExpeditionHard)

####################################################################################################################
#Reset and Validations#
####################################################################################################################

def returntoMenu():
    print("Return to Menu")

def macroStart(imgPath):
    print(imgPath)
    pyautogui.hotkey('ctrl', 'shiftleft', '7')
    imgSearchClickOffset(imgPath,457,4)

####################################################################################################################
#Main Program Loop#
####################################################################################################################

#set up variables
x = 0
#Load json states
dailyCompletions = load_file(jsonDailyCompletions)
questList = load_file(jsonQuestList)

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
        print("An issue has occured, game loop restarted")

#checkDailyStatus()
#getDailyQuests()
# Traceback (most recent call last):  
#   File "c:/project/PY_AUTO/test.py", line 492, in <module>
#     rewind()
#   File "c:/project/PY_AUTO/test.py", line 241, in rewind
#     imgSearchClick(imgRewindSelect) 
#   File "c:/project/PY_AUTO/test.py", line 159, in imgSearchClick        
#     pos = findImage(imagePath)      
#   File "c:/project/PY_AUTO/test.py", line 150, in findImage
#     time.sleep(0.5)
# KeyboardInterrupt
# PS C:\project>     po


#Bugs: Stuck on Ad loop in menu
#Bugs: Stuck on Summoning Screen after daily refresh
#make sure questChecked is only toggled when quest screen is verified