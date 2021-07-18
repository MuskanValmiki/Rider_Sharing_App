import random 
import json
print("***********************Hii this is utter pradesh uber cab**************************")
name = input("enter your name = ")
print("welcome to my uber app",name)
rider = ["Yogesh","Aditya","Arjun","Abhishek","sunny"]

def booking():
    limit = int(input("enter how much ride we have to do for you = "))
    if limit == 0:
        print("you dont want to visit ok")
    else:
        index = 1
        total = 0
        dict = {}
        while index <= limit:
            cab_no = input("enter your cab number = ")
            distance = int(input("enter how much far you will go distance in km = "))
            place = input("enter any place name where you want to go = ")
            driver = random.choice(rider)
            print(driver,"this driver is available")
            if driver in rider:
                print("you choice",driver,"driver","he is on that distination",place)
                money = distance*5
                total += money
                print("For",index,"ride money = ",money)
            else:
                print("driver is not available")
            print(limit,"ride your total amount = ",total)
            dict[driver] = money 
            index += 1
        with open("driving data.json","w+") as file:
            json.dump(dict,file)
        print(dict,"this is all ride data")
        max = 0
        for key in dict:
            if dict[key] > max:
                max = dict[key]
                driver = key
        print(driver,"this driver is earn more money",max)

def cancel():
    with open("driving data.json","r") as file1:
        data = json.load(file1)
        print(data)
        driver = input("enter your driver which driver you will cansel = ")
        del data[driver]
        print(data)     
        print("thanks for visit my Rider sharing app  and you cancel the cab safely.")

def main():
    options = int(input("if you put 1 so book the cab and if you put 2 so you cancel the cab = "))
    if options == 1:
        booking()
        print("thanks to visit my cab service ","\U0001F929")
    else:
        cancel()
main()