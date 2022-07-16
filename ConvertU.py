# Converter for pretty much anything... Mass, Digital Storage, Length, Speed, Temperature. 
# Currency might come in the future but not right now....
# Do not steal please just don't lol
# No, Seriously this took me like 20 hours


import os
from select import select 
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
            print("your answer is: " + str(answertonstokilograms))
        if int(tonstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Grams. Ok, input how many Tons to Grams")
            tonstograms = input("")
            answertonstograms = float(tonstograms) * 907200
            print("your answer is: " + str(answertonstograms))
        if int(tonstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Milligrams. Ok, input how many Tons to Milligrams")
            tonstomilligrams = input("")
            answertonstomilligrams = float(tonstomilligrams) * 970200000
            print("your answer is: " + str(answertonstomilligrams))
        if int(tonstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Pounds. Ok, input how many Tons to Pounds")
            tonstopounds = input("")
            answertonstopounds = float(tonstopounds) * 2000
            print("your answer is: " + str(answertonstopounds))
        if int(tonstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ounces. Ok, input how many Tons to Ounces")
            tonstoounces = input("")
            answertonstoounces = float(tonstoounces) * 32000
            print("your answer is: " + str(answertonstoounces))
    if int(massoption) == 2:
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
                print("your answer is: " + str(answerkilogramstotons))
        if int(kilogramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Grams. Ok, input how many Kilograms to Grams")
                kilogramstograms = input("")
                answerkilogramstograms = float(kilogramstograms) * 1000
                print("your answer is: " + str(answerkilogramstograms))
        if int(kilogramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Milligrams. Ok, input how many Kilograms to Milligrams")
                kilogramstomilligrams = input("")
                answerkilogramstomilligrams = float(kilogramstomilligrams) * 1000000
                print("your answer is: " + str(answerkilogramstomilligrams))
        if int(kilogramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Pounds. Ok, input how many Kilograms to Pounds")
                kilogramstopounds = input("")
                answerkilogramstopounds = float(kilogramstopounds) * 2.205
                print("your answer is: " + str(answerkilogramstopounds))
        if int(kilogramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print("Ounces. Ok, input how many Kilograms to Ounces")
                kilogramstoounces = input("")
                answerkilogramstoounces = float(kilogramstoounces) * 35.274
                print("your answer is: " + str(answerkilogramstoounces))
    if int(massoption) == 3:
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
                print("your answer is: " + str(answergramstotons))
        if int(gramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Grams to Kilograms")
                gramstokilograms = input("")
                answergramstokilograms = float(gramstokilograms) / 1000
                print("your answer is: " + str(answergramstokilograms))
        if int(gramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Grams to Milligrams")
                gramstomilligrams = input("")
                answergramstomilligrams = float(gramstomilligrams) * 1000
                print("your answer is: " + str(answergramstomilligrams))
        if int(gramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many Grams to Pounds")
                gramstopounds = input("")
                answergramstopounds = float(gramstopounds) / 453.6
                print("your answer is: " + str(answergramstopounds))
        if int(gramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many Grams to Ounces")
                gramstoounces = input("")
                answergramstoounces = float(gramstoounces) / 28.35
                print("your answer is: " + str(answergramstoounces))
    if int(massoption) == 4:
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
                print("your answer is: " + str(answermilligramstotons))
        if int(milligramstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Milligrams to Kilograms")
                milligramstokilograms = input("")
                answermilligramstokilograms = float(milligramstokilograms) / 1000000
                print("your answer is: " + str(answermilligramstokilograms))
        if int(milligramstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Milligrams to Grams")
                milligramstograms = input("")
                answermilligramstograms = float(milligramstograms) / 1000
                print("your answer is: " + str(answermilligramstograms))
        if int(milligramstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many milligrams to Pounds")
                milligramstopounds = input("")
                answermilligramstopounds = float(gramstopounds) / 453600
                print("your answer is: " + str(answermilligramstopounds))
        if int(milligramstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many milligrams to Ounces")
                milligramstoounces = input("")
                answermilligramstoounces = float(milligramstoounces) / 28350
                print("your answer is: " + str(answermilligramstoounces))
    if int(massoption) == 5:
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
                print("your answer is: " + str(answerpoundstotons))
        if int(poundstowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Pounds to Kilograms")
                poundstokilograms = input("")
                answerpoundstokilograms = float(poundstokilograms) / 2.205
                print("your answer is: " + str(answerpoundstokilograms))
        if int(poundstowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Pounds to Grams")
                poundstograms = input("")
                answerpoundstograms = float(poundstograms) * 453.6
                print("your answer is: " + str(answerpoundstograms))
        if int(poundstowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Pounds to Milligrams")
                poundstomilligrams = input("")
                answerpoundstomilligrams = float(poundstomilligrams) * 453600
                print("your answer is: " + str(answerpoundstomilligrams))
        if int(poundstowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ounces. Ok, input how many Pounds to Ounces")
                poundstoounces = input("")
                answerpoundstoounces = float(poundstoounces) * 16
                print("your answer is: " + str(answerpoundstoounces)) 
    if int(massoption) == 6:
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
                print("your answer is " + str(answerouncestotons))
        if int(ouncestowhat) == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Kilograms. Ok, input how many Ounces to Kilograms")
                ouncestokilograms = input("")
                answerouncestokilograms = float(ouncestokilograms) / 35.274
                print("your answer is " + str(answerouncestokilograms))
        if int(ouncestowhat) == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Grams. Ok, input how many Ounces to Grams")
                ouncestograms = input("")
                answerouncestograms = float(ouncestograms) * 28.35
                print("your answer is: " + str(answerouncestograms))
        if int(ouncestowhat) == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Milligrams. Ok, input how many Ounces to Milligrams")
                ouncestomilligrams = input("")
                answerouncestomilligrams = float(ouncestomilligrams) * 28350
                print("your answer is: " + str(answerouncestomilligrams))
        if int(ouncestowhat) == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Pounds. Ok, input how many Ounces to Pounds")
                ouncestopounds = input("")
                answerouncestopounds = float(ouncestopounds) / 16
                print("your answer is: " + str(answerouncestopounds))

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
            print("your answer is: " + str(answerbytestokilobytes))
        if int(bytestowhat) == 2: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, input how many Bytes to Megabytes")
            bytestomegabytes = input("")
            answerbytestomegabytes = float(bytestomegabytes) / 1000000
            print("your answer is: " + str(answerbytestomegabytes))
        if int(bytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabyte. Ok, input how many Bytes to Gigabytes")
            bytestogigabytes = input("")
            answerbytestogigabytes = float(bytestogigabytes) / 1000000000 
            print("your answer is: " + str(answerbytestogigabytes))
        if int(bytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, input how many Bytes to Terabytes")
            bytestoterabytes = input("")
            answerbytestoterabytes = float(bytestoterabytes) / 1000000000000
            print("your answer is: " + str(answerbytestogigabytes))
    if int(storageoption) == 2:
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
            print("your answer is: " + str(answerkilobytestobytes))
        if int(kilobytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, input how many Kilobytes to Megabytes")
            kilobytestomegabytes = input("")
            answerkilobytestomegabytes = float(kilobytestomegabytes) / 1000
            print("your answer is: " + str(answerkilobytestomegabytes))
        if int(kilobytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, input how many Kilobytes to Gigabytes")
            kilobytestogigabytes = input("")
            answerkilobytestogigabytes = float(kilobytestogigabytes) / 1000000
            print("your answer is: " + str(answerkilobytestogigabytes))
        if int(kilobytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabytes. Ok, input how many Kilobytes to Terabytes")
            kilobytestoterabytes = input("")
            answerkilobytestoterabytes = float(kilobytestoterabytes) / 1000000000
            print("your answer is: " + str(answerkilobytestoterabytes))
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
            print("your answer is: " + str(answergigabytestobytes))
        if int(gigabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Gigabytes to Kilobytes")
            gigabytestokilobytes = input("")
            answergigabytestokilobytes = float(gigabytestokilobytes) * 1000000
            print("your answer is: " + str(answergigabytestokilobytes))
        if int(gigabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, now input how many Gigabytes to Megabytes")
            gigabytestomegabytes = input("")
            answergigabytestomegabytes = float(gigabytestomegabytes) * 1000
            print("your answer is: " + str(answergigabytestomegabytes))
        if int(gigabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, now input how many Gigabytes to Terabytes")
            gigabytestoterabytes = input("")
            answergigabytestoterabytes = float(gigabytestoterabytes) / 1000
            print("your answer is: " + str(answergigabytestoterabytes))
    if int(storageoption) == 4:
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
            print("your answer is: " + str(answermegabytestobytes))
        if int(megabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Megabytes to Kilobytes")
            megabytestokilobytes = input("")
            answermegabytestokilobytes = float(megabytestokilobytes) * 1000
            print("your answer is: " + str(answermegabytestokilobytes))
        if int(megabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, now input how many Megabytes to Gigabytes")
            megabytestogigabytes = input("")
            answermegabytestogigabytes = float(megabytestogigabytes) / 1000
            print("your answer is: " + str(answermegabytestogigabytes))
        if int(megabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terabyte. Ok, now input how many Megabytes to Terabytes")
            megabytestoterabytes = input("")
            answermegabytestoterabytes = float(megabytestoterabytes) / 1000000
    if int(storageoption) == 4:
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
            print("your answer is: " + str(answerterabytestobytes))
        if int(terabytestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilobytes. Ok, now input how many Terabytes to Kilobytes")
            terabytestokilobytes = input("")
            answerterabytestokilobytes = float(terabytestokilobytes) * 1000000000
            print("your answer is: " + str(answerterabytestokilobytes))
        if int(terabytestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Gigabytes. Ok, now input how many Terabytes to Gigabytes")
            terabytestogigabytes = input("")
            answerterabytestogigabytes = float(terabytestogigabytes) * 1000 
            print("your answer is: " + str(answerterabytestogigabytes))
        if int(terabytestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Megabytes. Ok, now input how many Terabytes to Megabytes.")
            terabytestomegabytes = input("")
            answerterabytestomegabytes = float(terabytestomegabytes) * 1000000
            print("your answer is: " + str(answerterabytestomegabytes))


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
            print("your answer is: " + str(answerfeettometres))
        if int(feettowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Feet to Kilometres")
            feettokilometres = input("")
            answerfeettokilometres = float(feettokilometres) / 3281
            print("your answer is: " + str(answerfeettokilometres))
        if int(feettowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Feet to Centimetres")
            feettocentimetres = input("")
            answerfeettocentimetres = float(feettocentimetres) * 30.48
            print("your answer is: "  + str(answerfeettocentimetres))
        if int(feettowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Feet to Millimetres")
            feettomillimetres = input("")
            answerfeettomillimetres = float(feettomillimetres) * 304.8
            print("your answer is: " + str(answerfeettomillimetres))
        if int(feettowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Feet to Yards")
            feettoyard = input("")
            answerfeettoyard = float(feettoyard) / 3
            print("your answer is: " + str(answerfeettoyard))
        if int(feettowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Feet to Inches")
            feettoinches = input("")
            answerfeettoinches = float(feettoinches) * 12
            print("your answer is: " + str(answerfeettoinches))
    if int(lengthoption) == 2:
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
            print("your answer is: " + str(answermetrestofeet))
        if int(metrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Metres to Kilometres")
            metrestokilometres = input("")
            answermetrestokilometres = float(metrestokilometres) / 1000
            print("your answer is: " + str(answermetrestokilometres))
        if int(metrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Metres to Centimetres")
            metrestocentimetres = input("")
            answermetrestocentimetres = float(metrestocentimetres) * 100
            print("your answer is: " + str(answermetrestocentimetres))
        if int(metrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Metres to Millimetres")
            metrestomillimetres = input("")
            answermetrestomillimetres = float(metrestomillimetres) * 1000
            print("your answer is: " + str(metrestomillimetres))
        if int(metrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Metres to Yards")
            metrestoyards = input("")
            answermetrestoyards = float(metrestoyards) * 1.094
            print("your answer is: " + str(answermetrestoyards))
        if int(metrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Metres to Inches")
            metrestoinches = input("")
            answermetrestoinches = float(metrestoinches) * 39.37
            print("your answer is: " + str(answermetrestoinches))
    if int(lengthoption) == 3:
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
            print("your answer is: " + str(answerkilometrestofeet))
        if int(kilometrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Kilometres to Metres")
            kilometrestometres = input("")
            answerkilometrestometres = float(kilometrestometres) * 1000 
            print("your answer is: " + str(answerkilometrestometres))
        if int(kilometrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Kilometres to Centimetres")
            kilometrestocentimetres = input("")
            answerkilometrestocentimetres = float(kilometrestocentimetres) * 100000 
            print("your answer is: " + str(answerkilometrestocentimetres))
        if int(kilometrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Kilometres to Millimetres")
            kilometrestocentimetres = input("")
            answerkilometrestomillimetres = float(kilometrestocentimetres) * 1000000
            print("your answer is: " + str(answerkilometrestomillimetres))
        if int(kilometrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Kilometres to Yards")
            kilometrestoyards = input("")
            answerkilometrestoyards = float(kilometrestoyards) * 1094
            print("your answer is: " + str(answerkilometrestoyards))
        if int(kilometrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Kilometres to Inches")
            kilometrestoinches = input("")
            answerkilometrestoinches = float(kilometrestoinches) * 39370 
            print("your answer is: " + str(answerkilometrestoinches))
    if int(lengthoption) == 4:
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
            print("your answer is: " + str(answercentimetrestofeet))
        if int(centimetrestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Centimetres to Metres")
            centimetrestometres = input("")
            answercentimetrestometres = float(centimetrestometres) / 100
            print('your answer is: ' + str(answercentimetrestometres))
        if int(centimetrestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Centimetres to Kilometres")
            centimetrestokilometres = input("")
            answercentimetrestokilometres = float(centimetrestokilometres) / 1000000
            print("your answer is: " + str(answercentimetrestokilometres))
        if int(centimetrestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Centimetres to Millimetres")
            centimetrestomillimetres = input("")
            answercentimetrestomillimetres = float(centimetrestomillimetres) * 10 
            print("your answer is: " + str(answercentimetrestomillimetres))
        if int(centimetrestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok. Now input how many Centimetres to Yards")
            centimetrestoyards = input("")
            answercentimetrestoyards = float(centimetrestoyards) / 91.44
            print("your answer is: " + str(answercentimetrestoyards))
        if int(centimetrestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Centimetres to Inches")
            centimetrestoinches = input("")
            answercentimetrestoinches = float(centimetrestoinches) / 2.54
            print("your answer is: " + str(answercentimetrestoinches))
    if int(lengthoption) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Millimetres. Ok, now what do you want to convert that to?")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Feet\n2. Metre\n3. Kilometre\n4. Centimetre\n5. Yard\n6. Inch")
        millimetrestowhat = input("Select a number 1-6 for the corresponding unit: ")
        if int(milligramstowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Feet. Ok, now input how many Millimetres to Feet")
            millimetrestofeet = input("")
            answermillimetrestofeet = float(millimetrestofeet) / 304.8
            print("your answer is: " + str(answermillimetrestofeet))
        if int(milligramstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. OK, now input how many Millimetres to Metres")
            millimetrestometres = input("")
            answermillimetrestometres = float(millimetrestometres) / 1000
            print("your answer is: " + str(answermillimetrestometres))
        if int(milligramstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Millimetres to Kilometres")
            millimetrestokilometres = input("")
            answermillimetrestokilometres = float(millimetrestokilometres) / 1000000
            print("your answer is: " + str(answermillimetrestokilometres))
        if int(milligramstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Millimetres to Centimetres")
            millimetrestocentimetres = input("")
            answermillimetrestocentimetres = float(millimetrestocentimetres) / 10
            print("your answer is: " + str(answermillimetrestocentimetres))
        if int(milligramstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Millimetres to Yards")
            millimetrestoyards = input("")
            answermillimetrestoyards = float(millimetrestoyards) / 914.4
            print("your answer is: " + str(answermillimetrestoyards))
        if int(milligramstowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Millimetres to Inches")
            millimetrestoinches = input("")
            answermillimetrestoinches = float(millimetrestoinches) / 25.4
            print("your answer is: " + str(answermillimetrestoinches))
    if int(lengthoption) == 6:
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
            print("your answer is: " + str(answeryardstofeet))
        if int(yardstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Yards to Metres")
            yardstometres = input("")
            answeryardstometres = float(yardstometres) / 1.094
            print("your answer is: " + str(answeryardstometres))
        if int(yardstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Yards to Kilometres")
            yardstokilometres = input("")
            answeryardstokilometres = float(yardstokilometres) / 1094
            print("your answer is: " + str(answeryardstokilometres))
        if int(yardstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Yards to Centimetres")
            yardstocentimetres = input("")
            answeryardstocentimetres = float(yardstocentimetres) * 91.44
            print("your answer is: " + str(answeryardstocentimetres))
        if int(yardstowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Yards to Millimetres")
            yardstomillimetres = input("")
            answeryardstomillimetres = float(yardstomillimetres) * 914.44
            print("your answer is: " + str(answeryardstomillimetres))
        if int(yardstowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Inches. Ok, now input how many Yards to Inches")
            yardstoinches = input("")
            answeryardstoinches = float(yardstoinches) * 36
            print("your answer is: " + str(answeryardstoinches))
    if int(lengthoption) == 7:
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
            print("your answer is: " + str(answerinchestofeet))
        if int(inchestowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Metres. Ok, now input how many Inches to Metres")
            inchestometres = input("")
            answerinchestometres = float(inchestometres) / 39.37
            print("your answer is: " + str(answerinchestometres))
        if int(inchestowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kilometres. Ok, now input how many Inches to Kilometres")
            inchestokilometres = input("")
            answerinchestokilometres = float(inchestokilometres) / 39370
            print("your answer is: " + str(answerinchestokilometres))
        if int(inchestowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Centimetres. Ok, now input how many Inches to Centimetres")
            inchestocentimetres = input("")
            answerinchestocentimetres = float(inchestocentimetres) * 2.54
            print("your answer is: " + str(answerinchestocentimetres))
        if int(inchestowhat) == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Millimetres. Ok, now input how many Inches to Millimetres")
            inchestomillimetres = input("")
            answerinchestomillimetres = float(inchestomillimetres) * 25.4
            print("your answer is: " + str(answerinchestomillimetres))
        if int(inchestowhat) == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Yards. Ok, now input how many Inches to Yards")
            inchestoyards = input("")
            answerinchestoyards = float(inchestoyards) / 36
            print("your answer is: " + str(answerinchestoyards))

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
            print("your answer is: " + str(answermphtokph))
        if int(mphtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many MPH to FPS")
            mphtofps = input("")
            answermphtofps = float(mphtofps) * 1.467
            print("your answer is: " + str(answermphtofps))
        if int(mphtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many MPH to MPS")
            mphtomps = input("")
            answermphtomps = float(mphtomps) * 2.237
            print("your answer is: " + str(answermphtomps))
        if int(mphtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many MPH to Knots")
            mphtoknots = input("")
            answermphtoknots = float(mphtoknots) / 1.151
            print("your answer is: " + str(mphtoknots))
    if int(speedoption) == 2:
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
            print("your answer is: " + str(answerkphtomph))
        if int(kphtowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many KPH to FPS")
            kphtofps = input("")
            answerkphtofps = float(kphtofps) / 1.097
            print("your answer is: " + str(answerkphtofps))
        if int(kphtowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many KPH to MPS")
            kphtomps = input("")
            answerkphtomps = float(kphtomps) / 3.6 
            print("your answer is: " + str(answerkphtomps))
        if int(kphtowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many KPH to Knots")
            kphtoknots = input("")
            answerkphtoknots = float(kphtoknots) / 1.852
            print("your answer is: " + str(answerkphtoknots))
    if int(speedoption) == 3:
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
            print("your answer is: " + str(answerfpstomph))
        if int(fpstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many FPS to KPH")
            fpstokph = input("")
            answerfpstokph = float(fpstokph) / 1.097
            print("your answer is: " + str(answerfpstokph))
        if int(fpstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many FPS to MPS")
            fpstomps = input("")
            answerfpstomps = float(fpstomps) / 3.281 
            print("your answer is: " + str(answerfpstomps))
        if int(fpstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many FPS to Knots")
            fpstoknots = input("")
            answerfpstoknots = float(fpstoknots) / 1.688
            print("your answer is: " + str(answerfpstoknots))
    if int(speedoption) == 4:
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
            print("your answer is " + str(answermpstomph))
        if int(mpstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many MPS to KPH")
            mpstokph = input("")
            answermpstokph = float(mpstokph)
            print("your answer is: " + str(answermpstokph))
        if int(mpstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many MPS to FPS")
            mpstofps = input("")
            answermpstofps = float(mpstofps) * 3.281
            print("your answer is: " + str(answermpstofps))
        if int(mpstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Knots. Ok, now input how many MPS to Knots")
            mpstoknots = input("")
            answermpstoknots = float(mpstoknots) * 1.944
            print("your answer is: " + str(answermpstoknots))
    if int(speedoption) == 5:
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
            print("your answer is: " + str(answerknotstomph))
        if int(knotstowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("KPH. Ok, now input how many Knots to KPH")
            knotstokph = input("")
            answerknotstokph = float(knotstokph) * 1.852
            print("your answer is: " + str(answerknotstokph))
        if int(knotstowhat) == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("FPS. Ok, now input how many Knots to FPS")
            knotstofps = input("")
            answerknotstofps = float(knotstofps) * 1.688
            print("your answer is: " + str(answerknotstofps))
        if int(knotstowhat) == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("MPS. Ok, now input how many Knots to MPS")
            knotstomps = input("")
            answerknotstomps = float(knotstomps) / 1.944
            print("your answer is: " + str(answerknotstomps))

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
            print("your answer is: " + str(answercelsiustofahrenheit))
        if int(celsiustowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kelvin. Ok, now input how many Celsius to Kelvin")
            celsiustokelvin = input("")
            answercelsiustokelvin = float(celsiustokelvin) + 273.15
            print("your answer is: " + str(answercelsiustokelvin))
    if int(tempoption) == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Fahrenheit. Ok, Now what do you want to convert that to?") 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Celsius\n2. Kelvin")
        fahrenheittowhat = input("Select a number 1-2 for the corresponding unit: ")
        if int(celsiustowhat) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Celsius. Ok, now input how many Fahrenheit to Celsius")
            fahrenheittocelsius = input("")
            answerfahrenheittocelsius = float(fahrenheittocelsius) - 32 * 0.5556
            print("your answer is: " + str(answerfahrenheittocelsius))
        if int(celsiustowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Kelvin. Ok, now input how many Fahrenheit to Kelvin")
            fahrenheittokelvin = input("")
            answerfahrenheittokelvin = float(fahrenheittokelvin) + 459.67 * 0.5556
            print("your answer is: " + str(answerfahrenheittokelvin))
    if int(tempoption) == 3:
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
            print("your answer is: " + str(answerkelvintocelsius))
        if int(kelvintowhat) == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Fahrenheit. Ok, now input how many Kelvin to Fahrenheit")
            kelvintofahrenheit = input("")
            answerkelvintofahrenheit = float(kelvintofahrenheit) - 273.15 * 1.8 + 32
            print("your answer is: " + str(answerkelvintofahrenheit))

print("Welcome to ConvertU")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("1. Mass\n2. Digital Storage\n3. Length\n4. Speed\n5. Temperature")
option1 = input("Select a number 1-5 for the corresponding unit type: ")
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
