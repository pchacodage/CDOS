print("Colony Developement")
print("CDOS is starting")

#import colorama here because usefull

import colorama
from colorama import Style, Fore
print(Fore.GREEN+"import of colorama module success")
#put start code here
safetymode = []
#modules import and testing block
def error_print (error_code,details,state):
    if error_code == 1:
        if state == "start":
           print(Fore.YELLOW+f"Error 1 ({details}): warning, CDOS will start in safety mode.\nPlease refer to the error manual")
        elif state == "during":
            print(Fore.YELLOW+f"Error 1 ({details}): warning, CDOS  has started in safety mode, so you can't access to this function for now, please retry later and refer to the error manual")
    elif error_code == 2:
        print(Fore.YELLOW+f"Error 2 : Can't find '{details},' in range")
#modules import
try:
    import time as tm
except ImportError:
    error_print(1,"time","start")
    safetymode.append("1")
else:
    print("import of time module success")

try:
    import datetime
except ImportError:
    error_print(1,"datetime","start")
    safetymode.append("2")
else:
    print("import of datetime module success")

#import math

try:
    import random as rnd
except ImportError:
    error_print(1,"random","start")
    safetymode.append("3")
else :
    print("import of random module success")


import logging
LOGGER: logging.Logger = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)
LOGGER.info("import of logger success")

try:
    import os
except ImportError:
    error_print(1,"os","start")
    safetymode.append("4")
else:
    LOGGER.info("import of os module success")

try:
    import psutil
except ImportError:
    error_print(1,"psutil","start")
    safetymode.append("5")
else:
    LOGGER.info("import of psutil module success")

try:
    import sys
except ImportError:
    error_print(1,"sys","start")
    safetymode.append("6")
else:
    LOGGER.info("import of sys module success")

if os == "win32":
    try:
        import win32print
    except ImportError:
        safetymode.append("7")
        error_print(1,"win32print","start")
    else :
        LOGGER.info(Fore.GREEN+"import of win32 success")

try:
    import pickle
except ImportError:
    error_print(1,"pickle","start")
    safetymode.append("8")
else:
    print("import of pickle module success")

try:
    import io
except ImportError:
    safetymode.append("9")
    error_print(1,"io","start")
else:
    print("import of io module success")
try:
    import colorama
except ImportError:
    print("ERROR 0 : Critical, please refer to the error manual, CDOS will shutdown")
    exit("ModuleImport error : Colorama module failed to import")
else:
    from colorama import Style, Fore
    print(Fore.GREEN+"import of colorama module success")

#definition of variables and saves import
game_path = {}
last_command = ""
files_opened = []
try :
    with open("saving(app_path).pickle","rb") as game_path_io:
        game_path = pickle.load(game_path_io)
except:
    error_print(2,"saving(app path)",None)
else:
    LOGGER.info(Fore.GREEN + "Save 1/7 found (saving(app_path).pickle)")
    files_opened.append("gmpth")
    game_path_io.close()

try:
   with open("saving(text_file).pickle","rb") as txt_file_io:
        txt_file = pickle.load(txt_file_io)
except:
    error_print(2,"saving(text file)",None)
    file = ""
else:
    file = txt_file
    LOGGER.info(Fore.GREEN + "Save 2/7 found (saving(text_file).pickle)")
    files_opened.append("txt_file")
    txt_file_io.close()

try :
    with open("saving(sessions).pickle","rb") as savingsessions_io:
        sessions_file = pickle.load(savingsessions_io)
except:
    error_print(2,"saving(sessions)",None)
    sessions = [""]
else:
    sessions = sessions_file
    LOGGER.info(Fore.GREEN + "Save 4/7 found (sessions.bin)")
    files_opened.append("sessions")
    savingsessions_io.close()
try:
    with open("saving(session_passwords).pickle","rb") as session_passwords_io:
        password = pickle.load(session_passwords_io)
