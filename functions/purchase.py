import enum
import time
import wrappers as event
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, region_grabber, click_image, click_image_offset, imagesearch_numLoop, imagesearch_loop

class image(enum.Enum):
    store_icon = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_icon.PNG"
    store_close = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_close.PNG"
    store_friendship = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship.PNG"
    store_friendship_valid = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_valid.PNG"
    store_friendship_invalid = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_invalid.PNG"
    store_friendship_confirm = "C:\\project\\PY_AUTO\\img\\daily\\store\\store_friendship_confirm.PNG"

class Purchase:
    def __init__(self, purchase_list):
        self.purchase_list = purchase_list


    def spend_friendship(self):
        #Input: None
        #Output: updated purchase dictionary
        print("Daily Weekly Frienship Shop:", self.purchase_list["status"]["daily_friendship_shop"])
        if self.purchase_list["status"]["daily_friendship_shop"] == False:
            event.search_click(image.store_icon.value)
            event.search_click(image.store_friendship.value)
            while imagesearch(image.store_friendship_valid.value, 0.9)[0] != -1:
                event.search_click(image.store_friendship_valid.value)
                event.search_click(image.store_friendship_confirm.value)
                time.sleep(0.5)
            self.purchase_list["status"]["daily_friendship_shop"] = True
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