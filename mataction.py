from time import time
import pyautogui
import time
import glob
from PIL import Image

secs_between_keys = 0.5
span = 2


def setdata():
    time.sleep(span)
    pyautogui.typewrite("clear")
    pyautogui.typewrite(["enter"])
    time.sleep(span)
    pyautogui.typewrite("reference")
    pyautogui.typewrite(["enter"])
    time.sleep(span)
    pyautogui.typewrite("currentverspan")
    pyautogui.typewrite(["enter"])
    time.sleep(span)
    pyautogui.typewrite("roi")
    pyautogui.typewrite(["enter"])


def matlab(i):
    time.sleep(span)
    pyautogui.typewrite(
        f"ans{i} = ncorr")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)

    time.sleep(span)

    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    pyautogui.typewrite(
        f"ans{i}.set_ref(data_ref{i})")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    pyautogui.typewrite(
        f"ans{i}.set_cur(data_cur{i})")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    pyautogui.typewrite(
        f"ans{i}.set_roi_ref(data_roi{i})")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)

    time.sleep(span)
    l, t, w, h = pyautogui.locateOnScreen('./finish.png')
    pyautogui.click(l+5, t+5)


#i > 2
def matlab2(i):
    time.sleep(span)
    pyautogui.typewrite(
        f"handles_ncorr.set_ref(data_ref{i})")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    pyautogui.typewrite(
        f"handles_ncorr.set_cur(data_cur{i})")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    pyautogui.typewrite(
        f"handles_ncorr.set_roi_ref(data_roi{i})")
    pyautogui.typewrite(["enter"], interval=secs_between_keys)
    time.sleep(span)
    l, t, w, h = pyautogui.locateOnScreen('./finish.png')
    pyautogui.click(l+5, t+5)


def photshop(i):
    time.sleep(span)
    pyautogui.press("f12")
    time.sleep(span)
    pyautogui.hotkey("option", "command", "shift", "w")
    time.sleep(span)
    pyautogui.hotkey("shift", "tab")
    pyautogui.press("enter")
    time.sleep(span)
    pyautogui.press("delete")
    pyautogui.typewrite(f"Roi_0{i}", interval=secs_between_keys)
    pyautogui.press("enter")
    time.sleep(span)
    pyautogui.hotkey("ctrl", "tab")


# for i in range(1, 6):
#    matlab(i)

for i in range(1, 6):
    photshop(i)
