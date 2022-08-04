## ____  ____  _      _     _____ ____  _____  _    
##/   _\/  _ \/ \  /|/ \ |\/  __//  __\/__ __\/ \ /\
##|  /  | / \|| |\ ||| | //|  \  |  \/|  / \  | | ||
##|  \__| \_/|| | \||| \// |  /_ |    /  | |  | \_/|
##\____/\____/\_/  \|\__/  \____\\_/\_\  \_/  \____/
##                                                
## Written In Python
## By Tristan And Triman    
## Aka PhotonMastr
## twitch.tv/photonmastr
## github.com/photonmastr
## twitter.com/photonmastr
## github.com/lildemonn

import os
import time

def mass():
    print("1. US Tons\n2. Kilograms\n3. Grams\n4. Milligrams\n5. Pounds\n6. Ounces")
    massoption = input("Select a number for the corresponding units 1-6: ")
    if int(massoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tons. Ok. Now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Kilograms\n2. Grams\n3. Milligrams\n4. Pounds\n5. Ounces")
        tonstowhat = input("Select a number for the corresponding units 1-5: ")
        if int(tonstowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilograms. Ok, input how many Tons to Kilograms.")
            tonstokilograms = input("")
            answertonstokilograms = float(tonstokilograms) * 907.2
            print(f"your answer is: {answertonstokilograms}")
            input("")
        elif int(tonstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Grams. Ok, input how many Tons to Grams")
            tonstograms = input("")
            answertonstograms = float(tonstograms) * 907200
            print(f"your answer is: {answertonstograms}")
            input("")
        elif int(tonstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Milligrams. Ok, input how many Tons to Milligrams")
            tonstomilligrams = input("")
            answertonstomilligrams = float(tonstomilligrams) * 970200000
            print(f"your answer is: {answertonstomilligrams}")
            input("")
        elif int(tonstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pounds. Ok, input how many Tons to Pounds")
            tonstopounds = input("")
            answertonstopounds = float(tonstopounds) * 2000
            print(f"your answer is: {answertonstopounds}")
            input("")
        elif int(tonstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ounces. Ok, input how many Tons to Ounces")
            tonstoounces = input("")
            answertonstoounces = float(tonstoounces) * 32000
            print(f"your answer is: {answertonstoounces}")
            input("")
    elif int(massoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Kilograms. Ok,  Now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("1. Tons\n2. Grams\n3. Milligrams\n4. Pounds\n5. Ounces")
        kilogramstowhat = input("Select a number for the corresponding units 1-5")
        if int(kilogramstowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Tons. Ok, input how many Kilograms to Tons")
                kilogramstotons = input("")
                answerkilogramstotons = float(kilogramstotons) / 907.2
                print(f"your answer is: {answerkilogramstotons}")
                input("")
        elif int(kilogramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Grams. Ok, input how many Kilograms to Grams")
                kilogramstograms = input("")
                answerkilogramstograms = float(kilogramstograms) * 1000
                print(f"your answer is: {answerkilogramstograms}")
                input("")
        elif int(kilogramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Milligrams. Ok, input how many Kilograms to Milligrams")
                kilogramstomilligrams = input("")
                answerkilogramstomilligrams = float(kilogramstomilligrams) * 1000000
                print(f"your answer is: {answerkilogramstomilligrams}")
                input("")
        elif int(kilogramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Pounds. Ok, input how many Kilograms to Pounds")
                kilogramstopounds = input("")
                answerkilogramstopounds = float(kilogramstopounds) * 2.205
                print(f"your answer is: {answerkilogramstopounds}")
                input("")
        elif int(kilogramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Ounces. Ok, input how many Kilograms to Ounces")
                kilogramstoounces = input("")
                answerkilogramstoounces = float(kilogramstoounces) * 35.274
                print(f"your answer is: {answerkilogramstoounces}")
                input("")
    elif int(massoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Grams. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Tons\n2. Kilograms\n3. Milligrams\n4. Pounds\n5. Ounces")
        gramstowhat = input("Select a number for the corresponding units 1-5")
        if int(gramstowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Tons. Ok, input how many Grams to Tons")
                gramstotons = input("")
                answergramstotons = float(gramstotons) / 907200
                print(f"your answer is: {answergramstotons}")
                input("")
        elif int(gramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Grams to Kilograms")
                gramstokilograms = input("")
                answergramstokilograms = float(gramstokilograms) / 1000
                print(f"your answer is: {answergramstokilograms}")
                input("")
        elif int(gramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Grams to Milligrams")
                gramstomilligrams = input("")
                answergramstomilligrams = float(gramstomilligrams) * 1000
                print(f"your answer is: {answergramstomilligrams}")
                input("")
        elif int(gramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many Grams to Pounds")
                gramstopounds = input("")
                answergramstopounds = float(gramstopounds) / 453.6
                print(f"your answer is: {answergramstopounds}")
                input("")
        elif int(gramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many Grams to Ounces")
                gramstoounces = input("")
                answergramstoounces = float(gramstoounces) / 28.35
                print(f"your answer is: {answergramstoounces}")
                input("")
    elif int(massoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("milligrams. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Tons\n2. Kilograms\n3. Grams\n4. Pounds\n5. Ounces")
        milligramstowhat = input("Select a number for the corresponding units 1-5")
        if int(milligramstowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Tons. Ok, input how many Milligrams to Tons")
                milligramstotons = input("")
                answermilligramstotons = float(milligramstotons) / 907200000
                print(f"your answer is: {answermilligramstotons}")
                input("")
        elif int(milligramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Milligrams to Kilograms")
                milligramstokilograms = input("")
                answermilligramstokilograms = float(milligramstokilograms) / 1000000
                print(f"your answer is: {answermilligramstokilograms}")
                input("")
        elif int(milligramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Milligrams to Grams")
                milligramstograms = input("")
                answermilligramstograms = float(milligramstograms) / 1000
                print(f"your answer is: {answermilligramstograms}")
                input("")
        elif int(milligramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many milligrams to Pounds")
                milligramstopounds = input("")
                answermilligramstopounds = float(milligramstopounds) / 453600
                print(f"your answer is: {answermilligramstopounds}")
                input("")
        elif int(milligramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many milligrams to Ounces")
                milligramstoounces = input("")
                answermilligramstoounces = float(milligramstoounces) / 28350
                print(f"your answer is: {answermilligramstoounces}")
                input("")
    elif int(massoption) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Pounds. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Tons\n2. Kilograms\n3. Grams\n4. Milligrams\n5. Ounces")
        poundstowhat = input("Select a number for the corresponding units 1-5")
        if int(poundstowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Tons. Ok, input how many Pounds to Tons")
                poundstotons = input("")
                answerpoundstotons = float(poundstotons) / 2000
                print(f"your answer is: {answerpoundstotons}")
                input("")
        elif int(poundstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Pounds to Kilograms")
                poundstokilograms = input("")
                answerpoundstokilograms = float(poundstokilograms) / 2.205
                print(f"your answer is: {answerpoundstokilograms}")
                input("")
        elif int(poundstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Pounds to Grams")
                poundstograms = input("")
                answerpoundstograms = float(poundstograms) * 453.6
                print(f"your answer is: {answerpoundstograms}")
                input("")
        elif int(poundstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Pounds to Milligrams")
                poundstomilligrams = input("")
                answerpoundstomilligrams = float(poundstomilligrams) * 453600
                print(f"your answer is: {answerpoundstomilligrams}")
                input("")
        elif int(poundstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many Pounds to Ounces")
                poundstoounces = input("")
                answerpoundstoounces = float(poundstoounces) * 16
                print(f"your answer is: {answerpoundstoounces}") 
                input("")
    elif int(massoption) == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ounces. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Tons\n2. Kilograms\n3. Grams\n4. Milligrams\n5. Pounds")
        ouncestowhat = input("Select a number for the corresponding units 1-5")
        if int(ouncestowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Tons. Ok, input how many Ounces to Tons")
                ouncestotons = input("")
                answerouncestotons = float(ouncestotons) / 32000
                print(f"your answer is {answerouncestotons}")
                input("")
        elif int(ouncestowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Ounces to Kilograms")
                ouncestokilograms = input("")
                answerouncestokilograms = float(ouncestokilograms) / 35.274
                print(f"your answer is {answerouncestokilograms}")
                input("")
        elif int(ouncestowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Grams. Ok, input how many Ounces to Grams")
                ouncestograms = input("")
                answerouncestograms = float(ouncestograms) * 28.35
                print(f"your answer is: {answerouncestograms}")
                input("")
        elif int(ouncestowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Ounces to Milligrams")
                ouncestomilligrams = input("")
                answerouncestomilligrams = float(ouncestomilligrams) * 28350
                print(f"your answer is: {answerouncestomilligrams}")
                input("")
        elif int(ouncestowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many Ounces to Pounds")
                ouncestopounds = input("")
                answerouncestopounds = float(ouncestopounds) / 16
                print(f"your answer is: {answerouncestopounds}")
                input("")

def storage():
    print("1. Byte\n2. Kilobyte\n3. Gigabyte\n4. Megabyte\n5. Terabyte")
    storageoption = input("Select a number for the corresponding units 1-5: ")
    if int(storageoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bytes. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Kilobyte\n2. Megabyte\n3. Gigabyte\n4. Terabyte")
        bytestowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(bytestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, input how many Bytes to Kilobytes")
            bytestokilobytes = input("")
            answerbytestokilobytes = float(bytestokilobytes) / 1000 
            print(f"your answer is: {answerbytestokilobytes}")
            input("")
        elif int(bytestowhat) == 2: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, input how many Bytes to Megabytes")
            bytestomegabytes = input("")
            answerbytestomegabytes = float(bytestomegabytes) / 1000000
            print(f"your answer is: {answerbytestomegabytes}")
            input("")
        elif int(bytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabyte. Ok, input how many Bytes to Gigabytes")
            bytestogigabytes = input("")
            answerbytestogigabytes = float(bytestogigabytes) / 1000000000 
            print(f"your answer is: {answerbytestogigabytes}")
            input("")
        elif int(bytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, input how many Bytes to Terabytes")
            bytestoterabytes = input("")
            answerbytestoterabytes = float(bytestoterabytes) / 1000000000000
            print(f"your answer is: {answerbytestoterabytes}")
            input("")
    elif int(storageoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Kilobytes. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Byte\n2. Megabyte\n3. Gigabyte\n4. Terabyte")
        kilobytestowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(kilobytestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bytes. Ok, input how many Kilobytes to Bytes")
            kilobytestobytes = input("")
            answerkilobytestobytes = float(kilobytestobytes) * 1000 
            print(f"your answer is: {answerkilobytestobytes}")
            input("")
        elif int(kilobytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, input how many Kilobytes to Megabytes")
            kilobytestomegabytes = input("")
            answerkilobytestomegabytes = float(kilobytestomegabytes) / 1000
            print(f"your answer is: {answerkilobytestomegabytes}")
            input("")
        elif int(kilobytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, input how many Kilobytes to Gigabytes")
            kilobytestogigabytes = input("")
            answerkilobytestogigabytes = float(kilobytestogigabytes) / 1000000
            print(f"your answer is: {answerkilobytestogigabytes}")
            input("")
        elif int(kilobytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabytes. Ok, input how many Kilobytes to Terabytes")
            kilobytestoterabytes = input("")
            answerkilobytestoterabytes = float(kilobytestoterabytes) / 1000000000
            print(f"your answer is: {answerkilobytestoterabytes}")
            input("")
    if int(storageoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Megabytes. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Byte\n2. Kilobyte\n3. Megabyte\n4. Terabyte")
        gigabytestowhat = input("Seloooohect a number 1-4 for the corresponding unit: ")
        if int(gigabytestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bytes. Ok, now input how many Gigabytes to Bytes?")
            gigabytestobytes = input("")
            answergigabytestobytes = float(gigabytestobytes) * 1000000000
            print(f"your answer is: {answergigabytestobytes}")
            input("")
        elif int(gigabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Gigabytes to Kilobytes")
            gigabytestokilobytes = input("")
            answergigabytestokilobytes = float(gigabytestokilobytes) * 1000000
            print(f"your answer is: {answergigabytestokilobytes}")
            input("")
        elif int(gigabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, now input how many Gigabytes to Megabytes")
            gigabytestomegabytes = input("")
            answergigabytestomegabytes = float(gigabytestomegabytes) * 1000
            print(f"your answer is: {answergigabytestomegabytes}")
            input("")
        elif int(gigabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, now input how many Gigabytes to Terabytes")
            gigabytestoterabytes = input("")
            answergigabytestoterabytes = float(gigabytestoterabytes) / 1000
            print(f"your answer is: {answergigabytestoterabytes}")
            input("")
    elif int(storageoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Megabytes. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Byte\n2. Kilobyte\n3. Gigabyte\n4. Terabyte")
        megabytestowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(megabytestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bytes. Ok, now input how many Megabytes to Bytes")
            megabytestobytes = input("")
            answermegabytestobytes = float(megabytestobytes) * 1000000
            print(f"your answer is: {answermegabytestobytes}")
            input("")
        elif int(megabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Megabytes to Kilobytes")
            megabytestokilobytes = input("")
            answermegabytestokilobytes = float(megabytestokilobytes) * 1000
            print(f"your answer is: {answermegabytestokilobytes}")
            input("")
        elif int(megabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, now input how many Megabytes to Gigabytes")
            megabytestogigabytes = input("")
            answermegabytestogigabytes = float(megabytestogigabytes) / 1000
            print(f"your answer is: {answermegabytestogigabytes}")
            input("")
        elif int(megabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, now input how many Megabytes to Terabytes")
            megabytestoterabytes = input("")
            answermegabytestoterabytes = float(megabytestoterabytes) / 1000000
            print(f"your answer is: {answermegabytestoterabytes}")
            input("")
    elif int(storageoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terabytes. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Byte\n2. Kilobyte\n3. Gigabyte\n4. Megabyte")
        terabytestowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(terabytestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bytes. Ok, now input how many Terabytes to Bytes")
            terabytestobytes = input("")
            answerterabytestobytes = float(terabytestobytes) * 1000000000000
            print(f"your answer is: {answerterabytestobytes}")
            input("")
        elif int(terabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Terabytes to Kilobytes")
            terabytestokilobytes = input("")
            answerterabytestokilobytes = float(terabytestokilobytes) * 1000000000
            print(f"your answer is: {answerterabytestokilobytes}")
            input("")
        elif int(terabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, now input how many Terabytes to Gigabytes")
            terabytestogigabytes = input("")
            answerterabytestogigabytes = float(terabytestogigabytes) * 1000 
            print(f"your answer is: {answerterabytestogigabytes}")
            input("")
        elif int(terabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, now input how many Terabytes to Megabytes.")
            terabytestomegabytes = input("")
            answerterabytestomegabytes = float(terabytestomegabytes) * 1000000
            print(f"your answer is: {answerterabytestomegabytes}")
            input("")


def length():
    print("1. Foot\n2. Metre\n3. Kilometre\n4. Centimetre\n5. Millimetre\n6. Yard\n7. Inch")
    lengthoption = input("Select a number for the corresponding units 1-7: ")
    if int(lengthoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Feet. Ok, Now what do you want to convert that to?") 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Metre\n2. Kilometre\n3. Centimetre\n4. Millimetre\n5. Yard\n6. Inch")
        feettowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(feettowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Feet to Metres")
            feettometres = input("")
            answerfeettometres = float(feettometres) / 3.281
            print(f"your answer is: {answerfeettometres}")
            input("")
        elif int(feettowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Feet to Kilometres")
            feettokilometres = input("")
            answerfeettokilometres = float(feettokilometres) / 3281
            print(f"your answer is: {answerfeettokilometres}")
            input("")
        elif int(feettowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Feet to Centimetres")
            feettocentimetres = input("")
            answerfeettocentimetres = float(feettocentimetres) * 30.48
            print(f"your answer is: "  + str(answerfeettocentimetres))
            input("")
        elif int(feettowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Feet to Millimetres")
            feettomillimetres = input("")
            answerfeettomillimetres = float(feettomillimetres) * 304.8
            print(f"your answer is: {answerfeettomillimetres}")
            input("")
        elif int(feettowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Feet to Yards")
            feettoyard = input("")
            answerfeettoyard = float(feettoyard) / 3
            print(f"your answer is: {answerfeettoyard}")
            input("")
        elif int(feettowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Feet to Inches")
            feettoinches = input("")
            answerfeettoinches = float(feettoinches) * 12
            print(f"your answer is: {answerfeettoinches}")
            input("")
    elif int(lengthoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Metres. Ok, Now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Kilometre\n3. Centimetre\n4. Millimetre\n5. Yard\n6. Inch")
        metrestowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(metrestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Metres to Feet")
            metrestofeet = input("")
            answermetrestofeet = float(metrestofeet) * 3.281
            print(f"your answer is: {answermetrestofeet}")
            input("")
        elif int(metrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Metres to Kilometres")
            metrestokilometres = input("")
            answermetrestokilometres = float(metrestokilometres) / 1000
            print(f"your answer is: {answermetrestokilometres}")
            input("")
        elif int(metrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Metres to Centimetres")
            metrestocentimetres = input("")
            answermetrestocentimetres = float(metrestocentimetres) * 100
            print(f"your answer is: {answermetrestocentimetres}")
            input("")
        elif int(metrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Metres to Millimetres")
            metrestomillimetres = input("")
            answermetrestomillimetres = float(metrestomillimetres) * 1000
            print(f"your answer is: {answermetrestomillimetres}")
            input("")
        elif int(metrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Metres to Yards")
            metrestoyards = input("")
            answermetrestoyards = float(metrestoyards) * 1.094
            print(f"your answer is: {answermetrestoyards}")
            input("")
        elif int(metrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Metres to Inches")
            metrestoinches = input("")
            answermetrestoinches = float(metrestoinches) * 39.37
            print(f"your answer is: {answermetrestoinches}")
            input("")
    elif int(lengthoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Kilometres. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Metre\n3. Centimetre\n4. Millimetre\n5. Yard\n6. Inch")
        kilometrestowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(kilometrestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Kilometres to Feet")
            kilometrestofeet = input("")
            answerkilometrestofeet = float(kilometrestofeet) * 3281
            print(f"your answer is: {answerkilometrestofeet}")
            input("")
        elif int(kilometrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Kilometres to Metres")
            kilometrestometres = input("")
            answerkilometrestometres = float(kilometrestometres) * 1000 
            print(f"your answer is: {answerkilometrestometres}")
            input("")
        elif int(kilometrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Kilometres to Centimetres")
            kilometrestocentimetres = input("")
            answerkilometrestocentimetres = float(kilometrestocentimetres) * 100000 
            print(f"your answer is: {answerkilometrestocentimetres}")
            input("")
        elif int(kilometrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Kilometres to Millimetres")
            kilometrestocentimetres = input("")
            answerkilometrestomillimetres = float(kilometrestocentimetres) * 1000000
            print(f"your answer is: {answerkilometrestomillimetres}")
            input("")
        elif int(kilometrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Kilometres to Yards")
            kilometrestoyards = input("")
            answerkilometrestoyards = float(kilometrestoyards) * 1094
            print(f"your answer is: {answerkilometrestoyards}")
            input("")
        elif int(kilometrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Kilometres to Inches")
            kilometrestoinches = input("")
            answerkilometrestoinches = float(kilometrestoinches) * 39370 
            print(f"your answer is: {answerkilometrestoinches}")
            input("")
    elif int(lengthoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Centimetres. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Metre\n3. Kilometre\n4. Millimetre\n5. Yard\n6. Inch")
        centimetrestowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(centimetrestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Centimetres to Feet")
            centimetrestofeet = input("")
            answercentimetrestofeet = float(centimetrestofeet) / 30.48
            print(f"your answer is: {answercentimetrestofeet}")
            input("")
        elif int(centimetrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Centimetres to Metres")
            centimetrestometres = input("")
            answercentimetrestometres = float(centimetrestometres) / 100
            print(f'your answer is: {answercentimetrestometres}')
            input("")
        elif int(centimetrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Centimetres to Kilometres")
            centimetrestokilometres = input("")
            answercentimetrestokilometres = float(centimetrestokilometres) / 1000000
            print(f"your answer is: {answercentimetrestokilometres}")
            input("")
        elif int(centimetrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Centimetres to Millimetres")
            centimetrestomillimetres = input("")
            answercentimetrestomillimetres = float(centimetrestomillimetres) * 10 
            print(f"your answer is: {answercentimetrestomillimetres}")
            input("")
        elif int(centimetrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok. Now input how many Centimetres to Yards")
            centimetrestoyards = input("")
            answercentimetrestoyards = float(centimetrestoyards) / 91.44
            print(f"your answer is: {answercentimetrestoyards}")
            input("")
        elif int(centimetrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Centimetres to Inches")
            centimetrestoinches = input("")
            answercentimetrestoinches = float(centimetrestoinches) / 2.54
            print(f"your answer is: {answercentimetrestoinches}")
            input("")
    elif int(lengthoption) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Millimetres. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Metre\n3. Kilometre\n4. Centimetre\n5. Yard\n6. Inch")
        millimetrestowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(millimetrestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Millimetres to Feet")
            millimetrestofeet = input("")
            answermillimetrestofeet = float(millimetrestofeet) / 304.8
            print(f"your answer is: {answermillimetrestofeet}")
            input("")
        elif int(millimetrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. OK, now input how many Millimetres to Metres")
            millimetrestometres = input("")
            answermillimetrestometres = float(millimetrestometres) / 1000
            print(f"your answer is: {answermillimetrestometres}")
            input("")
        elif int(millimetrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Millimetres to Kilometres")
            millimetrestokilometres = input("")
            answermillimetrestokilometres = float(millimetrestokilometres) / 1000000
            print(f"your answer is: {answermillimetrestokilometres}")
            input("")
        elif int(millimetrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Millimetres to Centimetres")
            millimetrestocentimetres = input("")
            answermillimetrestocentimetres = float(millimetrestocentimetres) / 10
            print(f"your answer is: {answermillimetrestocentimetres}")
            input("")
        elif int(millimetrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Millimetres to Yards")
            millimetrestoyards = input("")
            answermillimetrestoyards = float(millimetrestoyards) / 914.4
            print(f"your answer is: {answermillimetrestoyards}")
            input("")
        elif int(millimetrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Millimetres to Inches")
            millimetrestoinches = input("")
            answermillimetrestoinches = float(millimetrestoinches) / 25.4
            print(f"your answer is: {answermillimetrestoinches}")
            input("")
    elif int(lengthoption) == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Yards. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Metre\n3. Kilometre\n4. Centimetre\n5. Millimetres\n6. Inch")
        yardstowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(yardstowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Yards to Feet")
            yardstofeet = input("")
            answeryardstofeet = float(yardstofeet) * 3
            print(f"your answer is: {answeryardstofeet}")
            input("")
        elif int(yardstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Yards to Metres")
            yardstometres = input("")
            answeryardstometres = float(yardstometres) / 1.094
            print(f"your answer is: {answeryardstometres}")
            input("")
        elif int(yardstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Yards to Kilometres")
            yardstokilometres = input("")
            answeryardstokilometres = float(yardstokilometres) / 1094
            print(f"your answer is: {answeryardstokilometres}")
            input("")
        elif int(yardstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Yards to Centimetres")
            yardstocentimetres = input("")
            answeryardstocentimetres = float(yardstocentimetres) * 91.44
            print(f"your answer is: {answeryardstocentimetres}")
            input("")
        elif int(yardstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Yards to Millimetres")
            yardstomillimetres = input("")
            answeryardstomillimetres = float(yardstomillimetres) * 914.44
            print(f"your answer is: {answeryardstomillimetres}")
            input("")
        elif int(yardstowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Yards to Inches")
            yardstoinches = input("")
            answeryardstoinches = float(yardstoinches) * 36
            print(f"your answer is: {answeryardstoinches}")
            input("")
    elif int(lengthoption) == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Inches. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Metre\n3. Kilometre\n4. Centimetre\n5. Millimetres\n6. Yards")
        inchestowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(inchestowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Inches to Feet")
            inchestofeet = input("")
            answerinchestofeet = float(inchestofeet) / 12 
            print(f"your answer is: {answerinchestofeet}")
            input("")
        elif int(inchestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Inches to Metres")
            inchestometres = input("")
            answerinchestometres = float(inchestometres) / 39.37
            print(f"your answer is: {answerinchestometres}")
            input("")
        elif int(inchestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Inches to Kilometres")
            inchestokilometres = input("")
            answerinchestokilometres = float(inchestokilometres) / 39370
            print(f"your answer is: {answerinchestokilometres}")
            input("")
        elif int(inchestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Inches to Centimetres")
            inchestocentimetres = input("")
            answerinchestocentimetres = float(inchestocentimetres) * 2.54
            print(f"your answer is: {answerinchestocentimetres}")
            input("")
        elif int(inchestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Inches to Millimetres")
            inchestomillimetres = input("")
            answerinchestomillimetres = float(inchestomillimetres) * 25.4
            print(f"your answer is: {answerinchestomillimetres}")
            input("")
        elif int(inchestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Inches to Yards")
            inchestoyards = input("")
            answerinchestoyards = float(inchestoyards) / 36
            print(f"your answer is: {answerinchestoyards}")
            input("")

def speed():
    print("1. MPH\n2. KPH\n3. FPS(feet per second)\n4. MPS(metres per second)\n5. Knots")
    speedoption = input("Select a number for the corresponding units 1-5: ")
    if int(speedoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("MPH. Ok, Now what do you want to convert that to?") 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. KPH\n2. FPS(feet per second)\n3. MPS(metres per second)\n4. Knots")
        mphtowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(mphtowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many MPH to KPH")
            mphtokph = input("")
            answermphtokph = float(mphtokph) * 1.609
            print(f"your answer is: {answermphtokph}")
            input("")
        elif int(mphtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many MPH to FPS")
            mphtofps = input("")
            answermphtofps = float(mphtofps) * 1.467
            print(f"your answer is: {answermphtofps}")
            input("")
        elif int(mphtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many MPH to MPS")
            mphtomps = input("")
            answermphtomps = float(mphtomps) * 2.237
            print(f"your answer is: {answermphtomps}")
            input("")
        elif int(mphtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many MPH to Knots")
            mphtoknots = input("")
            answermphtoknots = float(mphtoknots) / 1.151
            print(f"your answer is: {answermphtoknots}")
            input("")
    elif int(speedoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("KPH. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. MPH\n2. FPS(feet per second)\n3. MPS(metres per second)\n4. Knots")
        kphtowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(kphtowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPH. Ok, now input how many KPH to MPH")
            kphtomph = input("")
            answerkphtomph = float(kphtomph) / 1.609
            print(f"your answer is: {answerkphtomph}")
            input("")
        elif int(kphtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many KPH to FPS")
            kphtofps = input("")
            answerkphtofps = float(kphtofps) / 1.097
            print(f"your answer is: {answerkphtofps}")
            input("")
        elif int(kphtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many KPH to MPS")
            kphtomps = input("")
            answerkphtomps = float(kphtomps) / 3.6 
            print(f"your answer is: {answerkphtomps}")
            input("")
        elif int(kphtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many KPH to Knots")
            kphtoknots = input("")
            answerkphtoknots = float(kphtoknots) / 1.852
            print(f"your answer is: {answerkphtoknots}")
            input("")
    elif int(speedoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("FPS. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. MPH\n2. KPH\n3. MPS(metres per second)\n4. Knots")
        fpstowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(fpstowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPH. Ok, now input how many FPS to MPH")
            fpstomph = input("")
            answerfpstomph = float(fpstomph) / 1.467
            print(f"your answer is: {answerfpstomph}")
            input("")
        elif int(fpstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many FPS to KPH")
            fpstokph = input("")
            answerfpstokph = float(fpstokph) / 1.097
            print(f"your answer is: {answerfpstokph}")
            input("")
        elif int(fpstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many FPS to MPS")
            fpstomps = input("")
            answerfpstomps = float(fpstomps) / 3.281 
            print(f"your answer is: {answerfpstomps}")
            input("")
        elif int(fpstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many FPS to Knots")
            fpstoknots = input("")
            answerfpstoknots = float(fpstoknots) / 1.688
            print(f"your answer is: {answerfpstoknots}")
            input("")
    elif int(speedoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("MPS. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. MPH\n2. KPH\n3. FPS(feet per second)\n4. Knots")
        mpstowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(mpstowhat) == 1: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPH. Ok, now input how many MPS to MPH")
            mpstomph = input("")
            answermpstomph = float(mpstomph) * 2.237
            print(f"your answer is {answermpstomph}")
            input("")
        elif int(mpstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many MPS to KPH")
            mpstokph = input("")
            answermpstokph = float(mpstokph)
            print(f"your answer is: {answermpstokph}")
            input("")
        elif int(mpstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many MPS to FPS")
            mpstofps = input("")
            answermpstofps = float(mpstofps) * 3.281
            print(f"your answer is: {answermpstofps}")
            input("")
        elif int(mpstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many MPS to Knots")
            mpstoknots = input("")
            answermpstoknots = float(mpstoknots) * 1.944
            print(f"your answer is: {answermpstoknots}")
            input("")
    elif int(speedoption) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Knots. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. MPH\n2. KPH\n3. FPS(feet per second)\n4. MPS")
        knotstowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(knotstowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPH. Ok, now input how many Knots to MPH")
            knotstomph = input("")
            answerknotstomph = float(knotstomph) * 1.151
            print(f"your answer is: {answerknotstomph}")
            input("")
        elif int(knotstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many Knots to KPH")
            knotstokph = input("")
            answerknotstokph = float(knotstokph) * 1.852
            print(f"your answer is: {answerknotstokph}")
            input("")
        elif int(knotstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many Knots to FPS")
            knotstofps = input("")
            answerknotstofps = float(knotstofps) * 1.688
            print(f"your answer is: {answerknotstofps}")
            input("")
        elif int(knotstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many Knots to MPS")
            knotstomps = input("")
            answerknotstomps = float(knotstomps) / 1.944
            print(f"your answer is: {answerknotstomps}")
            input("")

def temperature():  
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    tempoption = input("Select a number for the corresponding units 1-3: ")
    if int(tempoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Celsius. Ok, Now what do you want to convert that to?") 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Fahrenheit\n2. Kelvin")
        celsiustowhat = input("Select a number 1-2 for the corresponding unit: ")
        if int(celsiustowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fahrenheit. Ok, now input how many Celsius to Fahrenheit")
            celsiustofahrenheit = input("")
            answercelsiustofahrenheit = float(celsiustofahrenheit) * 1.8 + 32
            print(f"your answer is: {answercelsiustofahrenheit}")
            input("")
        elif int(celsiustowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kelvin. Ok, now input how many Celsius to Kelvin")
            celsiustokelvin = input("")
            answercelsiustokelvin = float(celsiustokelvin) + 273.15
            print(f"your answer is: {answercelsiustokelvin}")
            input("")
    elif int(tempoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fahrenheit. Ok, Now what do you want to convert that to?") 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Celsius\n2. Kelvin")
        fahrenheittowhat = input("Select a number 1-2 for the corresponding unit: ")
        if int(fahrenheittowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Celsius. Ok, now input how many Fahrenheit to Celsius")
            fahrenheittocelsius = input("")
            answerfahrenheittocelsius = float(fahrenheittocelsius) - 32 * 0.5556
            print(f"your answer is: {answerfahrenheittocelsius}")
            input("")
        elif int(fahrenheittowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kelvin. Ok, now input how many Fahrenheit to Kelvin")
            fahrenheittokelvin = input("")
            answerfahrenheittokelvin = float(fahrenheittokelvin) + 459.67 * 0.5556
            print(f"your answer is: {answerfahrenheittokelvin}")
            input("")
    elif int(tempoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Kelvin. Ok, Now what do you want to convert that to?") 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Celsius\n2. Fahrenheit")
        kelvintowhat = input("Select a number 1-2 for the corresponding unit: ")
        if int(kelvintowhat) == 1: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Celsius. Ok, now input how many Kelvin to Celsius")
            kelvintocelsius = input("")
            answerkelvintocelsius = float(kelvintocelsius) - 273.15
            print(f"your answer is: {answerkelvintocelsius}")
            input("")
        elif int(kelvintowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fahrenheit. Ok, now input how many Kelvin to Fahrenheit")
            kelvintofahrenheit = input("")
            answerkelvintofahrenheit = float(kelvintofahrenheit) - 273.15 * 1.8 + 32
            print(f"your answer is: {answerkelvintofahrenheit}")
            input("")

def frequency():
    print("1. Hertz\n2. Kilohertz\n3. Megahertz\n4. Gigahertz")
    freqoption = input("Select a number 1-4 for the corresponding unit")
    if int(freqoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hertz. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Kilohertz\n2. Megahertz\n3. Gigahertz")
        hertztowhat = input("Select a number 1-3 for the corresponding unit")
        if int(hertztowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilohertz. Ok, now input how many Hertz to Kilohertz")
            hertztokilohertz = input("")
            answerhertztokilohertz = float(hertztokilohertz) / 100
            print(f"your answer is: {answerhertztokilohertz}")
            input("")
        elif int(hertztowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megahertz. Ok, now input how many Hertz to Megahertz")
            hertztomegahertz = input("")
            answerhertztomegahertz = float(hertztomegahertz) / 1000000
            print(f"your answer is: {answerhertztomegahertz}")
        elif int(hertztowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigahertz. Ok, now input how many Hertz to Gigahertz")
            hertztogigahertz = input("")
            answerhertztogigahertz = float(hertztogigahertz) / 1000000000
            print(f"your answer is: {answerhertztogigahertz}")
    elif int(freqoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Kilohertz. Ok, now what do you want to convert that to?")
        print("1. Hertz\n2. Megahertz\n3. Gigahertz")
        kilohertztowhat = input("Select a number 1-3 for the corresponding unit")
        if int(kilohertztowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hertz. Ok, now input how many Kilohertz to Hertz")
            kilohertztohertz = input("")
            answerkilohertztohertz = float(kilohertztohertz) * 1000
            print(f"your answer is: {answerkilohertztohertz}")
        elif int(kilohertztowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megahertz. Ok, now input how many Kilohertz to Megahertz")
            kilohertztomegahertz = input("")
            answerkilohertztomegahertz = float(kilohertztomegahertz) / 1000
            print(f"your answer is: {answerkilohertztomegahertz}")
        elif int(kilohertztowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigahertz. Ok, now input how many Kilohertz to Gigahertz")
            kilohertztogigahertz = input("")
            answerkilohertztogigahertz = float(kilohertztogigahertz) / 1000000
            print(f"your answer is {answerkilohertztogigahertz}")
    elif int(freqoption) -- 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Megahertz. Ok, now what do you want to convert that to")
        gigahertztomegahertz = input("")
        answergigahertztomegahertz = float(gigahertztomegahertz) / 1000
        print(f"your answer is: {answergigahertztomegahertz}")
        input("")

def area():
    print("1. Square Kilometre\n2. Square Metre\n3. Square Mile\n4. Square Yard\n5. Square Foot\n6. Square Inch\n7. Hectare\n8. Acre")
    areaoption = input("Select a number 1-8 for the corresponding unit: ")
    if int(areaoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Square KM. Ok, now what do you want to convert that to?")
        print("1. Square Metre\n2. Square Mile\n3. Square Yard\n4. Square Foot\n5. Square Inch\n6. Hectare\n7. Acre")
        squarekmtowhat = input("Select a number 1-7 for the corresponding unit: ")
        if int(squarekmtowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M, Ok, now input how many Square KM to Square M")
            squarekmtosquarem = input("")
            answersquarekmtosquarem = float(squarekmtosquarem) * 1000000
            print(f"your answer is: {answersquarekmtosquarem}")
            input("")
        elif int(squarekmtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square MI. Ok, now input how many Square KM to Square MI")
            squarekmtosquaremi = input("")
            answersquarekmtosquaremi = float(squarekmtosquaremi) / 2.59
            print(f"your answer is: {answersquarekmtosquaremi}")
            input("")
        elif int(squarekmtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square KM to Square Yards")
            squarekmtosquareyards = input("")
            answersquarekmtosquareyards = float(squarekmtosquareyards) * 1196000
            print(f"your answer is: {answersquarekmtosquareyards}")
            input("")
        elif int(squarekmtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square KM to Square Feet")
            squarekmtosquarefeet = input("")
            answersquarekmtosquarefeet = float(squarekmtosquarefeet) * 10760000
            print(f"your answer is: {answersquarekmtosquarefeet}")
            input("")
        elif int(squarekmtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square KM to Square Inches")
            squarekmtosquareinch = input("")
            answersquarekmtosquareinch = float(squarekmtosquareinch) * 1550000000
            print(f"your answer is: {answersquarekmtosquareinch}")
            input("")
        elif int(squarekmtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square KM to Hectares")
            squarekmtohectare = input("")
            answersquarekmtohectare = float(squarekmtohectare) * 100
            print(f"your answer is: {answersquarekmtohectare}")
            input("")
        elif int(squarekmtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acre. Ok, now input how many Square KM to Acres")
            squarekmtoacres = input("")
            answersquarekmtoacres = float(squarekmtoacres) * 247.1
            print(f"your answer is {answersquarekmtoacres}")
            input("")
    elif int(areaoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Square M. Ok, now what do you want to convert that to?")
        print("1. Square Kilometre\n2. Square Mile\n3. Square Yard\n4. Square Foot\n5. Square Inch\n6. Hectare\n7. Acre")
        squaremtowhat = input("Select a number 1-7 for the corresponding unit: ")
        if int(squaremtowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square KM. Ok, now input how many Square M to Square KM")
            squaremtosquarekm = input("")
            answersquaremtosquarekm = float(squaremtosquarekm) / 1000000
            print(f"your answer is: {answersquaremtosquarekm}i) ")
            input("")
        elif int(squaremtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Mi. Ok, now input how many Square M to Square Mi")
            squaremtosquaremi = input("")
            answersquaremtosquaremi = float(squaremtosquaremi) / 2590000
            print(f"your answer is: {answersquaremtosquaremi}")
            input("")
        elif int(squaremtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square M to Square Yards")
            squaremtosquareyards = input("")
            answersquarekmtosquareyards = float(squaremtosquareyards) * 1.196
            print(f"your answer is: {answersquarekmtosquareyards}")
            input("")
        elif int(squaremtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square M to Square Feet")
            squaremtosquarefeet = input("")
            answersquaremtosquarefoot = float(squaremtosquarefeet) * 10.764
            print(f"your answer is: {answersquaremtosquarefoot}")
            input("")
        elif int(squaremtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square M to Square Inches")
            squaremtosquareinch = input("")
            answersquaremtosquareinches = float(squaremtosquareinch) * 1550
            print(f"your answer is: {answersquaremtosquareinches}")
            input("")
        elif int(squaremtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square M to Hectares")
            squaremtohectare = input("")
            answersquaremtohectare = float(squaremtohectare) / 10000
            print(f"your answer is: {answersquaremtohectare}")
            input("")
        elif int(squaremtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acre. Ok, now input how many Square M to Acres")
            squaremtoacre = input("")
            answersquaremtoacre = float(squaremtoacre) / 4047
            print(f"your answer is: {answersquaremtoacre}")
            input("")
    elif int(areaoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Square MI. Ok, now what do you want to convert that to?")
        print("1. Square Kilometre\n2. Square Metre\n3. Square Yard\n4. Square Foot\n5. Square Inch\n6. Hectare\n7. Acre")
        squaremitowhat = input("Select a number 1-7 for the corresponding unit: ")
        if int(squaremitowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square KM. Ok, now input how many Square MI to Square KM")
            squaremitosquarekm = input("")
            answersquaremitosquarekm = float(squaremitosquarekm) * 2.59 
            print(f"your answer is: {answersquaremitosquarekm}")
            input("")
        elif int(squaremitowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square MI to Square Ms")
            squaremitosquarem = input("")
            answersquaremitosquarem = float(squaremitosquarem) * 2590000
            print(f"your answer is: {answersquaremitosquarem}") 
            input("") 
        elif int(squaremitowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square MI to Square Yards")
            squaremitosquareyard = input("")
            answersquaremitosquareyard = float(squaremitosquareyard) * 3098000
            print(f"your answer is: {answersquaremitosquareyard}") 
            input("") 
        elif int(squaremitowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square MI to Square Feet")
            squaremitosquarefeet = input("")
            answersquaremitosquarefeet = float(squaremitosquarefeet) * 27880000
            print(f"your answer is: {answersquaremitosquarefeet}") 
            input("")
        elif int(squaremitowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square MI to Square Inches")
            squaremitosquareinch = input("")
            answersquaremitosquareinch = float(squaremitosquareinch) * 4014000000
            print(f"your answer is: {answersquaremitosquareinch}") 
            input("")
        elif int(squaremitowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square MI to Hectares")
            squaremitohectare = input("")
            answersquaremitohectare = float(squaremitohectare) * 259
            print(f"your answer is: {answersquaremitohectare}") 
            input("")
        elif int(squaremitowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acre. Ok, now input how many Square MI to Acres")
            squaremitoacre = input("")
            answersquaremitoacre = float(squaremitoacre) * 640
            print(f"your answer is: {answersquaremitoacre}") 
            input("")
    elif int(areaoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Square Yard. Ok, now what do you want to convert that to?")
        print("1. Square Kilometre\n2. Square Metre\n3. Square Miles\n4. Square Foot\n5. Square Inch\n6. Hectare\n7. Acre")
        squareyardtowhat = input("Select a number 1-7 for the corresponding unit: ")
        if int(squareyardtowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square KM. Ok, now input how many Square Yards to Square KM")
            squareyardstosquarekm = input("")
            answersquareyardstosquarekm = float(squareyardstosquarekm) * 1196000
            print(f"your answer is: {answersquareyardstosquarekm}")
            input("")
        elif int(squareyardtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square Yards to Square Ms")
            squareyardtosquarem = input("")
            answersquareyardtosquarem = float(squareyardtosquarem) / 1.196
            print(f"your answer is: {answersquareyardtosquarem}") 
            input("") 
        elif int(squareyardtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Miles. Ok, now input how many Square Yards to Square Mi")
            squareyardstosquaremi = input("")
            answersquareyardstosquaremi = float(squareyardstosquaremi) / 3098000
            print(f"your answer is: {answersquareyardstosquaremi}") 
            input("") 
        elif int(squareyardtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square Yards to Square Feet")
            squareyardtosquarefeet = input("")
            answersquareyardtosquarefeet = float(squareyardtosquarefeet) * 9
            print(f"your answer is: {answersquareyardtosquarefeet}") 
            input("")
        elif int(squareyardtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square Yards to Square Inches")
            squareyardtosquareinch = input("")
            answersquareyardtosquareinch = float(squareyardtosquareinch) * 1296
            print(f"your answer is: {answersquareyardtosquareinch}") 
            input("")
        elif int(squareyardtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square Yards to Hectares")
            squareyardtohectare = input("")
            answersquareyardtohectare = float(squareyardtohectare) * 259
            print(f"your answer is: {answersquareyardtohectare}") 
            input("")
        elif int(squareyardtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acres. Ok, now input how many Yards to Acres")
            squareyardtoacre = input("")
            answersquareyardtoacre = float(squareyardtoacre) / 4840
            print(f"your answer is: {answersquareyardtoacre}") 
            input("")
    elif int(areaoption) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Square Feet. Ok, now what do you want to convert that to?")
        print("1. Square Kilometre\n2. Square Metre\n3. Square Miles\n4. Square Yard\n5. Square Inch\n6. Hectare\n7. Acre")
        squarefoottowhat = input("Select a number 1-7 for the corresponding unit: ")
        if int(squarefoottowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square KM. Ok, now input how many Square Feet to Square KM")
            squarefoottosquarekm = input("")
            answersquarefoottosquarekm = float(squarefoottosquarekm) / 10760000
            print(f"your answer is: {answersquarefoottosquarekm}")
            input("")
        elif int(squarefoottowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square Feet to Square Ms")
            squarefoottosquarem = input("")
            answersquarefoottosquarem = float(squarefoottosquarem) / 10.764
            print(f"your answer is: {answersquarefoottosquarem}") 
            input("") 
        elif int(squarefoottowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Miles. Ok, now input how many Square Feet to Square Mi")
            squarefoottosquaremi = input("")
            answersquarefoottosquaremi = float(squarefoottosquaremi) / 27880000
            print(f"your answer is: {answersquarefoottosquaremi}") 
            input("") 
        elif int(squarefoottowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square Feet to Square Yards")
            squarefeettosquareyards = input("")
            answersquarefeettosquareyards = float(squarefeettosquareyards) / 9
            print(f"your answer is: {answersquarefeettosquareyards}") 
            input("")
        elif int(squarefoottowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square Feet to Square Inches")
            squarefoottosquareinch = input("")
            answersquarefeettosquareinch = float(squarefoottosquareinch) * 1296
            print(f"your answer is: {answersquarefeettosquareinch}") 
            input("")
        elif int(squarefoottowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square Feet to Hectares")
            squarefeettohectare = input("")
            answersquarefeettohectare = float(squarefeettohectare) / 107600
            print(f"your answer is: {answersquarefeettohectare}") 
            input("")
        elif int(squarefoottowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acres. Ok, now input how many Square Feet to Acres")
            squarefeettoacre = input("")
            answersquarefeettoacre = float(squarefeettoacre) / 43560
            print(f"your answer is: {answersquarefeettoacre}") 
            input("")
    elif int(areaoption) == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Square Inch. Ok, now what do you want to convert that to?")
        print("1. Square Kilometre\n2. Square Metre\n3. Square Miles\n4. Square Yard\n5. Square Foot\n6. Hectare\n7. Acre")
        squareinchtowhat = input("Select a number 1-7 for the corresponding unit: ")
        if int(squareinchtowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square KM. Ok, now input how many Square Inches to Square KM")
            squareinchtosquarekm = input("")
            answersquareinchtosquarekm = float(squareinchtosquarekm) / 1550000000
            print(f"your answer is: {answersquareinchtosquarekm}")
            input("")
        elif int(squareinchtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square Inches to Square Ms")
            squareinchtosquarem = input("")
            answersquareinchtosquarem = float(squareinchtosquarem) / 1550
            print(f"your answer is: {answersquareinchtosquarem}") 
            input("") 
        elif int(squareinchtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Miles. Ok, now input how many Square Inches to Square Mi")
            squareinchtosquaremi = input("")
            answersquareinchtosquaremi = float(squareinchtosquaremi) / 4014000000
            print(f"your answer is: {answersquareinchtosquaremi}") 
            input("") 
        elif int(squareinchtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square Inches to Square Yards")
            squareinchtosquareyards = input("")
            answersquareinchtosquareyards = float(squareinchtosquareyards) / 1296
            print(f"your answer is: {answersquareinchtosquareyards}") 
            input("")
        elif int(squareinchtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square Inches to Square Feet")
            squareinchtosquarefoot = input("")
            answersquareinchtosquarefoot = float(squareinchtosquarefoot) / 144
            print(f"your answer is: {answersquareinchtosquarefoot}") 
            input("")
        elif int(squareinchtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square Inches to Hectares")
            squareinchtohectare = input("")
            answersquareinchtohectare = float(squareinchtohectare) / 15500000
            print(f"your answer is: {answersquareinchtohectare}") 
            input("")
        elif int(squareinchtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acres. Ok, now input how many Square Feet to Acres")
            squareinchtoacre = input("")
            answersquareinchtoacre = float(squareinchtoacre) / 6273000
            print(f"your answer is: {answersquareinchtoacre}") 
            input("") 
     
    elif int(areaoption) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now what do you want to convert that to?")
            print("1. Square Kilometre\n2. Square Metre\n3. Square Miles\n4. Square Yard\n5. Square Foot\n6. Square Inch\n7. Acre")
            hectaretowhat = input("Select a number 1-7 for the corresponding unit: ")
            if int(hectaretowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square KM. Ok, now input how many Hectares to Square KM")
                hectaretosquarekm = input("")
                answerhectaretosquarekm = float(hectaretosquarekm) / 100
                print(f"your answer is: {answerhectaretosquarekm}")
                input("")
            elif int(hectaretowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square M. Ok, now input how many Hectares to Square Ms")
                hectaretosquarem = input("")
                answerhectaretosquarem = float(hectaretosquarem) * 10000
                print(f"your answer is: {answerhectaretosquarem}") 
                input("") 
            elif int(hectaretowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Miles. Ok, now input how many Hectares to Square Mi")
                hectaretosquaremi = input("")
                answerhectaretosquaremi = float(hectaretosquaremi) / 259
                print(f"your answer is: {answerhectaretosquaremi}") 
                input("") 
            elif int(hectaretowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Yard. Ok, now input how many Hectares to Square Yards")
                hectaretosquareyards = input("")
                answerhectaretosquareyards = float(hectaretosquareyards) * 11960
                print(f"your answer is: {answerhectaretosquareyards}") 
                input("")
            elif int(hectaretowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Foot. Ok, now input how many Hectares to Square Feet")
                hectaretosquarefoot = input("")
                answerhectaretosquarefoot = float(hectaretosquarefoot) * 107600
                print(f"your answer is: {answerhectaretosquarefoot}") 
                input("")
            elif int(hectaretowhat) == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hectare. Ok, now input how many Hectares to Square Inches")
                hectaretosquareinch = input("")
                answerhectaretosquareinch = float(hectaretosquareinch) * 1550000000
                print(f"your answer is: {answerhectaretosquareinch}") 
                input("")
            elif int(hectaretowhat) == 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Acres. Ok, now input how many Square Feet to Acres")
                hectaretoacre = input("")
                answerhectaretoacre = float(hectaretoacre) * 2.471
                print(f"your answer is: {answerhectaretoacre}") 
                input("")   

    
    elif int(areaoption) == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("acre. Ok, now what do you want to convert that to?")
            print("1. Square Kilometre\n2. Square Metre\n3. Square Miles\n4. Square Yard\n5. Square Foot\n6. Square Inch\n7. acre")
            acretowhat = input("Select a number 1-7 for the corresponding unit: ")
            if int(acretowhat) == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square KM. Ok, now input how many acres to Square KM")
                acretosquarekm = input("")
                answeracretosquarekm = float(acretosquarekm) / 247.1
                print(f"your answer is: {answeracretosquarekm}")
                input("")
            elif int(acretowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square M. Ok, now input how many acres to Square Ms")
                acretosquarem = input("")
                answeracretosquarem = float(acretosquarem) / 4047
                print(f"your answer is: {answeracretosquarem}") 
                input("") 
            elif int(acretowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Miles. Ok, now input how many acres to Square Mi")
                acretosquaremi = input("")
                answeracretosquaremi = float(acretosquaremi) / 640
                print(f"your answer is: {answeracretosquaremi}") 
                input("") 
            elif int(acretowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Yard. Ok, now input how many acres to Square Yards")
                acretosquareyards = input("")
                answeracretosquareyards = float(acretosquareyards) * 4840
                print(f"your answer is: {answeracretosquareyards}") 
                input("")
            elif int(acretowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Foot. Ok, now input how many acres to Square Feet")
                acretosquarefoot = input("")
                answeracretosquarefoot = float(acretosquarefoot) * 43560
                print(f"your answer is: {answeracretosquarefoot}") 
                input("")
            elif int(acretowhat) == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("acre. Ok, now input how many Acres to Square Inches")
                acretosquareinch = input("")
                answeracretosquareinch = float(acretosquareinch) / 6273000
                print(f"your answer is: {answeracretosquareinch}") 
                input("")
            elif int(acretowhat) == 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hectares. Ok, now input how many Acres to Hectares")
                acretohectare = input("")
                answeracretohectare = float(acretohectare) / 2.471
                print(f"your answer is: {answeracretohectare}") 
                input("")             
                 
         
def timee():
    print("1. Millisecond\n2. Seconds\n3. Minutes\n4. Hours\n5. Days")
    timeoption = input("Select a number 1-5 for the corresponding unit")
    if int(timeoption) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Milliseconds. Ok, now what do you want to convert that to?")
        print("1. Seconds\n2. Minutes\n3. Hours\n4. Days")
        mstowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(mstowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Seconds. Ok, now input how many Milliseconds to Seconds")
            mstosec = input("")
            answermstosec = float(mstosec) / 1000
            print(f"your answer is: {answermstosec}")
            input("")
        elif int(mstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Minutes. Ok, now input how many Milliseconds to Minutes")
            mstomin = input("")
            answermstomin = float(mstomin) / 60000
            print(f"your answer is {answermstomin}")
            input("")
        elif int(mstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hours. Ok, now input how many Milliseconds to Hours")
            mstohour = input("")
            answermstohour = float(mstohour) / 3600000
            print(f"your answer is {answermstohour}")
            input("")
        elif int(mstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Days. Ok, now input how many Milliseconds to Days")
            mstodays = input("")
            answermstodays = float(mstodays) / 86400000
            print(f"your answer is: {answermstodays}")
            input("")
    elif int(timeoption) == 2:             
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seconds. Ok, now what do you want to convert that to?")
        print("1. Milliseconds\n2. Minutes\n3. Hours\n4. Days")
        sectowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(sectowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Milliseconds. Ok, now input how many Seconds to Milliseconds")
            sectoms = input("")
            answersectoms = float(sectoms) * 1000
            print(f"your answer is: {answersectoms}")
            input("")
        elif int(sectowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Minutes. Ok, now input how many Seconds to Minutes")
            sectomins = input("")
            answersectomins = float(sectomins) / 60 
            print(f"your answer is: {answersectomins}")
            input("")
        elif int(sectowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hours. Ok, now input how many Seconds to Hours")
            sectohours = input("")
            answersectohours = float(sectohours) / 3600 
            print(f"your answer is: {answersectohours}")
            input("")
        elif int(sectowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Days. Ok, now input how many Seconds to Days")
            sectodays = input("")
            answersectodays = float(sectodays) / 86400
            print(f"your answer is: {answersectodays}")
            input("")
    elif int(timeoption) == 3:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("Minutes. Ok, now what do you want to convert that to?")
       print("1. Milliseconds\n2. Seconds\n3. Hours\n4. Days")
       mintowhat = input("Select a number 1-4 for the corresponding unit: ")
       if int(mintowhat) == 1:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Milliseconds. Ok, now input how many Minutes to Milliseconds")
           mintoms = input("")
           answermintoms = float(mintoms) * 60000
           print(f"your answer is: {answermintoms}")
           input("")
       elif int(mintowhat) == 2:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Seconds. Ok, now input how many Minutes to Seconds")
           mintosec = input("")
           answermintosec = float(mintosec) * 60
           print(f"your answer is: {answermintosec}")
           input("")
       elif int(mintowhat) == 3:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Hours. Ok, now input how many Minutes to Hours")
           mintohr = input("")
           answermintohr = float(mintohr) / 60
           print(f"your answer is: {answermintohr}")
           input("")
       elif int(mintowhat) == 4:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Days. Ok, now input how many Minutes to Days")
           mintodays = input("")
           answermintodays = float(mintodays) / 1440
           print(f"your answer is: {answermintodays}")
           input("")
    elif int(timeoption) == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hours. Ok, now what do you want to convert that to?")
        print("1. Milliseconds\n2. Seconds\n3. Minutes\n4. Days")
        hrtowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(hrtowhat) == 1:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Milliseconds. Ok, now input how many Hours to Milliseconds")
           hrtoms = input("")
           answerhrtoms = float(hrtoms) * 3600000
           print(f"your answer is: {answerhrtoms}")
           input("")
        elif int(hrtowhat) == 2:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Seconds. Ok, now input how many Hours to Seconds")
           hrtosec = input("")
           answerhrtosec = float(hrtosec) * 3600
           print(f"your answer is: {answerhrtosec}")
           input("")
        elif int(hrtowhat) == 3:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Minutes. Ok, now input how many Hours to Minutes")
           hrtomin = input("")
           answerhrtomin = float(hrtomin) * 60 
           print(f"your answer is: {answerhrtomin}")
           input("")
        elif int(hrtowhat) == 4:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Days. Ok, now input how many Hours to Days")
           hrtodays = input("")
           answerhrtodays = float(hrtodays) / 24 
           print(f"your answer is: {answerhrtodays}")
           input("")
    elif int(timeoption) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Days. Ok, now what do you want to convert that to?")
        print("1. Milliseconds\n2. Seconds\n3. Minutes\n4. Hours")
        daytowhat = input("Select a number 1-4 for the corresponding unit: ")
        if int(daytowhat) == 1:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Milliseconds. Ok, now input how many Days to Milliseconds")
           daystoms = input("")
           answerdaystoms = float(daystoms) * 86400000
           print(f"your answer is: {answerdaystoms}")
           input("")
        elif int(daytowhat) == 2:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Seconds. Ok, now input how many Days to Seconds")
           daystosec = input("")
           answerdaystosec = float(daystosec) * 86400
           print(f"your answer is: {answerdaystosec}")
           input("")
        elif int(daytowhat) == 3:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Minutes. Ok, now input how many Days to Minutes")
           daystomin = input("")
           answerdaystomin = float(daystomin) * 1440
           print(f"your answer is: {answerdaystomin}")
           input("")
        elif int(daytowhat) == 4:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Hours. Ok, now input how many Days to Hours")
           daystohr = input("")
           answerdaystohr = float(daystohr) / 24 
           print(f"your answer is: {answerdaystohr}")
           input("")




    


print("Welcome to ConvertU")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("1. Mass\n2. Digital Storage\n3. Length\n4. Speed\n5. Temperature\n6. Frequency\n7. Area\n8. Time")
option1 = input("Select a number 1-8 for the corresponding unit type: ")
os.system('cls' if os.name == 'nt' else 'clear')



if int(option1) == 1:
    mass() 
elif int(option1) == 2:
    storage()
elif int(option1) == 3:
    length()
elif int(option1) == 4:
    speed()
elif int(option1) == 5:
    temperature()
elif int(option1) == 6:
    frequency()
elif int(option1) == 7:
    area()
elif int(option1) == 8:
    timee()
