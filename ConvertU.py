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
            roundtonstokilograms = round(answertonstokilograms, 2)
            print(f"your answer is: {roundtonstokilograms}")
            input("")
        elif int(tonstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Grams. Ok, input how many Tons to Grams")
            tonstograms = input("")
            answertonstograms = float(tonstograms) * 907200
            roundtonstograms = round(answertonstograms, 2)
            print(f"your answer is: {roundtonstograms}")
            input("")
        elif int(tonstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Milligrams. Ok, input how many Tons to Milligrams")
            tonstomilligrams = input("")
            answertonstomilligrams = float(tonstomilligrams) * 970200000
            roundtonstomilligrams = round(answertonstomilligrams, 2)
            print(f"your answer is: {roundtonstomilligrams}")
            input("")
        elif int(tonstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pounds. Ok, input how many Tons to Pounds")
            tonstopounds = input("")
            answertonstopounds = float(tonstopounds) * 2000
            roundtonstopounds = round(answertonstopounds, 2)
            print(f"your answer is: {roundtonstopounds}")
            input("")
        elif int(tonstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ounces. Ok, input how many Tons to Ounces")
            tonstoounces = input("")
            answertonstoounces = float(tonstoounces) * 32000
            roundtonstoounces = round(answertonstoounces, 2)
            print(f"your answer is: {roundtonstoounces}")
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
                roundkilogramstotons = round(answerkilogramstotons, 2)
                print(f"your answer is: {roundkilogramstotons}")
                input("")
        elif int(kilogramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Grams. Ok, input how many Kilograms to Grams")
                kilogramstograms = input("")
                answerkilogramstograms = float(kilogramstograms) * 1000
                roundkilogramstograms = round(answerkilogramstograms, 2)
                print(f"your answer is: {roundkilogramstograms}")
                input("")
        elif int(kilogramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Milligrams. Ok, input how many Kilograms to Milligrams")
                kilogramstomilligrams = input("")
                answerkilogramstomilligrams = float(kilogramstomilligrams) * 1000000
                roundkilogramstomilligrams = round(answerkilogramstomilligrams, 2)
                print(f"your answer is: {roundkilogramstomilligrams}")
                input("")
        elif int(kilogramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Pounds. Ok, input how many Kilograms to Pounds")
                kilogramstopounds = input("")
                answerkilogramstopounds = float(kilogramstopounds) * 2.205
                roundkilogramstopounds = round(answerkilogramstopounds, 2)
                print(f"your answer is: {roundkilogramstopounds}")
                input("")
        elif int(kilogramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Ounces. Ok, input how many Kilograms to Ounces")
                kilogramstoounces = input("")
                answerkilogramstoounces = float(kilogramstoounces) * 35.274
                roundkilogramstoounces = round(answerkilogramstoounces, 2)
                print(f"your answer is: {roundkilogramstoounces}")
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
                roundgramstotons = round(answergramstotons, 2)
                print(f"your answer is: {roundgramstotons}")
                input("")
        elif int(gramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Grams to Kilograms")
                gramstokilograms = input("")
                answergramstokilograms = float(gramstokilograms) / 1000
                roundgramstokilograms = round(answergramstokilograms, 2)
                print(f"your answer is: {roundgramstokilograms}")
                input("")
        elif int(gramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Grams to Milligrams")
                gramstomilligrams = input("")
                answergramstomilligrams = float(gramstomilligrams) * 1000
                roundgramstomilligrams = round(answergramstomilligrams, 2)
                print(f"your answer is: {roundgramstomilligrams}")
                input("")
        elif int(gramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many Grams to Pounds")
                gramstopounds = input("")
                answergramstopounds = float(gramstopounds) / 453.6
                roundgramstopounds = round(answergramstopounds, 2)
                print(f"your answer is: {roundgramstopounds}")
                input("")
        elif int(gramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many Grams to Ounces")
                gramstoounces = input("")
                answergramstoounces = float(gramstoounces) / 28.35
                roundgramstoounces = round(answergramstoounces, 2)
                print(f"your answer is: {roundgramstoounces}")
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
                roundmilligramstotons = round(answermilligramstotons, 2)
                print(f"your answer is: {roundmilligramstotons}")
                input("")
        elif int(milligramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Milligrams to Kilograms")
                milligramstokilograms = input("")
                answermilligramstokilograms = float(milligramstokilograms) / 1000000
                roundmilligramstokilograms = round(answermilligramstokilograms, 2)
                print(f"your answer is: {roundmilligramstokilograms}")
                input("")
        elif int(milligramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Milligrams to Grams")
                milligramstograms = input("")
                answermilligramstograms = float(milligramstograms) / 1000
                roundmilligramstograms = round(answermilligramstograms, 2)
                print(f"your answer is: {roundmilligramstograms}")
                input("")
        elif int(milligramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many milligrams to Pounds")
                milligramstopounds = input("")
                answermilligramstopounds = float(milligramstopounds) / 453600
                roundmilligramstopounds = round(answermilligramstopounds, 2)
                print(f"your answer is: {roundmilligramstopounds}")
                input("")
        elif int(milligramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many milligrams to Ounces")
                milligramstoounces = input("")
                answermilligramstoounces = float(milligramstoounces) / 28350
                roundmilligramstoounces = round(answermilligramstoounces, 2)
                print(f"your answer is: {roundmilligramstoounces}")
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
                roundpoundstotons = round(answerpoundstotons, 2)
                print(f"your answer is: {roundpoundstotons}")
                input("")
        elif int(poundstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Pounds to Kilograms")
                poundstokilograms = input("")
                answerpoundstokilograms = float(poundstokilograms) / 2.205
                roundpoundstokilograms = round(answerpoundstokilograms, 2)
                print(f"your answer is: {roundpoundstokilograms}")
                input("")
        elif int(poundstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Pounds to Grams")
                poundstograms = input("")
                answerpoundstograms = float(poundstograms) * 453.6
                roundpoundstograms = round(answerpoundstograms, 2)
                print(f"your answer is: {roundpoundstograms}")
                input("")
        elif int(poundstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Pounds to Milligrams")
                poundstomilligrams = input("")
                answerpoundstomilligrams = float(poundstomilligrams) * 453600
                roundpoundstomilligrams = round(answerpoundstomilligrams, 2)
                print(f"your answer is: {roundpoundstomilligrams}")
                input("")
        elif int(poundstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many Pounds to Ounces")
                poundstoounces = input("")
                answerpoundstoounces = float(poundstoounces) * 16
                roundpoundstoounces = round(answerpoundstoounces, 2)
                print(f"your answer is: {roundpoundstoounces}") 
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
                roundouncestotons = round(answerouncestotons, 2)
                print(f"your answer is {roundouncestotons}")
                input("")
        elif int(ouncestowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Ounces to Kilograms")
                ouncestokilograms = input("")
                answerouncestokilograms = float(ouncestokilograms) / 35.274
                roundouncestokilograms = round(answerouncestokilograms, 2)
                print(f"your answer is {roundouncestokilograms}")
                input("")
        elif int(ouncestowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Grams. Ok, input how many Ounces to Grams")
                ouncestograms = input("")
                answerouncestograms = float(ouncestograms) * 28.35
                roundouncestograms = round(answerouncestograms, 2)
                print(f"your answer is: {roundouncestograms}")
                input("")
        elif int(ouncestowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Ounces to Milligrams")
                ouncestomilligrams = input("")
                answerouncestomilligrams = float(ouncestomilligrams) * 28350
                roundouncestomilligrams = round(answerouncestomilligrams, 2)
                print(f"your answer is: {roundouncestomilligrams}")
                input("")
        elif int(ouncestowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many Ounces to Pounds")
                ouncestopounds = input("")
                answerouncestopounds = float(ouncestopounds) / 16
                roundouncestopounds = round(answerouncestopounds, 2)
                print(f"your answer is: {roundouncestopounds}")
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
            roundbytestokilobytes = round(answerbytestokilobytes, 2)
            print(f"your answer is: {roundbytestokilobytes}")
            input("")
        elif int(bytestowhat) == 2: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, input how many Bytes to Megabytes")
            bytestomegabytes = input("")
            answerbytestomegabytes = float(bytestomegabytes) / 1000000
            roundbytestomegabytes = round(answerbytestomegabytes, 2)
            print(f"your answer is: {roundbytestomegabytes}")
            input("")
        elif int(bytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabyte. Ok, input how many Bytes to Gigabytes")
            bytestogigabytes = input("")
            answerbytestogigabytes = float(bytestogigabytes) / 1000000000 
            roundbytestogigabytes = round(answerbytestogigabytes, 2)
            print(f"your answer is: {roundbytestogigabytes}")
            input("")
        elif int(bytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, input how many Bytes to Terabytes")
            bytestoterabytes = input("")
            answerbytestoterabytes = float(bytestoterabytes) / 1000000000000
            roundbytestoterabytes = round(answerbytestoterabytes, 2)
            print(f"your answer is: {roundbytestoterabytes}")
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
            roundkilobytestobytes = round(answerkilobytestobytes, 2)
            print(f"your answer is: {roundkilobytestobytes}")
            input("")
        elif int(kilobytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, input how many Kilobytes to Megabytes")
            kilobytestomegabytes = input("")
            answerkilobytestomegabytes = float(kilobytestomegabytes) / 1000
            roundkilobytestomegabytes = round(answerkilobytestomegabytes, 2)
            print(f"your answer is: {roundkilobytestomegabytes}")
            input("")
        elif int(kilobytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, input how many Kilobytes to Gigabytes")
            kilobytestogigabytes = input("")
            answerkilobytestogigabytes = float(kilobytestogigabytes) / 1000000
            roundkilobytestogigabytes = round(answerkilobytestogigabytes, 2)
            print(f"your answer is: {roundkilobytestogigabytes}")
            input("")
        elif int(kilobytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabytes. Ok, input how many Kilobytes to Terabytes")
            kilobytestoterabytes = input("")
            answerkilobytestoterabytes = float(kilobytestoterabytes) / 1000000000
            roundkilobytestoterabytes = round(answerkilobytestoterabytes, 2)
            print(f"your answer is: {roundkilobytestoterabytes}")
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
            roundgigabytestobytes = round(answergigabytestobytes, 2 )
            print(f"your answer is: {roundgigabytestobytes}")
            input("")
        elif int(gigabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Gigabytes to Kilobytes")
            gigabytestokilobytes = input("")
            answergigabytestokilobytes = float(gigabytestokilobytes) * 1000000
            roundgigabytestokilobytes = round(answergigabytestokilobytes, 2)
            print(f"your answer is: {roundgigabytestokilobytes}")
            input("")
        elif int(gigabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, now input how many Gigabytes to Megabytes")
            gigabytestomegabytes = input("")
            answergigabytestomegabytes = float(gigabytestomegabytes) * 1000
            roundgigabytestomegabytes = round(answergigabytestomegabytes, 2)
            print(f"your answer is: {roundgigabytestomegabytes}")
            input("")
        elif int(gigabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, now input how many Gigabytes to Terabytes")
            gigabytestoterabytes = input("")
            answergigabytestoterabytes = float(gigabytestoterabytes) / 1000
            roundgigabytestoterabytes = round(answergigabytestoterabytes, 2)
            print(f"your answer is: {roundgigabytestoterabytes}")
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
            roundmegabytestobytes = round(answermegabytestobytes, 2)
            print(f"your answer is: {roundmegabytestobytes}")
            input("")
        elif int(megabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Megabytes to Kilobytes")
            megabytestokilobytes = input("")
            answermegabytestokilobytes = float(megabytestokilobytes) * 1000
            roundmegabytestokilobytes = round(answermegabytestokilobytes, 2)
            print(f"your answer is: {roundmegabytestokilobytes}")
            input("")
        elif int(megabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, now input how many Megabytes to Gigabytes")
            megabytestogigabytes = input("")
            answermegabytestogigabytes = float(megabytestogigabytes) / 1000
            roundmegabytestogigabytes = round(answermegabytestogigabytes, 2)
            print(f"your answer is: {roundmegabytestogigabytes}")
            input("")
        elif int(megabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, now input how many Megabytes to Terabytes")
            megabytestoterabytes = input("")
            answermegabytestoterabytes = float(megabytestoterabytes) / 1000000
            roundmegabytestoterabytes = round(answermegabytestoterabytes, 2)
            print(f"your answer is: {roundmegabytestoterabytes}")
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
            roundterabytestobytes = round(answerterabytestobytes, 2)
            print(f"your answer is: {roundterabytestobytes}")
            input("")
        elif int(terabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Terabytes to Kilobytes")
            terabytestokilobytes = input("")
            answerterabytestokilobytes = float(terabytestokilobytes) * 1000000000
            roundterabytestokilobytes = round(answerterabytestokilobytes, 2)
            print(f"your answer is: {roundterabytestokilobytes}")
            input("")
        elif int(terabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, now input how many Terabytes to Gigabytes")
            terabytestogigabytes = input("")
            answerterabytestogigabytes = float(terabytestogigabytes) * 1000 
            roundterabytestogigabytes = round(answerterabytestogigabytes, 2)
            print(f"your answer is: {roundterabytestogigabytes}")
            input("")
        elif int(terabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, now input how many Terabytes to Megabytes.")
            terabytestomegabytes = input("")
            answerterabytestomegabytes = float(terabytestomegabytes) * 1000000
            roundterabytestomegabytes = round(answerterabytestomegabytes, 2)
            print(f"your answer is: {roundterabytestomegabytes}")
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
            roundfeettometres = round(answerfeettometres, 2)
            print(f"your answer is: {roundfeettometres}")
            input("")
        elif int(feettowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Feet to Kilometres")
            feettokilometres = input("")
            answerfeettokilometres = float(feettokilometres) / 3281
            roundfeettokilometres = round(answerfeettokilometres, 2)
            print(f"your answer is: {roundfeettokilometres}")
            input("")
        elif int(feettowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Feet to Centimetres")
            feettocentimetres = input("")
            answerfeettocentimetres = float(feettocentimetres) * 30.48
            roundfeettocentimetres = round(answerfeettocentimetres, 2)
            print(f"your answer is: "  + str(roundfeettocentimetres))
            input("")
        elif int(feettowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Feet to Millimetres")
            feettomillimetres = input("")
            answerfeettomillimetres = float(feettomillimetres) * 304.8
            roundfeettomillimetres = round(answerfeettomillimetres, 2)
            print(f"your answer is: {roundfeettomillimetres}")
            input("")
        elif int(feettowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Feet to Yards")
            feettoyard = input("")
            answerfeettoyard = float(feettoyard) / 3
            roundfeettoyards = round(answerfeettoyard, 2)
            print(f"your answer is: {roundfeettoyards}")
            input("")
        elif int(feettowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Feet to Inches")
            feettoinches = input("")
            answerfeettoinches = float(feettoinches) * 12
            roundfeettoinches = round(answerfeettoinches, 2)
            print(f"your answer is: {roundfeettoinches}")
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
            roundmetrestofeet = round(answermetrestofeet, 2)
            print(f"your answer is: {roundmetrestofeet}")
            input("")
        elif int(metrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Metres to Kilometres")
            metrestokilometres = input("")
            answermetrestokilometres = float(metrestokilometres) / 1000
            roundmetrestokilometres = round(answermetrestokilometres, 2)
            print(f"your answer is: {roundmetrestokilometres}")
            input("")
        elif int(metrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Metres to Centimetres")
            metrestocentimetres = input("")
            answermetrestocentimetres = float(metrestocentimetres) * 100
            roundmetrestocentimetres = round(answermetrestocentimetres, 2)
            print(f"your answer is: {roundmetrestocentimetres}")
            input("")
        elif int(metrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Metres to Millimetres")
            metrestomillimetres = input("")
            answermetrestomillimetres = float(metrestomillimetres) * 1000
            roundmetrestomillimetres = round(answermetrestomillimetres, 2)
            print(f"your answer is: {roundmetrestomillimetres}")
            input("")
        elif int(metrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Metres to Yards")
            metrestoyards = input("")
            answermetrestoyards = float(metrestoyards) * 1.094
            roundmetrestoyards = round(answermetrestoyards, 2)
            print(f"your answer is: {roundmetrestoyards}")
            input("")
        elif int(metrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Metres to Inches")
            metrestoinches = input("")
            answermetrestoinches = float(metrestoinches) * 39.37
            roundmetrestoinches = round(answermetrestoinches, 2)
            print(f"your answer is: {roundmetrestoinches}")
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
            roundkilometrestofeet = round(answerkilometrestofeet, 2)
            print(f"your answer is: {roundkilometrestofeet}")
            input("")
        elif int(kilometrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Kilometres to Metres")
            kilometrestometres = input("")
            answerkilometrestometres = float(kilometrestometres) * 1000 
            roundkilometrestometres = round(answerkilometrestometres, 2)
            print(f"your answer is: {roundkilometrestometres}")
            input("")
        elif int(kilometrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Kilometres to Centimetres")
            kilometrestocentimetres = input("")
            answerkilometrestocentimetres = float(kilometrestocentimetres) * 100000 
            roundkilometrestocentimetres = round(answerkilometrestocentimetres, 2)
            print(f"your answer is: {roundkilometrestocentimetres}")
            input("")
        elif int(kilometrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Kilometres to Millimetres")
            kilometrestocentimetres = input("")
            answerkilometrestomillimetres = float(kilometrestocentimetres) * 1000000
            roundkilometrestomillimetres = round(answerkilometrestomillimetres, 2)
            print(f"your answer is: {roundkilometrestomillimetres}")
            input("")
        elif int(kilometrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Kilometres to Yards")
            kilometrestoyards = input("")
            answerkilometrestoyards = float(kilometrestoyards) * 1094
            roundkilometrestoyards = round(answerkilometrestoyards, 2)
            print(f"your answer is: {roundkilometrestoyards}")
            input("")
        elif int(kilometrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Kilometres to Inches")
            kilometrestoinches = input("")
            answerkilometrestoinches = float(kilometrestoinches) * 39370 
            roundkilometrestoinches = round(answerkilometrestoinches, 2)
            print(f"your answer is: {roundkilometrestoinches}")
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
            roundcentimetrestofeet = round(answercentimetrestofeet, 2)
            print(f"your answer is: {roundcentimetrestofeet}")
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
            roundcentimetrestokilometres = round(answercentimetrestokilometres, 2)
            print(f"your answer is: {roundcentimetrestokilometres}")
            input("")
        elif int(centimetrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Centimetres to Millimetres")
            centimetrestomillimetres = input("")
            answercentimetrestomillimetres = float(centimetrestomillimetres) * 10 
            roundcentimetrestomillimetres = round(answercentimetrestomillimetres, 2)
            print(f"your answer is: {roundcentimetrestomillimetres}")
            input("")
        elif int(centimetrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok. Now input how many Centimetres to Yards")
            centimetrestoyards = input("")
            answercentimetrestoyards = float(centimetrestoyards) / 91.44
            roundcentimetrestoyards = round(answercentimetrestoyards, 2)
            print(f"your answer is: {roundcentimetrestoyards}")
            input("")
        elif int(centimetrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Centimetres to Inches")
            centimetrestoinches = input("")
            answercentimetrestoinches = float(centimetrestoinches) / 2.54
            roundcentimetrestoinches = round(answercentimetrestoinches, 2)
            print(f"your answer is: {roundcentimetrestoinches}")
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
            roundmillimetrestofeet = round(answermillimetrestofeet, 2)
            print(f"your answer is: {roundmillimetrestofeet}")
            input("")
        elif int(millimetrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. OK, now input how many Millimetres to Metres")
            millimetrestometres = input("")
            answermillimetrestometres = float(millimetrestometres) / 1000
            roundmillimetrestometres = round(answermillimetrestometres, 2)
            print(f"your answer is: {roundmillimetrestometres}")
            input("")
        elif int(millimetrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Millimetres to Kilometres")
            millimetrestokilometres = input("")
            answermillimetrestokilometres = float(millimetrestokilometres) / 1000000
            roundmillimetrestokilometres = round(answermillimetrestokilometres, 2)
            print(f"your answer is: {roundmillimetrestokilometres}")
            input("")
        elif int(millimetrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Millimetres to Centimetres")
            millimetrestocentimetres = input("")
            answermillimetrestocentimetres = float(millimetrestocentimetres) / 10
            roundmillimetrestocentimetres = round(answermillimetrestocentimetres, 2)
            print(f"your answer is: {roundmillimetrestocentimetres}")
            input("")
        elif int(millimetrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Millimetres to Yards")
            millimetrestoyards = input("")
            answermillimetrestoyards = float(millimetrestoyards) / 914.4
            roundmillimetrestoyards = round(answermillimetrestoyards, 2)
            print(f"your answer is: {roundmillimetrestoyards}")
            input("")
        elif int(millimetrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Millimetres to Inches")
            millimetrestoinches = input("")
            answermillimetrestoinches = float(millimetrestoinches) / 25.4
            roundmillimetrestoinches = round(answermillimetrestoinches, 2)
            print(f"your answer is: {roundmillimetrestoinches}")
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
            roundyardstofeet = round(answeryardstofeet, 2)
            print(f"your answer is: {roundyardstofeet}")
            input("")
        elif int(yardstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Yards to Metres")
            yardstometres = input("")
            answeryardstometres = float(yardstometres) / 1.094
            roundyardstometres = round(answeryardstometres, 2)
            print(f"your answer is: {roundyardstometres}")
            input("")
        elif int(yardstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Yards to Kilometres")
            yardstokilometres = input("")
            answeryardstokilometres = float(yardstokilometres) / 1094
            roundyardstokilometres = round(answeryardstokilometres, 2)
            print(f"your answer is: {roundyardstokilometres}")
            input("")
        elif int(yardstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Yards to Centimetres")
            yardstocentimetres = input("")
            answeryardstocentimetres = float(yardstocentimetres) * 91.44
            roundyardstocentimetres = round(answeryardstocentimetres, 2)
            print(f"your answer is: {roundyardstocentimetres}")
            input("")
        elif int(yardstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Yards to Millimetres")
            yardstomillimetres = input("")
            answeryardstomillimetres = float(yardstomillimetres) * 914.44
            roundyardstomillimetres = round(answeryardstomillimetres, 2)
            print(f"your answer is: {roundyardstomillimetres}")
            input("")
        elif int(yardstowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Yards to Inches")
            yardstoinches = input("")
            answeryardstoinches = float(yardstoinches) * 36
            roundyardstoinches = round(answeryardstoinches, 2)
            print(f"your answer is: {roundyardstoinches}")
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
            roundinchestofeet = round(answerinchestofeet, 2)
            print(f"your answer is: {roundinchestofeet}")
            input("")
        elif int(inchestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Inches to Metres")
            inchestometres = input("")
            answerinchestometres = float(inchestometres) / 39.37
            roundinchestometres = round(answerinchestometres, 2)
            print(f"your answer is: {roundinchestometres}")
            input("")
        elif int(inchestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Inches to Kilometres")
            inchestokilometres = input("")
            answerinchestokilometres = float(inchestokilometres) / 39370
            roundinchestokilometres = round(answerinchestokilometres, 2)
            print(f"your answer is: {roundinchestokilometres}")
            input("")
        elif int(inchestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Inches to Centimetres")
            inchestocentimetres = input("")
            answerinchestocentimetres = float(inchestocentimetres) * 2.54
            roundinchestocentimetres = round(answerinchestocentimetres, 2)
            print(f"your answer is: {roundinchestocentimetres}")
            input("")
        elif int(inchestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Inches to Millimetres")
            inchestomillimetres = input("")
            answerinchestomillimetres = float(inchestomillimetres) * 25.4
            roundinchestomillimetres = round(answerinchestomillimetres, 2)
            print(f"your answer is: {roundinchestomillimetres}")
            input("")
        elif int(inchestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Inches to Yards")
            inchestoyards = input("")
            answerinchestoyards = float(inchestoyards) / 36
            roundinchestoyards = round(answerinchestoyards, 2)
            print(f"your answer is: {roundinchestoyards}")
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
            roundmphtokph = round(answermphtokph, 2)
            print(f"your answer is: {roundmphtokph}")
            input("")
        elif int(mphtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many MPH to FPS")
            mphtofps = input("")
            answermphtofps = float(mphtofps) * 1.467
            roundmphtofps = round(answermphtofps, 2)
            print(f"your answer is: {roundmphtofps}")
            input("")
        elif int(mphtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many MPH to MPS")
            mphtomps = input("")
            answermphtomps = float(mphtomps) * 2.237
            roundmphtomps = round(answermphtomps, 2)
            print(f"your answer is: {roundmphtomps}")
            input("")
        elif int(mphtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many MPH to Knots")
            mphtoknots = input("")
            answermphtoknots = float(mphtoknots) / 1.151
            roundmphtoknots = round(answermphtoknots, 2)
            print(f"your answer is: {roundmphtoknots}")
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
            roundkphtomph = round(answerkphtomph, 2)
            print(f"your answer is: {roundkphtomph}")
            input("")
        elif int(kphtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many KPH to FPS")
            kphtofps = input("")
            answerkphtofps = float(kphtofps) / 1.097
            roundkphtofps = round(answerkphtofps, 2)
            print(f"your answer is: {roundkphtofps}")
            input("")
        elif int(kphtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many KPH to MPS")
            kphtomps = input("")
            answerkphtomps = float(kphtomps) / 3.6 
            roundkphtomps = round(answerkphtomps, 2)
            print(f"your answer is: {roundkphtomps}")
            input("")
        elif int(kphtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many KPH to Knots")
            kphtoknots = input("")
            answerkphtoknots = float(kphtoknots) / 1.852
            roundkphtoknots = round(answerkphtoknots, 2)
            print(f"your answer is: {roundkphtoknots}")
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
            roundfpstomph = round(answerfpstomph, 2)
            print(f"your answer is: {roundfpstomph}")
            input("")
        elif int(fpstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many FPS to KPH")
            fpstokph = input("")
            answerfpstokph = float(fpstokph) / 1.097
            roundfpstokph = round(answerfpstokph, 2)
            print(f"your answer is: {roundfpstokph}")
            input("")
        elif int(fpstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many FPS to MPS")
            fpstomps = input("")
            answerfpstomps = float(fpstomps) / 3.281 
            roundfpstomps = round(answerfpstomps, 2)
            print(f"your answer is: {roundfpstomps}")
            input("")
        elif int(fpstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many FPS to Knots")
            fpstoknots = input("")
            answerfpstoknots = float(fpstoknots) / 1.688
            roundfpstoknots = round(answerfpstoknots, 2)
            print(f"your answer is: {roundfpstoknots}")
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
            roundmpstomph = round(answermpstomph, 2)
            print(f"your answer is {roundmpstomph}")
            input("")
        elif int(mpstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many MPS to KPH")
            mpstokph = input("")
            answermpstokph = float(mpstokph)
            roundmpstokph = round(answermpstokph, 2)
            print(f"your answer is: {roundmpstokph}")
            input("")
        elif int(mpstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many MPS to FPS")
            mpstofps = input("")
            answermpstofps = float(mpstofps) * 3.281
            roundmpstofps = round(answermpstofps, 2)
            print(f"your answer is: {roundmpstofps}")
            input("")
        elif int(mpstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many MPS to Knots")
            mpstoknots = input("")
            answermpstoknots = float(mpstoknots) * 1.944
            roundmpstoknots = round(answermpstoknots, 2)
            print(f"your answer is: {roundmpstoknots}")
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
            roundknotstomph = round(answerknotstomph, 2)
            print(f"your answer is: {roundknotstomph}")
            input("")
        elif int(knotstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many Knots to KPH")
            knotstokph = input("")
            answerknotstokph = float(knotstokph) * 1.852
            roundknotstokph = round(answerknotstokph, 2)
            print(f"your answer is: {roundknotstokph}")
            input("")
        elif int(knotstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many Knots to FPS")
            knotstofps = input("")
            answerknotstofps = float(knotstofps) * 1.688
            roundknotstofps = round(answerknotstofps, 2)
            print(f"your answer is: {roundknotstofps}")
            input("")
        elif int(knotstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many Knots to MPS")
            knotstomps = input("")
            answerknotstomps = float(knotstomps) / 1.944
            roundknotstomps = round(answerknotstomps, 2)
            print(f"your answer is: {roundknotstomps}")
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
            roundcelsiustofahrenheit = round(answercelsiustofahrenheit, 2)
            print(f"your answer is: {roundcelsiustofahrenheit}")
            input("")
        elif int(celsiustowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kelvin. Ok, now input how many Celsius to Kelvin")
            celsiustokelvin = input("")
            answercelsiustokelvin = float(celsiustokelvin) + 273.15
            roundcelsiustokelvin = round(answercelsiustokelvin, 2)
            print(f"your answer is: {roundcelsiustokelvin}")
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
            roundfahrenheittocelsius = round(answerfahrenheittocelsius, 2)
            print(f"your answer is: {roundfahrenheittocelsius}")
            input("")
        elif int(fahrenheittowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kelvin. Ok, now input how many Fahrenheit to Kelvin")
            fahrenheittokelvin = input("")
            answerfahrenheittokelvin = float(fahrenheittokelvin) + 459.67 * 0.5556
            roundfahrenheittokelvin = round(answerfahrenheittokelvin, 2)
            print(f"your answer is: {roundfahrenheittokelvin}")
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
            roundkelvintocelsius = round(answerkelvintocelsius, 2)
            print(f"your answer is: {roundkelvintocelsius}")
            input("")
        elif int(kelvintowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fahrenheit. Ok, now input how many Kelvin to Fahrenheit")
            kelvintofahrenheit = input("")
            answerkelvintofahrenheit = float(kelvintofahrenheit) - 273.15 * 1.8 + 32
            roundkelvintofahrenheit = round(answerkelvintofahrenheit, 2)
            print(f"your answer is: {roundkelvintofahrenheit}")
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
            roundhertztokilohertz = round(answerhertztokilohertz, 2)
            print(f"your answer is: {roundhertztokilohertz}")
            input("")
        elif int(hertztowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megahertz. Ok, now input how many Hertz to Megahertz")
            hertztomegahertz = input("")
            answerhertztomegahertz = float(hertztomegahertz) / 1000000
            roundhertztomegahertz = round(answerhertztomegahertz, 2)
            print(f"your answer is: {roundhertztomegahertz}")
            input("")
        elif int(hertztowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigahertz. Ok, now input how many Hertz to Gigahertz")
            hertztogigahertz = input("")
            answerhertztogigahertz = float(hertztogigahertz) / 1000000000
            roundhertztogigahertz = round(answerhertztogigahertz, 2)
            print(f"your answer is: {roundhertztogigahertz}")
            input("")
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
            roundkilohertztohertz = round(answerkilohertztohertz, 2)
            print(f"your answer is: {roundkilohertztohertz}")
            input("")
        elif int(kilohertztowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megahertz. Ok, now input how many Kilohertz to Megahertz")
            kilohertztomegahertz = input("")
            answerkilohertztomegahertz = float(kilohertztomegahertz) / 1000
            roundkilohertztomegahertz = round(answerkilohertztomegahertz, 2)
            print(f"your answer is: {roundkilohertztomegahertz}")
            input("")
        elif int(kilohertztowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigahertz. Ok, now input how many Kilohertz to Gigahertz")
            kilohertztogigahertz = input("")
            answerkilohertztogigahertz = float(kilohertztogigahertz) / 1000000
            roundkilohertztogigahertz = round(answerkilohertztogigahertz, 2)
            print(f"your answer is {roundkilohertztogigahertz}")
            input("")
    elif int(freqoption) ==  3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Megahertz. Ok, now what do you want to convert that to")
        print("1. Hertz\n2. Kilohertz\n3. Gigahertz")
        megahertztowhat = input("")
        if int(megahertztowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hertz. Ok, now input how many Megahertz to Hertz.")
            megahertztohertz = input("")
            answermegahertztohertz = float(megahertztohertz) * 1000000
            roundmegahertztohertz = round(answermegahertztohertz, 2)
            print(f"your answer is: {roundmegahertztohertz}")
            input("")
        elif int(megahertztowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilohertz. Ok, now input how many Megahertz to Kilohertz")
            megahertztokilohertz = input("")
            answermegahertztokilohertz = float(megahertztokilohertz) * 1000
            roundmegahertztokilohertz = round(answermegahertztokilohertz, 2)
            print(f"your answer is: {roundmegahertztokilohertz}")
            input("")
        elif int(megahertztowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigahertz. Ok, now input how many Megahertz to Gigahertz")
            megahertztogigahertz = input("")
            answermegahertztogigahertz = float(megahertztogigahertz) / 1000
            roundmegahertztogigahertz = round(answermegahertztogigahertz, 2)
            print(f"your answer is: {roundmegahertztogigahertz}")
            input("")
    elif int(freqoption) == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gigahertz. Ok, now what do you want to convert that to")
        print("1. Hertz\n2. Kilohertz\n3. Megahertz")
        gigahertztowhat = input("")
        if int(gigahertztowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hertz. Ok, now input how many Gigahertz to Hertz")
            gigahertztohertz = input("")
            answergigahertztohertz = float(gigahertztohertz) * 1000000000
            roundgigahertztohertz = round(answergigahertztohertz, 2)
            print(f"your answer is: {roundgigahertztohertz}")
            input("")
        elif int(gigahertztowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilohertz. Ok, now input how many Gigahertz to Kilohertz")
            gigahertztokilohertz = input("")
            answergigahertztokilohertz = float(gigahertztokilohertz) * 1000000 
            roundgigahertztokilohertz = round(answergigahertztokilohertz, 2)
            print(f"your answer is: {roundgigahertztokilohertz}")
            input("")
        elif int(gigahertztowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megahertz. Ok, now input how many Gigahertz to Megahertz")
            gigahertztomegahertz = input("")
            answergigahertztomegahertz = float(gigahertztomegahertz) * 1000
            roundgigahertztomegahertz = round(answergigahertztomegahertz, 2)
            print(f"your answer is: {roundgigahertztomegahertz}")
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
            roundsquarekmtosquarem = round(answersquarekmtosquarem, 2)
            print(f"your answer is: {roundsquarekmtosquarem}")
            input("")
        elif int(squarekmtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square MI. Ok, now input how many Square KM to Square MI")
            squarekmtosquaremi = input("")
            answersquarekmtosquaremi = float(squarekmtosquaremi) / 2.59
            roundsquarekmtosquaremi = round(answersquarekmtosquaremi, 2)
            print(f"your answer is: {roundsquarekmtosquaremi}")
            input("")
        elif int(squarekmtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square KM to Square Yards")
            squarekmtosquareyards = input("")
            answersquarekmtosquareyards = float(squarekmtosquareyards) * 1196000
            roundsquarekmtosquareyards = round(answersquarekmtosquareyards, 2)
            print(f"your answer is: {roundsquarekmtosquareyards}")
            input("")
        elif int(squarekmtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square KM to Square Feet")
            squarekmtosquarefeet = input("")
            answersquarekmtosquarefeet = float(squarekmtosquarefeet) * 10760000
            roundsquarekmtosquarefeet = round(answersquarekmtosquarefeet, 2)
            print(f"your answer is: {roundsquarekmtosquarefeet}")
            input("")
        elif int(squarekmtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square KM to Square Inches")
            squarekmtosquareinch = input("")
            answersquarekmtosquareinch = float(squarekmtosquareinch) * 1550000000
            roundsquarekmtosquareinch = round(answersquarekmtosquareinch, 2)
            print(f"your answer is: {roundsquarekmtosquareinch}")
            input("")
        elif int(squarekmtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square KM to Hectares")
            squarekmtohectare = input("")
            answersquarekmtohectare = float(squarekmtohectare) * 100
            roundsquarekmtohectare = round(answersquarekmtohectare, 2)
            print(f"your answer is: {roundsquarekmtohectare}")
            input("")
        elif int(squarekmtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acre. Ok, now input how many Square KM to Acres")
            squarekmtoacres = input("")
            answersquarekmtoacres = float(squarekmtoacres) * 247.1
            roundsquarekmtoacres = round(answersquarekmtoacres, 2)
            print(f"your answer is {roundsquarekmtoacres}")
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
            roundsquaremtosquarekm = round(answersquaremtosquarekm, 2)   
            print(f"your answer is: {roundsquaremtosquarekm}i) ")
            input("")
        elif int(squaremtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Mi. Ok, now input how many Square M to Square Mi")
            squaremtosquaremi = input("")
            answersquaremtosquaremi = float(squaremtosquaremi) / 2590000
            roundsquaremtosquaremi = round(answersquaremtosquaremi, 2)
            print(f"your answer is: {roundsquaremtosquaremi}")
            input("")
        elif int(squaremtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square M to Square Yards")
            squaremtosquareyards = input("")
            answersquaremtosquareyards = float(squaremtosquareyards) * 1.196
            roundsquaremtosquareyards = round(answersquaremtosquareyards, 2)
            print(f"your answer is: {roundsquaremtosquareyards}")
            input("")
        elif int(squaremtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square M to Square Feet")
            squaremtosquarefeet = input("")
            answersquaremtosquarefoot = float(squaremtosquarefeet) * 10.764
            roundsquaremtosquarefoot = round(answersquaremtosquarefoot, 2)
            print(f"your answer is: {roundsquaremtosquarefoot}")
            input("")
        elif int(squaremtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square M to Square Inches")
            squaremtosquareinch = input("")
            answersquaremtosquareinches = float(squaremtosquareinch) * 1550
            roundsquaremtosquareinches = round(answersquaremtosquareinches, 2)
            print(f"your answer is: {roundsquaremtosquareinches}")
            input("")
        elif int(squaremtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square M to Hectares")
            squaremtohectare = input("")
            answersquaremtohectare = float(squaremtohectare) / 10000
            roundsquaremtohectare = round(answersquaremtohectare, 2)
            print(f"your answer is: {roundsquaremtohectare}")
            input("")
        elif int(squaremtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acre. Ok, now input how many Square M to Acres")
            squaremtoacre = input("")
            answersquaremtoacre = float(squaremtoacre) / 4047
            roundsquaremtoacre = round(answersquaremtoacre, 2)
            print(f"your answer is: {roundsquaremtoacre}")
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
            roundsquaremitosquarekm = round(answersquaremitosquarekm, 2)
            print(f"your answer is: {roundsquaremitosquarekm}")
            input("")
        elif int(squaremitowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square MI to Square Ms")
            squaremitosquarem = input("")
            answersquaremitosquarem = float(squaremitosquarem) * 2590000
            roundsquaremitosquarem = round(answersquaremitosquarem, 2)
            print(f"your answer is: {roundsquaremitosquarem}") 
            input("") 
        elif int(squaremitowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square MI to Square Yards")
            squaremitosquareyard = input("")
            answersquaremitosquareyard = float(squaremitosquareyard) * 3098000
            roundsquaremitosquareyard = round(answersquaremitosquareyard, 2)
            print(f"your answer is: {roundsquaremitosquareyard}") 
            input("") 
        elif int(squaremitowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square MI to Square Feet")
            squaremitosquarefeet = input("")
            answersquaremitosquarefeet = float(squaremitosquarefeet) * 27880000
            roundsquaremitosquarefeet = round(answersquaremitosquarefeet, 2)
            print(f"your answer is: {roundsquaremitosquarefeet}") 
            input("")
        elif int(squaremitowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square MI to Square Inches")
            squaremitosquareinch = input("")
            answersquaremitosquareinch = float(squaremitosquareinch) * 4014000000
            roundsquaremitosquareinch = round(answersquaremitosquareinch, 2)
            print(f"your answer is: {roundsquaremitosquareinch}") 
            input("")
        elif int(squaremitowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square MI to Hectares")
            squaremitohectare = input("")
            answersquaremitohectare = float(squaremitohectare) * 259
            roundsquaremitohectare = round(answersquaremitohectare, 2)
            print(f"your answer is: {roundsquaremitohectare}") 
            input("")
        elif int(squaremitowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acre. Ok, now input how many Square MI to Acres")
            squaremitoacre = input("")
            answersquaremitoacre = float(squaremitoacre) * 640
            roundsquaremitoacre = round(answersquaremitoacre, 2)
            print(f"your answer is: {roundsquaremitoacre}") 
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
            roundsquareyardstosquarekm = round(answersquareyardstosquarekm, 2)
            print(f"your answer is: {roundsquareyardstosquarekm}")
            input("")
        elif int(squareyardtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square Yards to Square Ms")
            squareyardtosquarem = input("")
            answersquareyardtosquarem = float(squareyardtosquarem) / 1.196
            roundsquareyardtosquarem = round(answersquareyardtosquarem, 2)
            print(f"your answer is: {roundsquareyardtosquarem}") 
            input("") 
        elif int(squareyardtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Miles. Ok, now input how many Square Yards to Square Mi")
            squareyardstosquaremi = input("")
            answersquareyardstosquaremi = float(squareyardstosquaremi) / 3098000
            roundsquareyardstosquaremi = round(answersquareyardstosquaremi, 2)
            print(f"your answer is: {roundsquareyardstosquaremi}") 
            input("") 
        elif int(squareyardtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square Yards to Square Feet")
            squareyardtosquarefeet = input("")
            answersquareyardtosquarefeet = float(squareyardtosquarefeet) * 9
            roundsquareyardtosquarefeet = round(answersquareyardtosquarefeet, 2)
            print(f"your answer is: {roundsquareyardtosquarefeet}") 
            input("")
        elif int(squareyardtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square Yards to Square Inches")
            squareyardtosquareinch = input("")
            answersquareyardtosquareinch = float(squareyardtosquareinch) * 1296
            roundsquareyardtosquareinch = round(answersquareyardtosquareinch, 2)
            print(f"your answer is: {roundsquareyardtosquareinch}") 
            input("")
        elif int(squareyardtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square Yards to Hectares")
            squareyardtohectare = input("")
            answersquareyardtohectare = float(squareyardtohectare) * 259
            roundsquareyardtohectare = round(answersquareyardtohectare, 2)
            print(f"your answer is: {roundsquareyardtohectare}") 
            input("")
        elif int(squareyardtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acres. Ok, now input how many Yards to Acres")
            squareyardtoacre = input("")
            answersquareyardtoacre = float(squareyardtoacre) / 4840
            roundsquareyardtoacre = round(answersquareyardtoacre, 2)
            print(f"your answer is: {roundsquareyardtoacre}") 
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
            roundsquarefoottosquarekm = round(answersquarefoottosquarekm, 2)
            print(f"your answer is: {roundsquarefoottosquarekm}")
            input("")
        elif int(squarefoottowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square Feet to Square Ms")
            squarefoottosquarem = input("")
            answersquarefoottosquarem = float(squarefoottosquarem) / 10.764
            roundsquarefoottosquarem = round(answersquarefoottosquarem, 2)
            print(f"your answer is: {roundsquarefoottosquarem}") 
            input("") 
        elif int(squarefoottowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Miles. Ok, now input how many Square Feet to Square Mi")
            squarefoottosquaremi = input("")
            answersquarefoottosquaremi = float(squarefoottosquaremi) / 27880000
            roundsquarefoottosquaremi = round(answersquarefoottosquaremi, 2)
            print(f"your answer is: {roundsquarefoottosquaremi}") 
            input("") 
        elif int(squarefoottowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square Feet to Square Yards")
            squarefeettosquareyards = input("")
            answersquarefeettosquareyards = float(squarefeettosquareyards) / 9
            roundsquarefeettosquareyards = round(answersquarefeettosquareyards, 2)
            print(f"your answer is: {roundsquarefeettosquareyards}") 
            input("")
        elif int(squarefoottowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Inch. Ok, now input how many Square Feet to Square Inches")
            squarefoottosquareinch = input("")
            answersquarefeettosquareinch = float(squarefoottosquareinch) * 1296
            roundsquarefeettosquareinch = round(answersquarefeettosquareinch, 2)
            print(f"your answer is: {roundsquarefeettosquareinch}") 
            input("")
        elif int(squarefoottowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square Feet to Hectares")
            squarefeettohectare = input("")
            answersquarefeettohectare = float(squarefeettohectare) / 107600
            roundsquarefeettohectare = round(answersquarefeettohectare, 2)
            print(f"your answer is: {roundsquarefeettohectare}") 
            input("")
        elif int(squarefoottowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acres. Ok, now input how many Square Feet to Acres")
            squarefeettoacre = input("")
            answersquarefeettoacre = float(squarefeettoacre) / 43560
            roundsquarefeettoacre = round(answersquarefeettoacre, 2)
            print(f"your answer is: {roundsquarefeettoacre}") 
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
            roundsquareinchtosquarekm = round(answersquareinchtosquarekm , 2)
            print(f"your answer is: {roundsquareinchtosquarekm}")
            input("")
        elif int(squareinchtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square M. Ok, now input how many Square Inches to Square Ms")
            squareinchtosquarem = input("")
            answersquareinchtosquarem = float(squareinchtosquarem) / 1550
            roundsquareinchtosquarem = round(answersquareinchtosquarem, 2)
            print(f"your answer is: {roundsquareinchtosquarem}") 
            input("") 
        elif int(squareinchtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Miles. Ok, now input how many Square Inches to Square Mi")
            squareinchtosquaremi = input("")
            answersquareinchtosquaremi = float(squareinchtosquaremi) / 4014000000
            roundsquareinchtosquaremi = round(answersquareinchtosquaremi, 2)
            print(f"your answer is: {roundsquareinchtosquaremi}") 
            input("") 
        elif int(squareinchtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Yard. Ok, now input how many Square Inches to Square Yards")
            squareinchtosquareyards = input("")
            answersquareinchtosquareyards = float(squareinchtosquareyards) / 1296
            roundsquareinchtosquareyards = round(answersquareinchtosquareyards, 2)
            print(f"your answer is: {roundsquareinchtosquareyards}") 
            input("")
        elif int(squareinchtowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Square Foot. Ok, now input how many Square Inches to Square Feet")
            squareinchtosquarefoot = input("")
            answersquareinchtosquarefoot = float(squareinchtosquarefoot) / 144
            roundsquareinchtosquarefoot = round(answersquareinchtosquarefoot, 2)
            print(f"your answer is: {roundsquareinchtosquarefoot}") 
            input("")
        elif int(squareinchtowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hectare. Ok, now input how many Square Inches to Hectares")
            squareinchtohectare = input("")
            answersquareinchtohectare = float(squareinchtohectare) / 15500000
            roundsquareinchtohectare = round(answersquareinchtohectare, 2)
            print(f"your answer is: {roundsquareinchtohectare}") 
            input("")
        elif int(squareinchtowhat) == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Acres. Ok, now input how many Square Feet to Acres")
            squareinchtoacre = input("")
            answersquareinchtoacre = float(squareinchtoacre) / 6273000
            roundsquareinchtoacre = round(answersquareinchtoacre, 2)
            print(f"your answer is: {roundsquareinchtoacre}") 
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
                roundhectaretosquarekm = round(answerhectaretosquarekm, 2)
                print(f"your answer is: {roundhectaretosquarekm}")
                input("")
            elif int(hectaretowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square M. Ok, now input how many Hectares to Square Ms")
                hectaretosquarem = input("")
                answerhectaretosquarem = float(hectaretosquarem) * 10000
                roundhectaretosquarem = round(answerhectaretosquarem, 2)
                print(f"your answer is: {roundhectaretosquarem}") 
                input("") 
            elif int(hectaretowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Miles. Ok, now input how many Hectares to Square Mi")
                hectaretosquaremi = input("")
                answerhectaretosquaremi = float(hectaretosquaremi) / 259
                roundhectaretosquaremi = round(answerhectaretosquaremi, 2)
                print(f"your answer is: {roundhectaretosquaremi}") 
                input("") 
            elif int(hectaretowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Yard. Ok, now input how many Hectares to Square Yards")
                hectaretosquareyards = input("")
                answerhectaretosquareyards = float(hectaretosquareyards) * 11960
                roundhectaretosquareyards = round(answerhectaretosquareyards, 2)
                print(f"your answer is: {roundhectaretosquareyards}") 
                input("")
            elif int(hectaretowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Foot. Ok, now input how many Hectares to Square Feet")
                hectaretosquarefoot = input("")
                answerhectaretosquarefoot = float(hectaretosquarefoot) * 107600
                roundhectaretosquarefoot = round(answerhectaretosquarefoot, 2)
                print(f"your answer is: {roundhectaretosquarefoot}") 
                input("")
            elif int(hectaretowhat) == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hectare. Ok, now input how many Hectares to Square Inches")
                hectaretosquareinch = input("")
                answerhectaretosquareinch = float(hectaretosquareinch) * 1550000000
                roundhectaretosquareinch = round(answerhectaretosquareinch, 2)
                print(f"your answer is: {roundhectaretosquareinch}") 
                input("")
            elif int(hectaretowhat) == 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Acres. Ok, now input how many Square Feet to Acres")
                hectaretoacre = input("")
                answerhectaretoacre = float(hectaretoacre) * 2.471
                roundhectaretoacre = round(answerhectaretoacre, 2)
                print(f"your answer is: {roundhectaretoacre}") 
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
                roundacretosquarekm = round(answeracretosquarekm, 2)
                print(f"your answer is: {roundacretosquarekm}")
                input("")
            elif int(acretowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square M. Ok, now input how many acres to Square Ms")
                acretosquarem = input("")
                answeracretosquarem = float(acretosquarem) / 4047
                roundacretosquarem = round(answeracretosquarem, 2)
                print(f"your answer is: {roundacretosquarem}") 
                input("") 
            elif int(acretowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Miles. Ok, now input how many acres to Square Mi")
                acretosquaremi = input("")
                answeracretosquaremi = float(acretosquaremi) / 640
                roundacretosquaremi = round(answeracretosquaremi, 2)
                print(f"your answer is: {roundacretosquaremi}") 
                input("") 
            elif int(acretowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Yard. Ok, now input how many acres to Square Yards")
                acretosquareyards = input("")
                answeracretosquareyards = float(acretosquareyards) * 4840
                roundacretosquareyards = round(answeracretosquareyards, 2)
                print(f"your answer is: {roundacretosquareyards}") 
                input("")
            elif int(acretowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Square Foot. Ok, now input how many acres to Square Feet")
                acretosquarefoot = input("")
                answeracretosquarefoot = float(acretosquarefoot) * 43560
                roundacretosquarefoot = round(answeracretosquarefoot, 2)
                print(f"your answer is: {roundacretosquarefoot}") 
                input("")
            elif int(acretowhat) == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("acre. Ok, now input how many Acres to Square Inches")
                acretosquareinch = input("")
                answeracretosquareinch = float(acretosquareinch) / 6273000
                roundacretosquareinch = round(answeracretosquareinch, 2)
                print(f"your answer is: {roundacretosquareinch}") 
                input("")
            elif int(acretowhat) == 7:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Hectares. Ok, now input how many Acres to Hectares")
                acretohectare = input("")
                answeracretohectare = float(acretohectare) / 2.471
                roundacretohectare = round(answeracretohectare, 2)
                print(f"your answer is: {roundacretohectare}") 
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
            roundmstosec = round(answermstosec, 2)
            print(f"your answer is: {roundmstosec}")
            input("")
        elif int(mstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Minutes. Ok, now input how many Milliseconds to Minutes")
            mstomin = input("")
            answermstomin = float(mstomin) / 60000
            roundmstomin = round(answermstomin, 2)
            print(f"your answer is {roundmstomin}")
            input("")
        elif int(mstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hours. Ok, now input how many Milliseconds to Hours")
            mstohour = input("")
            answermstohour = float(mstohour) / 3600000
            roundmstohour = round(answermstohour, 2)
            print(f"your answer is {roundmstohour}")
            input("")
        elif int(mstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Days. Ok, now input how many Milliseconds to Days")
            mstodays = input("")
            answermstodays = float(mstodays) / 86400000
            roundmstodays = round(answermstodays, 2)
            print(f"your answer is: {roundmstodays}")
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
            roundsectoms = round(answersectoms, 2)
            print(f"your answer is: {roundsectoms}")
            input("")
        elif int(sectowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Minutes. Ok, now input how many Seconds to Minutes")
            sectomins = input("")
            answersectomins = float(sectomins) / 60 
            roundsectomins = round(answersectomins, 2)
            print(f"your answer is: {roundsectomins}")
            input("")
        elif int(sectowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Hours. Ok, now input how many Seconds to Hours")
            sectohours = input("")
            answersectohours = float(sectohours) / 3600 
            roundsectohours = round(answersectohours, 2)
            print(f"your answer is: {roundsectohours}")
            input("")
        elif int(sectowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Days. Ok, now input how many Seconds to Days")
            sectodays = input("")
            answersectodays = float(sectodays) / 86400
            roundsectodays = round(answersectodays, 2)
            print(f"your answer is: {roundsectodays}")
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
           roundmintoms = round(answermintoms, 2)
           print(f"your answer is: {roundmintoms}")
           input("")
       elif int(mintowhat) == 2:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Seconds. Ok, now input how many Minutes to Seconds")
           mintosec = input("")
           answermintosec = float(mintosec) * 60
           roundmintosec = round(answermintosec, 2)
           print(f"your answer is: {roundmintosec}")
           input("")
       elif int(mintowhat) == 3:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Hours. Ok, now input how many Minutes to Hours")
           mintohr = input("")
           answermintohr = float(mintohr) / 60
           roundmintohr = round(answermintohr, 2)
           print(f"your answer is: {roundmintohr}")
           input("")
       elif int(mintowhat) == 4:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Days. Ok, now input how many Minutes to Days")
           mintodays = input("")
           answermintodays = float(mintodays) / 1440
           roundmintodays = round(answermintodays, 2)
           print(f"your answer is: {roundmintodays}")
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
           roundhrtoms = round(answerhrtoms, 2)
           print(f"your answer is: {roundhrtoms}")
           input("")
        elif int(hrtowhat) == 2:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Seconds. Ok, now input how many Hours to Seconds")
           hrtosec = input("")
           answerhrtosec = float(hrtosec) * 3600
           roundhrtosec = round(answerhrtosec, 2)
           print(f"your answer is: {roundhrtosec}")
           input("")
        elif int(hrtowhat) == 3:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Minutes. Ok, now input how many Hours to Minutes")
           hrtomin = input("")
           answerhrtomin = float(hrtomin) * 60 
           roundhrtomin = round(answerhrtomin, 2)
           print(f"your answer is: {roundhrtomin}")
           input("")
        elif int(hrtowhat) == 4:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Days. Ok, now input how many Hours to Days")
           hrtodays = input("")
           answerhrtodays = float(hrtodays) / 24 
           roundhrtodays = round(answerhrtodays, 2)
           print(f"your answer is: {roundhrtodays}")
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
           rounddaystoms = round(answerdaystoms, 2)
           print(f"your answer is: {rounddaystoms}")
           input("")
        elif int(daytowhat) == 2:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Seconds. Ok, now input how many Days to Seconds")
           daystosec = input("")
           answerdaystosec = float(daystosec) * 86400
           rounddaystosec = round(answerdaystosec, 2)
           print(f"your answer is: {rounddaystosec}")
           input("")
        elif int(daytowhat) == 3:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Minutes. Ok, now input how many Days to Minutes")
           daystomin = input("")
           answerdaystomin = float(daystomin) * 1440
           rounddaystomin = round(answerdaystomin, 2)
           print(f"your answer is: {rounddaystomin}")
           input("")
        elif int(daytowhat) == 4:
           os.system('cls' if os.name == 'nt' else 'clear')
           print("Hours. Ok, now input how many Days to Hours")
           daystohr = input("")
           answerdaystohr = float(daystohr) / 24
           rounddaystohr = round(answerdaystohr, 2)
           print(f"your answer is: {rounddaystohr}")
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
