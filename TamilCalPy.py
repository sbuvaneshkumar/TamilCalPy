# -*- coding: utf-8 -*-
while True:
    print("தேர்ந்தெடு:")
    print("கூட்ட 'கூட்டு' என தட்டச்சிடவும்")
    print("கழிக்க 'கழி; ' தட்டச்சிடவும்")
    print("பெருக்க 'பெருக்கு' என தட்டச்சிடவும்")
    print("வகுக்க 'வகு' என தட்டச்சிடவும்")
    print("வெளியேற 'வெளி' என தட்டச்சிடவும்")
    user_input = input(":")

    if user_input == "வெளி":
        break
    elif user_input == "கூட்டு":
        num1 =float(input("ஒரு எண்ணை உள்ளிடு:"))
        num2 =float(input("மற்றொரு எண்ணை உள்ளிடு:"))
        result = str(num1 + num2)
        print("விடை " + result)
    elif user_input == "கழி":
        num1 =float(input("ஒரு எண்ணை உள்ளிடு:"))
        num2 =float(input("மற்றொரு எண்ணை உள்ளிடு:"))
        result = str(num1 - num2)
        print("விடை " + result)
    elif user_input == "பெருக்கு":
        num1 =float(input("ஒரு எண்ணை உள்ளிடு:"))
        num2 =float(input("மற்றொரு எண்ணை உள்ளிடு:"))
        result = str(num1 * num2)
        print("விடை " + result)
    elif user_input == "வகு":
        num1 =float(input("ஒரு எண்ணை உள்ளிடு:"))
        num2 =float(input("மற்றொரு எண்ணை உள்ளிடு:"))
        result = str(num1 / num2)
        print("விடை " + result)
    else:       
        print("தவறான உள்ளீடு")
