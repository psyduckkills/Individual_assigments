# MAIN 
# Importera resten av modulerna för att de ska funka. 

import time
import Fil_hantering 
from Fil_hantering import skapa_uppgift ,andra_av_uppgift,se_hela_uppgift_listan, ta_bort_hela_uppgift_listan, ta_bort_uppgift,finns_redan_id_uppgift


def meny():
    print("----TaskMaster-------")
    print("1. Skapa Uppgifter")
    print("2. Ändra Uppgifter")
    print("3. Se Hela Listan ")
    print("4. Ta bort Hela Listan")
    print("5. Ta bort en Uppgift")
    print("6. Exit ")
    print("---------------------")
    

def meny_logik():
    meny()
    val = input("Vad är ditt val?: ")
    match val:
        case "1":
            skapa_uppgift()
            return meny_logik()
        
        case "2":
            andra_av_uppgift()
            return meny_logik()

        case "3":
            se_hela_uppgift_listan()
            return meny_logik() 

        case "4":
            ta_bort_hela_uppgift_listan()
            return meny_logik()

        case "5":
            ta_bort_uppgift()
            return meny_logik()

        case "6":
            print("Logging out....")
            time.sleep(2)
            exit()

        case _:
            print(f"Ditt val {val} är ej gilltig, försök igen")
            return meny_logik()
            


meny_logik()


# Logik för att se hela listan 
