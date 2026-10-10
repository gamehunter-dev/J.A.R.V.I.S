import pyautogui
import subprocess
import webbrowser
import time

# Safety: move the mouse to the top-left corner to stop PyAutoGUI
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3


def open_website(url):
    """Open a website in the default browser."""
    if not url.startswith(("https://", "http://")):
        return "Please provide a valid HTTP or HTTPS URL."

    webbrowser.open(url)
    return f"Opening {url}"


def type_text(text):
    """Type text into the currently focused application."""
    pyautogui.write(text, interval=0.03)
    return "Text typed."


def press_key(key):
    """Press a key such as enter, tab, or escape."""
    allowed_keys = {
        "enter", "tab", "escape", "space",
        "backspace", "delete", "up", "down",
        "left", "right"
    }

    if key.lower() not in allowed_keys:
        return "That key is not allowed by this function."

    pyautogui.press(key.lower())
    return f"Pressed {key}"


def click_mouse(x=None, y=None):
    """Click at a position or at the current mouse location."""
    if x is None or y is None:
        pyautogui.click()
    else:
        pyautogui.click(x=int(x), y=int(y))

    return "Mouse clicked."


def take_screenshot():
    """Save a screenshot to the project folder."""
    filename = f"jarvis_screenshot_{int(time.time())}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return f"Screenshot saved as {filename}"


def get_mouse_position():
    """Return the current mouse coordinates."""
    position = pyautogui.position()
    return f"Mouse position: X={position.x}, Y={position.y}"

