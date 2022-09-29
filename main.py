from ast import While
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
        title = "**Drink water gajadu ram. NOW.**",
        message = "Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
        app_icon = r"waterglass.png",
        timeout=18)
        time.sleep(60*60)


