import enum
# Using enum class create enumerations

class quest(enum.Enum):
    icon = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_icon.PNG"
    claim = "C:\\project\\DBG_Automation\\img\\daily\\quests\\questClaim.PNG"
    quest_dungeon = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_dungeon.PNG"
    quest_spells =  "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_spells.PNG"
    quest_expedition = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_expedition.PNG"
    quest_claim_x5 = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_claim_x5.PNG"
    quest_claim_x15 = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_claim_x15.PNG"
    quest_scroll_down = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_scroll_down.PNG"
    close_quest = "C:\\project\\DBG_Automation\\img\\daily\\quests\\quest_close.PNG"

class image(enum.Enum):
    #Rewind Image Paths
    rewind_menu = "C:\\project\\DBG_Automation\\img\\rewind\\rewind.png"
    rewind_menu_active = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_active.png"
    rewind_select = "C:\\project\\DBG_Automation\\img\\rewind\\elixir_icon.png"
    rewind_confirm = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_confirm.png"
    ok_button = "C:\\project\\DBG_Automation\\img\\rewind\\ok.png"
    rewind_locked = "C:\\project\\DBG_Automation\\img\\rewind\\rewind_error4.PNG"
    stat_icon = "C:\\project\\DBG_Automation\\img\\rewind\\Stat.png"

    #Macro Image Paths
    normal_macro = "C:\\project\\DBG_Automation\\img\\macro\\battle_normal.PNG"
    spell_macro = "C:\\project\\DBG_Automation\\img\\macro\\battle_spell.PNG"

    #Campaign Image Paths
    battle_button = "C:\\project\\DBG_Automation\\img\\battle\\battle.PNG"
    campaign_button = "C:\\project\\DBG_Automation\\img\\battle\\campaign.PNG"
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

    #Dungeon Image Paths
    dungeon = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon.PNG"
    dungeon_down = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_down.PNG"
    dungeon_enter = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_enter.PNG"
    dungeon_leave = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_leave.PNG"
    dungeon_pause = "C:\\project\\DBG_Automation\\img\\battle\\dungeon\\dungeon_pause.PNG"

    #Expedition Image Paths
    expedition = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition.PNG"
    expedition_hard = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hard.PNG"
    expedition_hell = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_hell.PNG"
    small_back = "C:\\project\\DBG_Automation\\img\\battle\\expedition\\expedition_back.PNG"

    #Ads Image Paths
    ad_ruby = "C:\\project\\DBG_Automation\\img\\ads\\adRuby.PNG"
    ad_ruby_invalid = "C:\\project\\DBG_Automation\\img\\ads\\adRubyInvalid.PNG"
    ad_2x_gold = "C:\\project\\DBG_Automation\\img\\ads\\ad2xGold.PNG"
    bluestacks_logo = "C:\\project\\DBG_Automation\\img\\ads\\bs_logo.PNG"
    store_rubies = "C:\\project\\DBG_Automation\\img\\ads\\storeRubies.PNG"
    ads_close = "C:\\project\\DBG_Automation\\img\\ads\\close.PNG"

    #Menu Image Paths
    menu_skills = "C:\\project\\DBG_Automation\\img\\screen_check\\menuSkills.PNG"
    menu_spells = "C:\\project\\DBG_Automation\\img\\screen_check\\menuSpells.PNG"
    menu_stats = "C:\\project\\DBG_Automation\\img\\screen_check\\menuStats.PNG"
    menu_weapons = "C:\\project\\DBG_Automation\\img\\screen_check\\menuWeapons.PNG"
    #imgHeroesSkills = "C:\\project\\DBG_Automation\\img\\screen_check\\heroesSkills.PNG"

    #Skill Image Paths
    skill_multi_elixir = "C:\\project\\DBG_Automation\\img\\rewind\\elixir_mastery.PNG"
    skill_add_dmg = "C:\\project\\DBG_Automation\\img\\skills\\hidden_strength.PNG"
    skill_multi_dmg = "C:\\project\\DBG_Automation\\img\\skills\\untapped_power.PNG"
    skill_multi_mob_dmg = "C:\\project\\DBG_Automation\\img\\skills\\mob_slayer.PNG"
    skill_multi_boss_dmg = "C:\\project\\DBG_Automation\\img\\skills\\boss_slayer.PNG"
    skill_add_crit_dmg = "C:\\project\\DBG_Automation\\img\\skills\\explosive_strength_scroll.PNG"
    skill_multi_crit_dmg = "C:\\project\\DBG_Automation\\img\\skills\\beautiful_disaster_scroll.PNG"
    skill_multi_hero_dmg = "C:\\project\\DBG_Automation\\img\\skills\\inspire_scroll.PNG"
    skill_multi_gold = "C:\\project\\DBG_Automation\\img\\skills\\hard_labour_scroll.PNG"

    #Friendship Image Paths
    social_icon = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\social_icon.PNG"
    friends_menu = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\friends.PNG"
    friends_gift_all = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\gift_all.PNG"
    close = "C:\\project\\DBG_Automation\\img\\daily\\friendship\\close.PNG"

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

    #Daily Image Paths
    title_check_in = "C:\\project\\DBG_Automation\\img\\daily\\titleCheckIn.PNG"
    check_in_claim = "C:\\project\\DBG_Automation\\img\\daily\\checkInClaim.PNG"
    check_in_close = "C:\\project\\DBG_Automation\\img\\daily\\checkInClose.PNG"
    weapons_icon = "C:\\project\\DBG_Automation\\img\\daily\\weapons_icon.PNG"

    #Restart Image Paths
    close_app = "C:\\project\\DBG_Automation\\img\\others\\app_close.PNG"
    app_icon = "C:\\project\\DBG_Automation\\img\\others\\app_icon.PNG"
    app_tab = "C:\\project\\DBG_Automation\\img\\others\\app_tab.PNG"
    home_tab = "C:\\project\\DBG_Automation\\img\\others\\home_tab.PNG"
    welcome_prompt = "C:\\project\\DBG_Automation\\img\\others\\welcome_prompt.PNG"
    welcome_text = "C:\\project\\DBG_Automation\\img\\others\\welcome_text.PNG"


    # printing all enum members using loop
# print ("The enum members are : ")
# for weekday in (Days):
#    print(weekday)


    #filePaths
    #jsonDailyCompletions = "C:\\project\\DBG_Automation\\dailyCompletions.json"
# https://www.geeksforgeeks.org/enum-in-python/