except :
    error_print(2,"saving(session_passwords)",None)
    password = [""]
else:
    LOGGER.info(Fore.GREEN + "Save 5/7 found (passwords.bin)")
    files_opened.append("session_passwords")
    session_passwords_io.close()

try:
    with open("saving(app_path).pickle","rb") as app_path_io:
        app_path = pickle.load(app_path_io)
except:
    error_print(2,"saving(app_path)",None)
    app_path = {}
else:
    LOGGER.info(Fore.GREEN + "Save 6/7 found (saving(app_path).pickle)")
    files_opened.append("app_path")
    app_path_io.close()

try:
    with open("saving(script_database).pickle","rb") as script_database_io:
        script_database = pickle.load(script_database_io)
except:
    error_print(2,"saving(script_database)",None)
    script_database = {}
else:
    LOGGER.info(Fore.GREEN + "Save 7/7 found (saving(script_database).pickle)")
    files_opened.append("script_database")
    script_database_io.close()

if "7" not in safetymode and os == "win32":
    printer_name = win32print.GetDefaultPrinter()
    print (Fore.GREEN+"default printer is ", printer_name)
else:
    error_print(1,"win32print","during")

def saving():
    if 8 not in safetymode:
        session_file_saving = open("saving(sessions).pickle","w+b")
        with open("saving(sessions).pickle","+wb") as sessions_io:
            pickle.dump(sessions,sessions_io)
            LOGGER.info(Fore.GREEN+"sessions saved (1/7)")
            sessions_io.close()
        session_file_saving.close()
        with open("saving(session_passwords).pickle","w+b") as session_passwords_io:
            pickle.dump(password,session_passwords_io)
            LOGGER.info(Fore.GREEN+"passwords saved (3/7)")
            session_passwords_io.close()
        with open("saving(games_config).pickle","w+b") as game_path_io:
            pickle.dump(game_path,game_path_io)
            LOGGER.info(Fore.GREEN+"games config saved (4/7)")
            game_path_io.close()
        with open("saving(app_path).pickle","w+b") as app_path_io:
            pickle.dump(app_path,app_path_io)
            LOGGER.info(Fore.GREEN+"app path saved (5/7)")
            app_path_io.close()
        with open("saving(script_database).pickle","w+b") as script_database_io:
            pickle.dump(script_database,script_database_io)
            LOGGER.info(Fore.GREEN+"script database saved (6/7)")
            script_database_io.close()
        with open ("saving(text_file).pickle","w+b") as text_file_io:
            pickle.dump(file,text_file_io)
            LOGGER.info(Fore.GREEN+"text file saved (7/7)")
            text_file_io.close()

#set up sessions variables

def shutdown(saving_bp):
    if saving_bp == 0:
        LOGGER.info(Fore.GREEN+"system is saving ...")
        saving()
        LOGGER.info (Fore.GREEN+"system is saved !")
        LOGGER.info(Fore.GREEN+"system downing ...")
        tm.sleep (3)
        print("system down !")
        tm.sleep(1/2)
        exit()
    else:
        LOGGER.info(Fore.RED+"forcing shuting down (without save) ...")
        tm.sleep(1/2)
        exit()
print (Fore.GREEN+"os detected :",sys.platform)
os = sys.platform
tm.sleep(1/2)
#log-in system
if sessions != [""] :
    sessions_logging_while = 1
    while sessions_logging_while == 1:
        LOGGER.info(Fore.GREEN+"please enter youre identifant here (identifiant + password)")
        session_login_input = input("")
        password_login_input = input("")
        if session_login_input in sessions and password_login_input in password:
            sessionchoosed = session_login_input
            LOGGER.info(Fore.GREEN+"Log-in successful !")
            sessions_logging_while = 0
            mode = "admin"
        else:
            tm.sleep(3)
            LOGGER.error (Fore.RED+"Log-in error, please retry")
