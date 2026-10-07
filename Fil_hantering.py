# Fil hantering 
# Version 2 
#-----------------------------------------------------------
import time


fil_namn = "uppgifter.txt"

'''Funkar'''

def finns_redan_id_uppgift():
     finns_redan_id = set()

     try:
          with open(fil_namn, "r", encoding="utf-8") as f:
               for rad in f:
                    if rad.startswith("ID Nr: "):
                         finns_redan_id.add(rad.split(":",1)[1].strip())
     except FileNotFoundError:
          pass # För att filen inte finns , finns det inga sparade ID:n

     return finns_redan_id
#---------------------------------------------------------------------------     



'''Funkar '''
def skapa_uppgift(): 
    print("----Skapa Uppgift----")
    uppgift_id = input("ID Nr för Uppgiften? ").strip()
    uppgift = input("Namnet på Uppgiften? ").strip()
    beskrivning = input("Mer anteckningar för uppgiften? ").strip()
    status = input("Vad för rank är uppgiften? Hög; Medel Prioritet eller Låg Prioritet ? ").upper()

    while True:

        try:

            if uppgift_id == "":
                print("Felaktig inmatning")
                go_back_id = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny").upper()
                if go_back_id == "C":
                    return skapa_uppgift()
                    
                elif go_back_id == "M":
                    exit()

                else:
                    print("Fel inmatning, försök igen")
                    return skapa_uppgift()
                    
            elif uppgift_id in finns_redan_id_uppgift():
                print()
                print(f"ID Nr: {uppgift_id} finns redan, försök igen")
                print()
                return skapa_uppgift()
                
            else:
                with open(fil_namn, 'a',encoding="utf-8") as f:
                    uppgift_id_input = f.write(f"-------------------------\nID Nr: {uppgift_id}\n")
                    
        
        except FileNotFoundError:
            print(f"Filen {fil_namn} finns inte.")
            time.sleep(2)
            exit()                

        try:
            if uppgift == "":
                print("Felaktig inmatning")
                go_back_uppgift = input("Välj C för att forsätta , Välj M för att gå tillbaka till Meny: ").upper()
                if go_back_uppgift == "C":
                    return skapa_uppgift()
                        
                elif go_back_id == "M":
                            exit()

                else:
                    print("Fel inmatning, försök igen.")
                    return skapa_uppgift()
            else:
                with open(fil_namn, 'a',encoding="utf-8") as f:
                    uppgift_input = f.write(f"Uppgift: {uppgift}\n")
                    

        except FileNotFoundError:
            print(f"Filen {fil_namn} finns inte, försök igen")
            time.sleep(2)
            exit()


        try:
            if beskrivning == "":
                    print("Beskrivningen kan inte vara blank")
                    val_av_beskrivning =input("Tryck C för att fortsätta. Tryck M för att gå tillbaka till Menyn: ").upper()

                    if val_av_beskrivning == "C":
                        return skapa_uppgift()
                                                    
                    elif val_av_beskrivning == "M":
                        exit()   
                        
                    else:
                        print("Fel inmatning,förrsök igen")
                        val_av_beskrivning =input("Tryck C för att fortsätta. Tryck M för att gå tillbaka till Menyn: ").upper()                     
                            
            else:        
                with open(fil_namn, 'a',encoding="utf-8") as f:
                    beskrivning_input = f.write(f"Beskrivning: {beskrivning}\n")
                    

        except FileNotFoundError:
            print(f"Filen {fil_namn} finns inte, försök igen")
            time.sleep(2)
            exit()

                
            

        try:
            if status == "":
                        print("Status kan inte vara blank")
                        val_av_status =input("Tryck C för att fortsätta. Tryck M för att gå tillbaka till Menyn: ").upper()
                        if val_av_status == "C":
                                return skapa_uppgift()
                                                            
                        elif val_av_status == "M":
                                exit()    
            
                        else:
                                print("Fel inmatning, försök igen")
                                val_av_staus =input("Tryck C för att fortsätta. Tryck M för att gå tillbaka till Menyn: ").upper() 
            
            elif status == "HÖG" or status == "MEDEL" or status == "LÅG":        
                with open(fil_namn, 'a',encoding="utf-8") as f:
                    status_input = f.write(f"Status: {status}\n")
                    return False
            else:
                print()
                print("Status måste vara Hög, Medel eller Låg, försök igen")
                print()
                return skapa_uppgift()
            

                
        except FileNotFoundError:
            print("Filen finns inte")


                 
#skapa_uppgift()
#--------------------------------------------------------------------

''' Funkar '''


def andra_av_uppgift():
    print("-----Ändra Uppgift-----------")
    id_som_ska_andras = input("Vilken uppgift vill du ändra ? ")

    with open(fil_namn, "r", encoding="utf-8") as andraUppgift:
        rader = andraUppgift.readlines()

    hittad = False

    for i in range(len(rader)):
        if rader[i].strip() == "ID Nr: " + id_som_ska_andras:
            hittad = True

            ny_uppgift = input("Ny Uppgift: ")
            ny_beskriving = input("Ny beskrivning: ")
            ny_status = input("Ny status: ")

            rader[i + 1] = "Uppgift: " + ny_uppgift + "\n"
            rader[i + 2] = "Beskrivinig: " + ny_beskriving  + "\n"
            rader[i + 3] = "Status: " + ny_status + "\n"
            break
    try:
        if hittad:
            with open(fil_namn, 'w', encoding="utf-8") as rad:
                rad.writelines(rader)
            print("Uppgiften har ändrats. ")
        else:
            print("Det finns ingen uppgift med det ID:t.")
    except FileNotFoundError:
         print("Filen finns inte.")

#andra_av_uppgift()

#---------------------------------------------------------------------------------

'''Funkar'''
def ta_bort_uppgift():
    print("----Ta bort Uppgift----")
    id_att_ta_bort = input("Vilken är uppgifts-ID vill du ta bort?:  ").strip()

    with open (fil_namn, "r", encoding="utf-8") as fil:
        rader = fil.readlines()

    nya_rader = []
    borttagen = False
    i = 0

    while i < len(rader):
        if rader[i].startswith("ID Nr:"):
            sparat_id = rader[i].strip().replace("ID Nr:", "").strip()

            if sparat_id == id_att_ta_bort:
                i += 4
                borttagen = True
                continue

        nya_rader.append(rader[i])
        i += 1
    with open(fil_namn, "w", encoding="utf-8") as fil:
        fil.writelines(nya_rader)
    if borttagen:
        print(f"Uppgift {id_att_ta_bort} är borttagen.")
    else:
        print(f"Hittade ingen uppgift med ID {id_att_ta_bort}.")
        
#ta_bort_uppgift()    
#----------------------------------------------------------------
'''Funkar'''
def se_hela_uppgift_listan():
    print("-----Se Alla Uppgifter-----")
    with open(fil_namn, "r", encoding="utf-8") as v_l:
        visa_listan = v_l.read()
        print(visa_listan)

#se_hela_uppgift_listan()
#-----------------------------------------------------------------
   
''' Funkar '''
def ta_bort_hela_uppgift_listan():
    print("----Ta Bort Hela Uppgift Listan----")
    tom_lista_av_uppgifter = ""
    with open(fil_namn, "w", encoding="utf-8") as f:
        ta_bort_alla_uppgifter = f.write(tom_lista_av_uppgifter)
        print()
        print("---Hela listan är nu Borttagen---")
        print()

#ta_bort_hela_uppgift_listan()
#----------------------------------------------------------------



