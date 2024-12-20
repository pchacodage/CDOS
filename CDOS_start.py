# put start code here
import time as tm
# import math
import random as rnd
import logging

LOGGER: logging.Logger = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)

LOGGER.info("Colony Developement")
LOGGER.info("CDOS is starting")


def shutdown():
    LOGGER.info("system downing ...")
    tm.sleep(3)
    LOGGER.info("system is down !")
    exit()


modeinput = 0
session_number = 1
session = ["general"]
passwords = ["No passwords"]
if session_number < 1:
    session = input("wich session do you want to start (please enter the identifiant of session) ?")
else:
    mode = input("wich mode do you want ? (N/G)")
    if mode == "N":
        mode = ("admin")
        session_choosed = ("general")
        modeinput = 1
    elif mode == "G":
        mode = ("guest")
        session = ["Guest"]
        modeinput = 1
    else:
        LOGGER.warning("critical error : answer not availaible")
        exit()

# end of starting
print("CDOS is started")
while True:
    print(f"computer/{session_choosed}>")
    order = input("")
    if order == "calculator":
        easter_egg = rnd.randint(1, 100)
        if easter_egg == 11:
            print("your computer IS a calculator")
        first_number = int(input("please enter the 1st number"))
        sign = input("please enter the sign :")
        second_number = int(input("please enter the 2nd number"))
        if sign == "/":
            result = (first_number / second_number)
        else:
            if sign == "*":
                result = (first_number * second_number)
            else:
                if sign == "-":
                    result = (first_number - second_number)
                else:
                    if sign == "+":
                        result = (first_number + second_number)
        print("the result is", result)
    if order == "help":
        LOGGER.info(
            "here's the list of all the commands: \n calculator : a very basic calculator \n help : you know \n rnd : : choose a random number between 2 numbers you choose\n settings : Settings of computer. Can only acces with admin access\n SHUTDOWN : exit from the programm")
    if order == "rnd":
        first_limit = input("please enter the first limit")
        try:
            int(first_limit)
        except:
            LOGGER.info("critical error, please enter a number")
            continue
        second_limit = input("please enter the second limit")
        try:
            int(second_limit)
        except:
            LOGGER.info("critical error, please enter a valid number")
            continue
        result = rnd.randint(float(first_limit), float(second_limit))
        LOGGER.info("le nombre est ", result)
    if order == "settings":
        LOGGER.info("debug message, line 71 : settings is starting")
        if mode == ("guest"):
            LOGGER.info("error : you are not admin !")
        if mode == ("admin"):
            settings = 1
            while settings == 1:
                order_settings = ("what do you want ?")
                if order_settings == ("help"):
                    LOGGER.info(
                        "here's the list of the commands : help : you know \n sessions : for create, delete and modify the sessions")
                else:
                    if order_settings == ("sessions"):
                        if second_number == 1:
                            session_mode_order = input(
                                "Currently, the mode admin/guest sessions is active, do you want to change it ? (Y/N)")
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
                                        session_number = + 1
                                        sessions = + (input("Please enter the new identifiant") + ",")
                                        passwords = + (input("Please enter the new password") + ",")
                                    else:
                                        if session_mode_order == "M":
                                            session_to_modify = input("Wich session do you want to modify ?")
                                            if session_to_modify in session:
                                                thing_to_modify = input("what do you want to modify ? (Password : P, Identifiant : I")
                                                if thing_to_modify == "P":
                                                    position_session_to_modify = session.find()
                                                    point_research = 1
                                                    for session_to_modify in session:
                                                        if session_to_modify == session:
                                                            LOGGER.info("Oh, I find it !")
                                                    if session_mode_order == "M":
                                                        LOGGER.info("Oh, error code, please look at script line 112")

                                                else:
                                                    LOGGER.info("error, answer is not good")
        else:
            LOGGER.info("system hack or bypass detected, system shutdowning")
            shutdown()
    if order == "SHUTDOWN":
        shutdown()
