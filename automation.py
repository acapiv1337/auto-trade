from pywinauto import Application
import pyautogui
import time
import cv2
import numpy as np

def start_app(moomoo_path):
    app = Application().start(moomoo_path)
    return app

def login(window, email, password):
    window.set_focus()
    pyautogui.tripleClick(1133, 434)  # Adjust based on screen
    pyautogui.write(email)
    pyautogui.tripleClick(1133, 484)
    pyautogui.write(password)
    pyautogui.click(1133, 560)
    time.sleep(10)
    login_success(window)
    return window

def login_success(window):
    bool_find = find_template(window, 'template_matching/moomoo - watchlist.png')
    if bool_find:
        print('Login successful')
    else:
        print('Login failed')

def find_template(window, template_path_img, coeff=0.9):
    window.set_focus()
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(template_path_img, 0)
    w, h = template.shape[::-1]
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= coeff:
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return [center_x, center_y]
    else:
        print('No match found')
        return False


def unlock_trade(window, pin):
    coor_x, coor_y = find_template(window, 'template_matching/unlock trade.png')
    pyautogui.click(coor_x, coor_y)
    pyautogui.write(pin)
    pyautogui.press('enter')
