import pyautogui, time, exceptions
from python_imagesearch.imagesearch import imagesearch, imagesearcharea, click_image, click_image_offset
from datetime import datetime

def find_image(image_path, print_suppression = False):
    '''
    Description: Checks if an image is on-screen.
    Input: imagePath - File Path of image to check
    Output: True if found, false if not found.
    '''
    pos = imagesearch(image_path)
    
    if pos[0] != -1:
        if print_suppression == False:
            txt_var = "Image Found:" + get_img_name(image_path)
            log("INFO", "wrapper.find_image", txt_var)
        return True
    else:
        if print_suppression == False:
            txt_var = "Image Not Found - " + get_img_name(image_path)
            log("WARNING", "wrapper.find_image", txt_var)
        return False

def find_image_area(image_path, x1, y1, x2, y2, print_suppression = False):
    pos = imagesearcharea(image_path, x1, y1, x2, y2)
    
    if pos[0] != -1:
        if print_suppression == False:
            txt_var = "Image Found:" + get_img_name(image_path)
            log("INFO", "wrapper.find_image", txt_var)
        return True
    else:
        if print_suppression == False:
            txt_var = "Image Not Found - " + get_img_name(image_path)
            log("WARNING", "wrapper.find_image", txt_var)
        return False

def search_click(image_path, wait_time = 0.5):
    time.sleep(wait_time)
    pos = imagesearch(image_path)
    if pos[0] != -1:
        txt_var = 'Image Clicked - ' + get_img_name(image_path)
        log("INFO", "wrapper.search_click", txt_var)
        click_image(image_path, pos, "left", 0, offset=0)
    else:
        txt_var = 'Cant find Image to Click - ' + get_img_name(image_path)
        log("WARNING", "wrapper.search_click", txt_var)
        return False
        
def search_click_offset(image_path, offsetX, offsetY, wait_time=0.5):
    time.sleep(wait_time)
    pos = imagesearch(image_path)
    print(pos)
    if pos[0] != -1:
        txt_var = 'Image Offset Clicked - ' + get_img_name(image_path)
        log("INFO", "wrapper.search_click_offset", txt_var)
        click_image_offset(image_path, pos, offsetX, offsetY, "left", 0, offset=0)
    else:
        txt_var = 'Image Not Found - ' + get_img_name(image_path)
        log("WARNING", "wrapper.search_click_offset", txt_var)
        return False

def click_button_validate(img_to_click, exception_class = exceptions.error, click_limit = 10):
    """Keep clicking button until it disappears"""
    click_count = 0
    while find_image(img_to_click) == True:
        txt_var = "Times clicked on "+get_img_name(img_to_click)+ ": "+ str(click_count) + "/"+ str(click_limit)
        search_click(img_to_click)
        log("INFO", "wrapper.click_button_validate", txt_var)
        click_count += 1
        time.sleep(5)
        if click_count == click_limit:
            txt_var = "Click count over the defined limit, throwing exception"
            log("ERROR", "wrapper.click_button_validate", txt_var)
            raise exception_class

def click_next_screen_validate(img_to_click, next_img_to_validate, exception_class = exceptions.error, click_limit = 10):
    """Keep clicking button until the next image appears"""
    click_count = 0
    while find_image(next_img_to_validate) == False:
        txt_var = "Times clicked on " + get_img_name(img_to_click) + ": " + str(click_count) + "/"+ str(click_limit)
        search_click(img_to_click)
        log("INFO", "wrapper.click_next_screen_validate", txt_var)
        time.sleep(1)
        click_count += 1
        print("Times clicked on ", get_img_name(img_to_click), ": ", str(click_count), "/", str(click_limit))
        if click_count == click_limit:
            txt_var = "Click count over the defined limit, throwing exception"
            log("ERROR", "wrapper.click_next_screen_validate", txt_var)
            raise exception_class

def click_next_screen_validate_offset(img_to_click, offset_x, offset_y, next_img_to_validate, exception_class = exceptions.error, click_limit = 10):
    click_count = 0
    while find_image(next_img_to_validate) == False:
        search_click_offset(img_to_click, offset_x, offset_y)
        time.sleep(1)
        click_count += 1
        print("Times clicked on ", get_img_name(img_to_click), ": ", str(click_count), "/", str(click_limit))
        if click_count == click_limit:
            raise exception_class

def get_img_name(img_path):
    if '\\' in img_path:
        return img_path.split('\\')[-1]
    else:
        return "<<IMAGE_NAME_NOT_FOUND>>"

def log(msg_type, function_name, message):
    timestamp_str = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
    print(timestamp_str,"-","[",msg_type,"] [",function_name,"]:", message)