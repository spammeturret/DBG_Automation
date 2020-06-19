import enum
import time
import wrappers as event
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

class image(enum.Enum):
    store_icon = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_icon.PNG"
    store_close = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_close.PNG"
    store_friendship = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_valid.PNG"
    store_friendship_valid = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_valid.PNG"
    store_friendship_invalid = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_invalid.PNG"
    store_friendship_confirm = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_confirm.PNG"
    store_friendship_menu = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_menu_friendship.PNG"
    store_expedition_menu = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_menu_expedition.PNG"
    store_expedition = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_expedition.PNG"
    store_rubies = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_rubies.PNG"
    store_weapon = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_weapon.PNG"
    store_hero = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_hero.PNG"
    store_purchase_confirm = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_purchase_confirm.PNG"

class Purchase:
    def __init__(self, purchase_list):
        self.purchase_list = purchase_list
    
    def make_purchase(self, image_purchase_button, purchase_item):
        if "rubies" in purchase_item:        
            coordinates = [297, 202, 1008, 311]
        elif "weapon" in purchase_item:
            coordinates = [297, 327, 1008, 433]
        elif "hero" in purchase_item:
            coordinates = [297, 448, 1008, 557]
        else:
            return "Error, invalid purchase item"
        
        print("coordinates:",coordinates[0])
        while event.find_image_area(image_purchase_button, coordinates[0], coordinates[1], coordinates[2], coordinates[3]) == True:
            print("correct")
            event.search_click_offset(purchase_item, 471, 28)
            time.sleep(0.5)
            event.search_click(image.store_purchase_confirm.value)


    def spend_friendship(self):
        #Input: None
        #Output: updated purchase dictionary
        print("Daily Weekly Frienship Shop:", self.purchase_list["status"]["daily_friendship_shop"])
        if self.purchase_list["status"]["daily_friendship_shop"] == False:
            event.search_click(image.store_icon.value)
            event.search_click(image.store_friendship_menu.value)
            time.sleep(0.5)
            self.make_purchase(image.store_friendship.value, image.store_rubies.value)
            self.make_purchase(image.store_friendship.value, image.store_weapon.value)
            self.make_purchase(image.store_friendship.value, image.store_hero.value)
            self.purchase_list["status"]["daily_friendship_shop"] = True
            event.search_click(image.store_close.value)
        return self.purchase_list

    def spend_fossils(self):
        print("Daily Weekly Fossil Shop:", self.purchase_list["status"]["daily_expedition_shop"])
        if self.purchase_list["status"]["daily_expedition_shop"] == False:
            event.search_click(image.store_icon.value)
            event.search_click(image.store_expedition_menu.value)
            time.sleep(0.5)
            self.make_purchase(image.store_expedition.value, image.store_rubies.value)
            self.make_purchase(image.store_expedition.value, image.store_weapon.value)
            self.make_purchase(image.store_expedition.value, image.store_hero.value)
            self.purchase_list["status"]["daily_expedition_shop"] = True
            event.search_click(image.store_close.value)
        return self.purchase_list


    def is_completed(self):
        """
        Input: none
        Output: (Boolean) true or false
        """
        outcome = True
        for value in self.purchase_list["status"].values():
            if value == False:
                outcome = False
        print('purchase is_completed: ', outcome)
        return outcome

    def reset_all(self):
        new_purchases = {}
        for key in self.purchase_list["status"]:
            new_purchases[key] = False
        return new_purchases