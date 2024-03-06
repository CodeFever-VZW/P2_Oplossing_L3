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
        hoeveelheid_energie = 0
        energie_per_click = 1
        volgende_aankoopprijs = 20
        winkel_coordinaten = (1189, -1051)
        earth_clicker_coordinaten = (750, -1465)
        sluit_coordinaten = (1224, -1711)

        for _ in range(gewenst_aantal_clicks):
            if hoeveelheid_energie >= volgende_aankoopprijs:
                koop_earth_clicker(winkel_coordinaten, earth_clicker_coordinaten, sluit_coordinaten)
                hoeveelheid_energie -= volgende_aankoopprijs
                volgende_aankoopprijs *= 3
                energie_per_click *= 2
                print(f'UPGRADE: vanaf heden genereren we {energie_per_click} per click.  Verheugt u allen!')

            click_coordinaat(muis_positie)
            print(f"Geklikt op positie {muis_positie}, aantal clicks: {aantal_uitgevoerde_clicks}")
            aantal_uitgevoerde_clicks += 1
            hoeveelheid_energie += energie_per_click

        print("De auto-clicker heeft alle clicks uitgevoerd.")
    except:
        print("De auto-clicker is gestopt wegens een fout.")


def koop_earth_clicker(winkel_coordinaten, earth_clicker_coordinaten, sluit_coordinaten):
    click_coordinaat(winkel_coordinaten)
    click_coordinaat(earth_clicker_coordinaten)
    click_coordinaat(sluit_coordinaten)


def click_coordinaat(coordinaat):
    pyautogui.mouseDown(coordinaat)
    time.sleep(0.2)
    pyautogui.mouseUp()


auto_clicker()