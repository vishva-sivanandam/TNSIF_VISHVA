import cv2
import pyautogui as pg
import os
page = "0"

def cp():
    global page

    try:
        screenshot = pg.screenshot()
    except:
        return
    screenshot.save('pages\screenshot.png')
    main_image = cv2.imread('pages\screenshot.png')
    sub_images_folder = "pages"

    match_found = False
    threshold = 0.8 

    for filename in os.listdir(sub_images_folder):
        if filename.lower().endswith(('.png')):
            sub_image_path = os.path.join(sub_images_folder, filename)
            sub_image = cv2.imread(sub_image_path)

            if sub_image is not None:
                result = cv2.matchTemplate(main_image, sub_image, cv2.TM_CCOEFF_NORMED)
                max_val = cv2.minMaxLoc(result)[1]

                if max_val >= threshold:
                    match_found = True
                    break

    if match_found:
        pagei = sub_image_path.find("pages") + 6
        page = sub_image_path[pagei:-4]
        page = page
        return page
    else:
        return "0"
    
