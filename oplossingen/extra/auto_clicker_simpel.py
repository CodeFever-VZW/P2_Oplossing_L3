import pyautogui
import time


def auto_clicker():
    print("Python Auto Clicker")
    print("-------------------")
    gewenst_aantal_clicks = int(input("Geef het gewenste aantal clicks in: "))
    print("De auto-clicker zal binnen 3 seconden starten.  Beweeg je muis naar de gewenste positie.")
    time.sleep(3)

    try:
        muis_positie = pyautogui.position()  # Get current mouse position
        aantal_uitgevoerde_clicks = 0

        for _ in range(gewenst_aantal_clicks):
            pyautogui.mouseDown(muis_positie)
            pyautogui.mouseUp()
            print(f"Geklikt op positie {muis_positie}, aantal clicks: {aantal_uitgevoerde_clicks}")
            aantal_uitgevoerde_clicks += 1

        print("De auto-clicker heeft alle clicks uitgevoerd.")
    except:
        print("De auto-clicker is gestopt wegens een fout.")


auto_clicker()