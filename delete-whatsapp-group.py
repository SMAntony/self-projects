import pyautogui as pag
import time

def click_grp_mem(x, y, button):
    time.sleep(1)
    pag.click(x, y, button = button)

def remove_mem():
    time.sleep(1)
    pag.click(1485, 832)

def confirm_remove_mem(x, y):
    time.sleep(1)
    pag.click(x, y)


def search(): # Use this function to search and find groups using the keyword
    pag.click(377, 293) # Position of the search bar
    keyword = "set" # Set the required keyword
    for i in range(len(keyword)): # in case keyword is already entered, delete the current keyword
        pag.hotkey("backspace")
    pag.typewrite(keyword) # Enter the keyword in the search box

def selecting_whatsapp(): # To select the required tab or windows
    pag.click(85, 23)

def select_searched_result():
    time.sleep(1)
    pag.click(297, 466)

def select_grp_settings():
    time.sleep(1)
    pag.click(1376, 190)

def scroll_to_mem():
    pag.moveTo(1793, 341)
    for i in range(5):
        time.sleep(1)
        pag.scroll(-250)

def leaving():
    time.sleep(1)
    pag.click(1395, 203)

def repeating_func():
    selecting_whatsapp()
    search()
    select_searched_result()
    select_grp_settings()
    scroll_to_mem()


if __name__ == "__main__":
    path = input("Remove or Delete:")    
    if path == "R":
        loop = int(input("Enter to stop:"))
        pag.hotkey("alt", "tab")
        time.sleep(1)
        repeating_func()
        for i in range(loop):
            click_grp_mem(1633, 939, "RIGHT")
            remove_mem()
            confirm_remove_mem(1128, 662)
        leaving()
    elif path == "D":   
        pag.hotkey("alt", "tab")
        repeating_func()
        pos = (0, 0, 0) # the positional arugments that needs to change when the loop is run
        for i in range(2):
            click_grp_mem(1633 - pos[0], 939 - pos[1], "LEFT")
            confirm_remove_mem(1128, 662 + pos[2])
            pos[0] += 98
            pos[1] += 115
            pos[2] += 41
        leaving()
    else:
        print(None)
