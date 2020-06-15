import enum
# Using enum class create enumerations

class quest(enum.Enum):
    icon = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_icon.PNG"
    claim = "C:\\project\\PY_AUTO\\img\\daily\\quests\\questClaim.PNG"
    quest_dungeon = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_dungeon.PNG"
    quest_spells =  "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_spells.PNG"
    quest_expedition = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_expedition.PNG"
    quest_claim_x5 = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_claim_x5.PNG"
    quest_claim_x15 = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_claim_x15.PNG"
    quest_scroll_down = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_scroll_down.PNG"
    close_quest = "C:\\project\\PY_AUTO\\img\\daily\\quests\\quest_close.PNG"

class image(enum.Enum):
    #Rewind Image Paths
    rewind_menu = "C:\\project\\PY_AUTO\\img\\rewind\\rewind.png"
    rewind_menu_active = "C:\\project\\PY_AUTO\\img\\rewind\\rewind_active.png"
    rewind_select = "C:\\project\\PY_AUTO\\img\\rewind\\elixir_icon.png"
    rewind_confirm = "C:\\project\\PY_AUTO\\img\\rewind\\rewind_confirm.png"
    ok_button = "C:\\project\\PY_AUTO\\img\\rewind\\ok.png"
    rewind_locked = "C:\\project\\PY_AUTO\\img\\rewind\\rewind_error4.PNG"
    stat_icon = "C:\\project\\PY_AUTO\\img\\rewind\\Stat.png"

    #Macro Image Paths
    normal_macro = "C:\\project\\PY_AUTO\\img\\macro\\battle_normal.PNG"
    spell_macro = "C:\\project\\PY_AUTO\\img\\macro\\battle_spell.PNG"

    #Campaign Image Paths
    battle_button = "C:\\project\\PY_AUTO\\img\\battle\\battle.PNG"
    campaign_button = "C:\\project\\PY_AUTO\\img\\battle\\campaign.PNG"
    gold_prompt = "C:\\project\\PY_AUTO\\img\\battle\\x2_gold_prompt.PNG"
    health_bar = "C:\\project\\PY_AUTO\\img\\battle\\health.PNG"
    start_macro = "C:\\project\\PY_AUTO\\img\\battle\\macro_play.PNG"
    stop_macro = "C:\\project\\PY_AUTO\\img\\battle\\macro_stop.PNG"
    defeat_prompt = "C:\\project\\PY_AUTO\\img\\battle\\defeat.PNG"
    back_button = "C:\\project\\PY_AUTO\\img\\battle\\back.PNG"
    skill_damage = "C:\\project\\PY_AUTO\\img\\battle\\skillDamage.PNG"
    skill_damage_icon = "C:\\project\\PY_AUTO\\img\\battle\\skillDamageIcon.PNG"
    weapon_crate = "C:\\project\\PY_AUTO\\img\\battle\\weapons_crate.PNG"
    x2_Battle = "C:\\project\\PY_AUTO\\img\\battle\\x2_battle.PNG"
    battle_next = "C:\\project\\PY_AUTO\\img\\battle\\battle_next.PNG"
    victory_prompt = "C:\\project\\PY_AUTO\\img\\battle\\victory.PNG"
    skill_knockback_icon = "C:\\project\\PY_AUTO\\img\\battle\\skill_knock_back.PNG"

    #Dungeon Image Paths
    dungeon = "C:\\project\\PY_AUTO\\img\\battle\\dungeon\\dungeon.PNG"
    dungeon_down = "C:\\project\\PY_AUTO\\img\\battle\\dungeon\\dungeon_down.PNG"
    dungeon_enter = "C:\\project\\PY_AUTO\\img\\battle\\dungeon\\dungeon_enter.PNG"
    dungeon_leave = "C:\\project\\PY_AUTO\\img\\battle\\dungeon\\dungeon_leave.PNG"
    dungeon_pause = "C:\\project\\PY_AUTO\\img\\battle\\dungeon\\dungeon_pause.PNG"

    #Expedition Image Paths
    expedition = "C:\\project\\PY_AUTO\\img\\battle\\expedition\\expedition.PNG"
    expedition_hard = "C:\\project\\PY_AUTO\\img\\battle\\expedition\\expedition_hard.PNG"
    expedition_hell = "C:\\project\\PY_AUTO\\img\\battle\\expedition\\expedition_hell.PNG"
    small_back = "C:\\project\\PY_AUTO\\img\\battle\\expedition\\expedition_back.PNG"

    #Ads Image Paths
    ad_ruby = "C:\\project\\PY_AUTO\\img\\ads\\adRuby.PNG"
    ad_ruby_invalid = "C:\\project\\PY_AUTO\\img\\ads\\adRubyInvalid.PNG"
    ad_2x_gold = "C:\\project\\PY_AUTO\\img\\ads\\ad2xGold.PNG"
    bluestacks_logo = "C:\\project\\PY_AUTO\\img\\ads\\bs_logo.PNG"
    store_rubies = "C:\\project\\PY_AUTO\\img\\ads\\storeRubies.PNG"
    ads_close = "C:\\project\\PY_AUTO\\img\\ads\\close.PNG"

    #Menu Image Paths
    menu_skills = "C:\\project\\PY_AUTO\\img\\screen_check\\menuSkills.PNG"
    menu_spells = "C:\\project\\PY_AUTO\\img\\screen_check\\menuSpells.PNG"
    menu_stats = "C:\\project\\PY_AUTO\\img\\screen_check\\menuStats.PNG"
    menu_weapons = "C:\\project\\PY_AUTO\\img\\screen_check\\menuWeapons.PNG"
    #imgHeroesSkills = "C:\\project\\PY_AUTO\\img\\screen_check\\heroesSkills.PNG"

    #Skill Image Paths
    skill_multi_elixir = "C:\\project\\PY_AUTO\\img\\rewind\\elixir_mastery.PNG"
    skill_add_dmg = "C:\\project\\PY_AUTO\\img\\skills\\hidden_strength.PNG"
    skill_multi_dmg = "C:\\project\\PY_AUTO\\img\\skills\\untapped_power.PNG"
    skill_multi_mob_dmg = "C:\\project\\PY_AUTO\\img\\skills\\mob_slayer.PNG"
    skill_multi_boss_dmg = "C:\\project\\PY_AUTO\\img\\skills\\boss_slayer.PNG"
    skill_add_crit_dmg = "C:\\project\\PY_AUTO\\img\\skills\\explosive_strength_scroll.PNG"
    skill_multi_crit_dmg = "C:\\project\\PY_AUTO\\img\\skills\\beautiful_disaster_scroll.PNG"
    skill_multi_hero_dmg = "C:\\project\\PY_AUTO\\img\\skills\\inspire_scroll.PNG"
    skill_multi_gold = "C:\\project\\PY_AUTO\\img\\skills\\hard_labour_scroll.PNG"

    #Friendship Image Paths
    social_icon = "C:\\project\\PY_AUTO\\img\\daily\\friendship\\social_icon.PNG"
    friends_menu = "C:\\project\\PY_AUTO\\img\\daily\\friendship\\friends.PNG"
    friends_gift_all = "C:\\project\\PY_AUTO\\img\\daily\\friendship\\gift_all.PNG"
    close = "C:\\project\\PY_AUTO\\img\\daily\\friendship\\close.PNG"

    #Store Image Paths
    store_icon = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_icon.PNG"
    store_close = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_close.PNG"
    store_friendship = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship.PNG"
    store_friendship_valid = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_valid.PNG"
    store_friendship_invalid = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_invalid.PNG"
    store_friendship_confirm = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_confirm.PNG"

    #Character Image Paths
    character_icon = "C:\\project\\PY_AUTO\\img\\daily\\character_icon.PNG"
    character_ticket = "C:\\project\\PY_AUTO\\img\\daily\\character_ticket.PNG"
    classic_summon = "C:\\project\\PY_AUTO\\img\\daily\\classic_summon.PNG"
    free_summon = "C:\\project\\PY_AUTO\\img\\daily\\free_summon.PNG"
    summon_confirm = "C:\\project\\PY_AUTO\\img\\daily\\summon_confirm.PNG"
    summon_close = "C:\\project\\PY_AUTO\\img\\daily\\summon_close.PNG"

    #Daily Image Paths
    title_check_in = "C:\\project\\PY_AUTO\\img\\daily\\titleCheckIn.PNG"
    check_in_claim = "C:\\project\\PY_AUTO\\img\\daily\\checkInClaim.PNG"
    check_in_close = "C:\\project\\PY_AUTO\\img\\daily\\checkInClose.PNG"
    weapons_icon = "C:\\project\\PY_AUTO\\img\\daily\\weapons_icon.PNG"

    #Restart Image Paths
    close_app = "C:\\project\\PY_AUTO\\img\\others\\app_close.PNG"
    app_icon = "C:\\project\\PY_AUTO\\img\\others\\app_icon.PNG"
    app_tab = "C:\\project\\PY_AUTO\\img\\others\\app_tab.PNG"
    home_tab = "C:\\project\\PY_AUTO\\img\\others\\home_tab.PNG"
    welcome_prompt = "C:\\project\\PY_AUTO\\img\\others\\welcome_prompt.PNG"
    welcome_text = "C:\\project\\PY_AUTO\\img\\others\\welcome_text.PNG"


    # printing all enum members using loop
# print ("The enum members are : ")
# for weekday in (Days):
#    print(weekday)


    #filePaths
    #jsonDailyCompletions = "C:\\project\\PY_AUTO\\dailyCompletions.json"
# https://www.geeksforgeeks.org/enum-in-python/