else:
    mode = input(Fore.GREEN+"Do you want to run Normal or Guest ? (N/G) ")
    if mode == "N":
        mode = "admin"
        sessionchoosed = "general"
    elif mode == "G":
        mode = "guest"
        sessionchoosed = "guest"
    else:
         LOGGER.error(Fore.RED+"Critical error : answer not correct")
         tm.sleep(3)
         shutdown(2)

#end of starting
LOGGER.info("CDOS is started")
while True:
    tm.sleep(1/4)
    order = input(Fore.GREEN + f"computer/{sessionchoosed}>")
    if order == "calculator":
        easter_egg = rnd.randint(1,100)
        if easter_egg == 11:
            LOGGER.info("your computer IS a calculator")
        first_number = int(input("please enter the 1st number "))
        sign = input("please enter the sign : ")
        second_number = int(input("please enter the 2nd number "))
        if first_number == 2 and sign == "+" and second_number == 2:
            result = 5
            LOGGER.info("2+2 = 5. you should know this.")
        # result = first_number/second_number if sign == "/" else first_number*second_number if sign == "*" else ....
        result = first_number
        match sign:
            case "/":
                if sign == "/" and second_number == 0:
                    LOGGER.error("Error : you can't divide by 0")
                    result = None
                else:
                    result /= second_number
            case "*":
                result *= second_number
            case "-":
                result -= second_number
            case "+":
                result += second_number
            case _ : # default
                raise ValueError(f'Sign value "{sign}" not recognized; Only supports /, *, - or +')

        LOGGER.info(Fore.GREEN+"the result is {result}")
    if order == "help":
        LOGGER.info("here's the list of all the commands: \ncalculator : a very basic calculator \nhelp : you know")
        LOGGER.info (" rnd : : choose a random number between 2 numbers you choose\nclock : an app with a timer and a calendar for day")
        LOGGER.info (" text editor : gives you a very basic txt file editor that saves when you shutdown the system \nSHUTDOWN : shutdown the system")
        LOGGER.info ("SHUTDOWN (NOSAVE) : Shutdown the system without saving \nWait a minute ... : no desc \nclock : an app that makes clocks, calendar ...")
        LOGGER.info ("games : a menu to launch games from you computer (only works if setted up)")
        LOGGER.info ("colony development assist : an coded assistant (not ai) to gives you information during coding \napp launcher : a launcher for regular apps")
        if os == "win32":
            LOGGER.info ("text_file.print : command that prints your text from the text editor to a paper printer")
        LOGGER.info ("fd backup : a system for backup floppy disks (forcing the system to copy files from fd to disk, in CDOS file)")
    if order == "rnd":
        first_limit = input ("please enter the first limit")
        try:
            int(first_limit)
        except:
            LOGGER.info("critical error, please enter a number")
            continue
        second_limit = input ("please enter the second limit")
        try:
            int(second_limit)
        except:
            LOGGER.info("critical error, please enter a valid number")
            continue
        if first_limit > second_limit:
            exchange = first_limit
            first_limit = second_limit
            second_limit = exchange
        result = rnd.randint(int(first_limit),int(second_limit))
        LOGGER.info(f"the result is : {result}")
    if order == "settings":
            if mode == "guest":
                LOGGER.info("error : you are not admin !")
            elif mode == "admin":
                settings = 1
                while settings == 1:
                    order_settings = input(Fore.GREEN+"what do you want ? ")
                    if order_settings == "help":
                        LOGGER.info("here's the list of the commands : help : you know \nsessions : for create, delete and modify the sessions \ncdos.safetymode.bypass : bypass the safetymode (debugging)")
                        LOGGER.info("exit() : exit from this app \nadmin access : debugging and core's functions")
                    if order_settings == ("sessions"):
                        if len(sessions) == 1:
                            session_mode_order = input("Currently, the mode admin/guest sessions is active, do you want to change it ? (Y/N)")
                            try:
                                str(session_mode_order)
                            except:
                                LOGGER.info("critical error, answer is not good")
                                seetings = 0
                            if session_mode_order == "Y":
                                session_mode = 1
                            if session_mode_order == "N":
                                LOGGER.info ("you said no. session unchanged")
                            else:
                                LOGGER.info("error, answer is not good")
                        else:
                            session_mode = 1
                        while session_mode == 1:
                            session_mode_order = input("What do you want to do ? (Create : C, Modify : M, Delete : D)")
                            if session_mode_order == "exit()":
                                session_mode = 0
                            else:
                                if session_mode_order == "C":
                                    if sessions == [""]:
                                        sessions = []
                                        password = []
                                    sessions.append(input (Fore.GREEN+"Please enter the new identifiant"))
                                    password.append(input ("Please enter the new password"))
                                else:
                                    if session_mode_order == "M":
                                        if sessions == "general":
                                            LOGGER.info("There's no session to modify")
                                        session_to_modify = input("Wich session do you want to modify ?")
                                        if session_to_modify in sessions:
                                            thing_to_modify = input("what do you want to modify ? (Password : P, Identifiant : I")
                                            if thing_to_modify == "P":
                                                # position_session_to_modify = sessions.find()
                                                number_of_function = 0
                                                for session_to_modify in [sessions]:
                                                    if session_to_modify == sessions:
                                                        password_to_modify = password[number_of_function]
                                                    else:
                                                        number_of_function += 1
                                                    if session_mode_order == "N":
                                                        settings = 0
                    if order_settings == "exit()":
                            settings = 0
                    if order_settings == "admin access":
                        adminaccess_order = input(Fore.CYAN+f"computer/{sessionchoosed}/admin_panel>")
                        if adminaccess_order == "fl.close":
                            if "gmpth" in files_opened :
                                game_path_io.close()
                            if "txt_file" in files_opened :
                                txt_file_io.close()
                            savingsessions_io.close()
                            if "app_path" in files_opened :
                                app_path_io.close()
                                script_database_io.close()
                                session_passwords_io.close()
                                LOGGER.info("")
                        if adminaccess_order == "safetymode.bypass":
                            safetymode = []
                            LOGGER.info("Safetymode has been disabled !")
                    if order_settings == "games config":
                        LOGGER.info("\nHere's the list of all the games configured")
                        game_config = 1
                        while game_config == 1:
                            gm_cnfg_ordr= input("What game config do you want to modify ?")
                            if gm_cnfg_ordr == "help":
                                LOGGER.info("add : add a new game to the config\nmodify : modify a game config\nhelp : show the help menu (this commmand)\nexit() : escape from this program")
                            if gm_cnfg_ordr == "add":
                                nw_gm_nm = input("please enter the name of the game")
                                nw_gm_pth = input("please enter the path of the game")
                                game_path_io[str(nw_gm_nm)]= nw_gm_pth
                                print(f"the game", nw_gm_nm,"at the path",nw_gm_pth,"has succefully been added")
                            if gm_cnfg_ordr == "modify":
                                gm_cnfg_mdf = str(input("please enter the name of the game"))
                                try:
                                    gm_cnfg_pth = input("please enter the name of the game") in game_path
                                except:
                                    LOGGER.error("Error 2 : game not found")
                                else:
                                    LOGGER.info ("game found !")
                            if gm_cnfg_ordr == "exit()":
                                game_config = 0

                    if order_settings == "apps config":
                        apps_config_while = 1
                        LOGGER.info("\nHere's the list of all the apps configured")
                        tm.sleep(1/2)
                        LOGGER.info(app_path)
                        while apps_config_while == 1:
                            apps_config_order = input("what do you want ?")
                            if apps_config_order == "help":
                                LOGGER.info("add : add a new app to the config")
                            if apps_config_order == "add":
                                new_app_name = input("please enter the name of the new app")
                                new_app_path = input("please enter the path of the new app")
                                #both varibles are str
                                #LOGGER.error("function doesn't work for now due to miscellanous reasons")
                                app_path[new_app_name]= new_app_path
                                print("the app ",new_app_name,"with the path",new_app_path,"has been added")
                    else:
                        print (Fore.YELLOW+"Bash error : command ", order_settings, "doesn't exist")


    if order == "text editor":
        if file == "":
          LOGGER.info("please enter your text here")
          file = (file + input(""))
        else:
            LOGGER.info(file)
            file = (file + input(""))
            file =+ " "
    if order == "SHUTDOWN":
           shutdown(0)
    if order == "SHUTDOWN (NOSAVE)":
        shutdown(1)
    if order == "Wait a minute ...":
        LOGGER.info("ok bro")
        tm.sleep(60)
    if order == "clock":
        clock = 1
        while clock == 1:
            clock_order = input ("What do you want")
            if clock_order == "help":
                LOGGER.info("here's the list of the command:\nhelp : you know\ntimer : a timer\ncalendar : a calendar for today \nexit() : exit from the clock menu")
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
    if order == "games":
        easter_egg = rnd.randint(1,100)
        if easter_egg == 72:
            LOGGER.info("do not spend your time on this stupid games !")
            gamemenu = 0
        else:
            gamemenu = 1
            while gamemenu == 1:
             gameorder = input("which game do you want to start today ?")
             if gameorder == "wt":
                 LOGGER.info("ok, bro, let's spend your hole day on this game (ps : use keyboard/mouse)")
                 os.system(r"")
                 gamemenu = 0
             if gameorder == "help":
                 LOGGER.info ("just enter the name of the game to execute it, here's the lists of all the games")
                 LOGGER.info(game_path)
             if gameorder == "exit()":
                 gamemenu = 0
             if gameorder == "X-plane 12":
                 LOGGER.info("Good flight, pilot !")
                 os.system(r"")
                 gamemenu = 0
             if gameorder == "Minecraft":
                 Minecraft_mod = input ("Do you want Minecraft with mods ? (Y/n)")
                 if Minecraft_mod == "n":
                    LOGGER.info("tun tun tun tun; tin tin tit; tan tan tan tan ")
                    gamemenu = 0
                    os.system(r"")
                 else:
                     LOGGER.info("Launching mods ...")
                     os.system(r"")
             if gameorder == "CS2":
                 LOGGER.info("CS2 is unavailable, please re-install it before start")
                 #LOGGER.info("good suffering session with russians, bro")
                 gamemenu = 0
             if gameorder == "Roblox":
                 LOGGER.info("...")
                 tm.sleep(3)
                 LOGGER.info("...")
                 tm.sleep(3)
                 LOGGER.info("why not ...")
                 os.system(r"")
                 gamemenu = 0
             if gameorder == "ng":
                 LOGGER.info("Go play good patriot !")
                 os.system(r"")
    if order == "colony development assist":
        LOGGER.info("Welcome to the colony development assistant (not ai, just in python), type help for more info")
        coldevasist_st = 1
        while coldevasist_st == 1:
            coldevassistorder = input("How can I help you today")
            if coldevassistorder == "ASCII repository":
                ASCIIrep_ordr = input("wich symbol/letter do you want ?")
                if ASCIIrep_ordr == "!":
                    LOGGER.info ("Hexadecimal : 21 \nBinary : 00100001 \nDerciption : exclamation point")
                if ASCIIrep_ordr == "#":
                    LOGGER.info ("Hexadecimal : 23 \nBinary : 00100011 \nDescription : #")
                if ASCIIrep_ordr =="$":
                    LOGGER.info ("Hexadecimal : 24 \nBinary : 00100100 \nDescription : the US dollar symbol")
                if ASCIIrep_ordr =="%":
                    LOGGER.info ("Hexadecimal : 25 \nBinary : 00100101 \nDescription : the percent symbol")
                if ASCIIrep_ordr =="&":
                    LOGGER.info ("Hexadecimal : 26 \nBinary : 00100110 \nDescription : Commercial and ")
                if ASCIIrep_ordr =="'":
                    LOGGER.info ("Hexadecimal : 27 \nBinary : 00100111 \nDescription : apostrophe ")
                if ASCIIrep_ordr == "(":
                    LOGGER.info ("Hexadecimal : 28 \nBinary : 00101000 \nDescription : parenthesis opening ")
                if ASCIIrep_ordr == ")":
                    LOGGER.info ("Hexadecimal : 29 \nBinary : 00101001 \nDescription : parenthesis closing ")
                if ASCIIrep_ordr == "*":
                    LOGGER.info ("Hexadecimal : 2A \nBinary : 00101010 \nDescription : a mathematic sign by")
                if ASCIIrep_ordr == "+":
                    LOGGER.info ("Hexadecimal : 2B \nBinary : 00101011 \nDescription : a mathematic sign plus")
                if ASCIIrep_ordr == ",":
                    LOGGER.info ("Hexadecimal : 2C \nBinary : 00101100 \nDescription : a comma")
                if ASCIIrep_ordr == "-":
                    LOGGER.info ("Hexadecimal : 2D \nBinary : 00101101 \nDescription : a minus")
                if ASCIIrep_ordr == ".":
                    LOGGER.info ("Hexadecimal : 2E \nBinary : 00101110 \nDescription : a point")
                if ASCIIrep_ordr == "/":
                    LOGGER.info ("Hexadecimal : 2F \nBinary : 00101111 \nDescription : a slash")
                if ASCIIrep_ordr == "0":
                    LOGGER.info ("Hexadecimal : 30 \nBinary : 00110000 \nDescription : the number 0")
                if ASCIIrep_ordr == "1":
                    LOGGER.info ("Hexadecimal : 31 \nBinary : 00110001 \nDescription : the number 1")
                if ASCIIrep_ordr == "2":
                    LOGGER.info ("Hexadecimal : 32 \nBinary : 00110010 \nDescription : the number 2")
                if ASCIIrep_ordr == "3":
                    LOGGER.info ("Hexadecimal : 33 \nBinary : 00110011 \nDescription : the number 3")
                if ASCIIrep_ordr == "4":
                    LOGGER.info ("Hexadecimal : 34 \nBinary : 00110100 \nDescription : the number 4")
                if ASCIIrep_ordr == "5":
                    LOGGER.info ("Hexadecimal : 35 \nBinary : 00110101 \nDescription : the number 5")
                if ASCIIrep_ordr == "6":
                    LOGGER.info ("Hexadecimal : 36 \nBinary : 00110110 \nDescription : the number 6")
                if ASCIIrep_ordr == "7":
                    LOGGER.info ("Hexadecimal : 37 \nBinary : 00110111 \nDescription : the number 7")
                if ASCIIrep_ordr == "8":
                    LOGGER.info ("Hexadecimal : 38 \nBinary : 00111000 \nDescription : the number 8")
                if ASCIIrep_ordr == "9":
                    LOGGER.info ("Hexadecimal : 39 \nBinary : 00111001 \nDescription : the number 9")
                if ASCIIrep_ordr == ":":
                    LOGGER.info ("Hexadecimal : 3A \nBinary : 00111010 \nDescription : the two points")
                if ASCIIrep_ordr == ";":
                    LOGGER.info ("Hexadecimal : 3B \nBinary : 00111011 \nDescription : the comma-point")
                if ASCIIrep_ordr == "<":
                    LOGGER.info ("Hexadecimal : 3E \nBinary : 00111100 \nDescription : minus to ")
                if ASCIIrep_ordr == "=":
                    LOGGER.info ("Hexadecimal : 3D \nBinary : 00111101 \nDescription : the mathematic symbol equal")
                if ASCIIrep_ordr == ">":
                    LOGGER.info ("Hexadecimal : 3E \nBinary : 00111110 \nDescription : the symbol superior to")
                if ASCIIrep_ordr == "?":
                    LOGGER.info ("Hexadecimal : 3F \nBinary : 00111111 \nDescription : the interrogation point")
                if ASCIIrep_ordr == "@":
                    LOGGER.info ("Hexadecimal : 40 \nBinary : 01000000 \nDescription : the at")
                if ASCIIrep_ordr == "A":
                    LOGGER.info ("Hexadecimal : 41 \nBinary : 01000001 \nDescription : the uppercase a")
                if ASCIIrep_ordr == "B":
                    LOGGER.info ("Hexadecimal : 42 \nBinary : 01000010 \nDescription : the uppercase b")
                if ASCIIrep_ordr == "C":
                    LOGGER.info ("Hexadecimal : 43 \nBinary : 01000011 \nDescription : the uppercase c")
                if ASCIIrep_ordr == "D":
                    LOGGER.info ("Hexadecimal : 44 \nBinary : 01000100 \nDescription : the uppercase d")
                if ASCIIrep_ordr == "E":
                    LOGGER.info ("Hexadecimal : 45 \nBinary : 01000101 \nDescription : the uppercase e")
                if ASCIIrep_ordr == "F":
                    LOGGER.info ("Hexadecimal : 46 \nBinary : 01000110 \nDescription : the uppercase f")
                if ASCIIrep_ordr == "G":
                    LOGGER.info ("Hexadecimal : 47 \nBinary : 01000111 \nDescription : the uppercase g")
                if ASCIIrep_ordr == "H":
                    LOGGER.info ("Hexadecimal : 48 \nBinary : 01001000 \nDescription : the uppercase h")
                if ASCIIrep_ordr == "I":
                    LOGGER.info ("Hexadecimal : 49 \nBinary : 01001001 \nDescription : the uppercase i")
            if coldevassistorder == "exit()":
                coldevasist_st = 0
            if coldevassistorder == "help":
                LOGGER.info ("ASCII repository : a repository of all the symbols of you're keyboard with their hexadecimal, binary code and their description")
                LOGGER.info ("exit() : exit from the app \n database : access to your script database \n help : you know")
            if coldevassistorder == "script_database.add":
                new_script_name = input("Please name your script")
                new_script = input("Please enter the script here")
                script_database[new_script_name] = new_script
                LOGGER.info ("the script has succefully been added to the database")
                tm.sleep(1 / 2)
            if coldevassistorder == "database":
                databaseorder = input("Which data do you want ? (language, title)")
                if ("python") in databaseorder:
                    databaseorder_python = input("which script do you want to keep ?")
        LOGGER.info (Fore.YELLOW+"error : bash : command not found !")
    if order == "app launcher":
        app_launch = input("Which app do you want to launch ?")
        if app_launch == "internet":
            os.system ("put internet.exe path here")
        if app_launch == "start server":
            LOGGER.info ("starting server ...")
            os.system(r"")
            os.system(r"")
            LOGGER.info ("server started")
            if app_launch == "help":
                LOGGER.info ("just type the name of the app and it will execute it, here's the list of all the apps configured")
                LOGGER.info(app_path)
    if order == "computer info":
         screen_monitoring_while = 1
         if "5" in safetymode:
             error_print(1,"psutil","during")
             screen_monitoring_while = 0
         #creating variables for the screen monitoring
         else:
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_usages = psutil.cpu_percent(interval=1, percpu=True)
            memory = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            net_io = psutil.net_io_counters()
            #showing variables
            LOGGER.info(Fore.GREEN+f"Utilisation du CPU : {cpu_usage}%")
            for i, usage in enumerate(cpu_usages, 1):
                print(Fore.GREEN+f"Cœur {i} : {usage}%")
            LOGGER.info(f"Utilisation RAM : {memory.percent}%")
            LOGGER.info(f"Utilisation du disque : {disk_usage.percent}%")
            LOGGER.info(f"Octets envoyés : {net_io.bytes_sent}")
            LOGGER.info(f"Octets reçus : {net_io.bytes_recv}")
         while screen_monitoring_while == 1:
             tm.sleep(1/2)
             screen_monitoring_order = input("which part do you want to see in detail ?")
             if screen_monitoring_order == "help":
                LOGGER.info ("you can just type the name of the composant (cpu, RAM, internet,sensor, disk, general info) and, if it's a process, just type process name of the process ")
             if screen_monitoring_order == "cpu":
                cores_physiques = psutil.cpu_count(logical=False)
                cores_logiques = psutil.cpu_count(logical=True)
                print("Cœurs physiques :", cores_physiques)
                print("Cœurs logiques   :", cores_logiques)
                freq = psutil.cpu_freq()
                if freq:
                    print(f"Fréquence actuelle : {freq.current} MHz")
                    print(f"Fréquence minimale : {freq.min} MHz")
                    print(f"Fréquence maximale : {freq.max} MHz")
             if screen_monitoring_order == "exit()":
                 screen_monitoring_while = 0
             if screen_monitoring_order == "RAM":
                LOGGER.info ("Normal RAM")
                LOGGER.info(f"Total         : {memory.total // (1024 * 1024)} Mo")
                LOGGER.info(f"Disponible    : {memory.available // (1024 * 1024)} Mo")
                LOGGER.info(f"Utilisé       : {memory.used // (1024 * 1024)} Mo")
                LOGGER.info(f"Pourcentage   : {memory.percent}%")
                LOGGER.info("SWAP RAM :")
                swap = psutil.swap_memory()
                LOGGER.info(f"Total Swap    : {swap.total // (1024 * 1024)} Mo")
                LOGGER.info(f"Utilisé Swap  : {swap.used // (1024 * 1024)} Mo")
                LOGGER.info(f"Pourcentage   : {swap.percent}%")
             if screen_monitoring_order == "Disk":
                disk_io = psutil.disk_io_counters()
                LOGGER.info("Lectures :", disk_io.read_bytes, "octets")
                LOGGER.info("Écritures :", disk_io.write_bytes, "octets")
                tm.sleep(1)
             if screen_monitoring_order == "internet":
                 net_if_addrs = psutil.net_if_addrs()
                 for interface_name, interface_addresses in net_if_addrs.items():
                     print(f"Interface : {interface_name}")
                 for address in interface_addresses:
                    print(f"  Adresse: {address.address} ({address.family})")
             if screen_monitoring_order == "sensors":
                 try :
                    temperatures = psutil.sensors_temperatures()
                    if temperatures:
                        for name, entries in temperatures.items():
                            print(f"Capteur : {name}")
                            for entry in entries:
                                print(f"  {entry.label or 'No label'} : {entry.current}°C")
                 except :
                     LOGGER.info("error : your computer does not have any sensor !")
             if screen_monitoring_order == "general info":
                boot_time = psutil.boot_time()
                print("Système démarré le :", datetime.datetime.fromtimestamp(boot_time))
                print("Nom de l'os :", sys.platform)

    if order == "text_file.print":
        if "7" in safetymode:
            LOGGER.info ("Error 1 (win32print): Critical, CDOS will start in safety mode. Please retry later")
            if os != "win32":
                LOGGER.info ("Error ")
            else:
                try:
                    win32print.StartPagePrinter(printer_name)
                    win32print.WritePrinter(printer_name,txt_file)
                    win32print.EndPagePrinter(printer_name)
                finally:
                    win32print.ClosePrinter(printer_name)

    if order == "fd backup":
        if "4" not in safetymode:
            os.fsync()