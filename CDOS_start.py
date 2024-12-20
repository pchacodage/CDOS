print("Colony Developement")
print("CDOS is starting")
#put start code here
import time as tm
#import math
import random as rnd
import logging
LOGGER: logging.Logger = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)
file = ""
def shutdown():
    LOGGER.info("system downing ...")
    tm.sleep (3)
    LOGGER.info("system down !")
    tm.sleep(1/2)
    exit()

modeinput = 0
session_number = 1 
sessions = ["general"]
passwords = ["No passwords"]
if session_number < 1:
    session = input("wich session do you want to start (please enter the identifiant of session) ?")
else:
    mode = input("wich mode do you want ? (N/G)")
    if mode == "N":
        mode = ("admin")
        sessionchoosed = ("general")
        modeinput = 1
    elif mode == "G":
        mode = ("guest")
        sessionchoosed = ("guest")
        modeinput = 1
    else:
         LOGGER.info("critical error : answer not availaible")
         tm.sleep(3)
         exit()

#end of starting
LOGGER.info("CDOS is started")
while True:
    order = input(LOGGER.info(f"computer/{sessionchoosed}>"))
    if order == "calculator":
        easter_egg = rnd.randint(1,100)
        LOGGER.info(easter_egg)
        if easter_egg == 11:
            LOGGER.info("your computer IS a calculator")
        first_number = int(input("please enter the 1st number"))
        sign = input("please enter the sign :")
        second_number = int(input("please enter the 2nd number"))
        if sign == "/":
            result = (first_number/second_number)
        else:
            if sign == "*":
                result = (first_number*second_number)
            else:
                if sign == "-":
                    result = (first_number-second_number)
                else:
                    if sign == "+":
                        result = (first_number + second_number)
        LOGGER.info("the result is",result)
    if order == "help":
        LOGGER.info("here's the list of all the commands: \n calculator : a very basic calculator \n help : you know \n rnd : : choose a random number between 2 numbers you choose\n clock : an app with a timer and a calendar for day")
    if order == "rnd":
        first_limit = input ("please enter the first limit")
        try:
            int(first_limit)
        except:
            ("critical error, please enter a number")
            continue
        second_limit = input ("please enter the second limit")
        try:
            int(second_limit)
        except:
            LOGGER.info("critical error, please enter a valid number")
            continue
        result = rnd.randint(float(first_limit),float(second_limit))
        LOGGER.info("le nombre est ",result)
    if order == "settings":
            if mode == ("guest"):
                LOGGER.info("error : you are not admin !")
            elif mode == "admin":
                settings = 1
                while settings == 1:
                    order_sittings = input("what do you want ?")
                    if order_sittings == ("help"):
                        LOGGER.info("here's the list of the commands : help : you know \n sessions : for create, delete and modify the sessions")
                    else:
                        if order_sittings == ("sessions"):
                            if session_number == 1:
                                session_mode_order = input("Currently, the mode admin/guest sessions is active, do you want to change it ? (Y/N)")
                                try:
                                    str(session_mode_order)
                                except:
                                    LOGGER.info("critical error, answer is not good")
                                    seetings = 0
                                if session_mode_order == "Y":
                                    session_mode = 1
                                    while session_mode == 1:
                                        session_mode_order = input("What do you want to do ? (Create : C, Modify : M, Delete : D)")
                                        if session_mode_order == "exit()":
                                            session_mode = 0
                                        else:
                                            if session_mode_order == "C":
                                                session_number += 1
                                                session = sessions.extend(input ("Please enter the new identifiant")+",")
                                                passwords = passwords.extend(input ("Please enter the new password")+",")
                                            else:
                                                if session_mode_order == "M":
                                                    session_to_modify = input("Wich session do you want to modify ?")
                                                    if session_to_modify in session:
                                                        thing_to_modify = input("what do you want to modify ? (Password : P, Identifiant : I")
                                                        if thing_to_modify == "P":
                                                            position_session_to_modify = sessions.find()
                                                            number_of_function = 0
                                                            for session_to_modify in [sessions]:
                                                                if session_to_modify == sessions:
                                                                   password_to_modify = passwords[number_of_function]
                                                                else:
                                                                    number_of_function += 1
                                elif session_mode_order == "N":
                                    seetings = 0
                                else:
                                    LOGGER.info("error, answer is not good")
                        if order_sittings == "exit()":
                            settings = 0
    if order == "text editor":
        if file == "":
          LOGGER.info("please enter your text here")
          
          file = input("")
        else:
            LOGGER.info(file)
            file = input()
    if order == "SHUTDOWN":       
           shutdown() 
    if order == "Wait a minute ...":
        LOGGER.info("ok bro")
        tm.sleep(60)
    if order == "clock":
        clock = 1
        while clock == 1:
            clock_order = input ("What do you want")
            if clock_order == "help":
                LOGGER.info("here's the list of the command:\n help : you know\n timer : a timer\n calendar : a calendar for today")
            if clock_order == "timer":
                timer_sec = input ("How Many second do you want ?")
                timer_minute = input("how many minutes do you want ?")
                timer_hour = input("how many hours do you want ?")
                timer_total = (float(timer_sec)+(float(timer_minute)*60)+(float(timer_hour)*3600))
                while timer_total != 0:
                   timer_total -= 1 
                   LOGGER.info(timer_total)
                   tm.sleep(1)
                LOGGER.info("TIMER IS FINISHED")
            if clock_order == "calendar":
                print("do something")
            if clock_order == "exit()":
                clock = 0
                                    