print("Colony Developement")
print("CDOS is starting")
#put start code here
safety_mode = 0
try:
    import time as tm
except ImportError:
    print("Error 1 (time as tm): Critical, CDOS will start in safety mode.")
    safety_mode = 1

try:
    import datetime
except ImportError:
    print("Error 1 (datetime): Critical, CDOS will start in safety mode.")
    safety_mode = 2

#import math

try:
    import random as rnd
except ImportError:
    print("Error 1 (random as rnd): Critical, CDOS will start in safety mode.")
    safety_mode = 3

try:
    import logging
except ImportError:
    print("Error 0 : Critical, please refer to the error manual, CDOS will exit().")
    time.sleep(3)
    exit("Bash error : loging import error (code 0)")
else:
    LOGGER: logging.Logger = logging.getLogger(__name__)
    LOGGER.addHandler(logging.StreamHandler())
    LOGGER.setLevel(logging.INFO)


try:
    import os
except ImportError:
    print("Error 1 (os): Critical, CDOS will start in safety mode.")
    safety_mode = 4

try:
    import psutil
except ImportError:
    print("Error 1 (psutil): Critical, CDOS will start in safety mode.")
    safety_mode = 1

file = ""
game_to_exe = ("nah bro")
txt_file = open("file_editor.txt", "a")
txt_file.write(str(file))
txt_file.close()

#for the good version, replace . txt (except txt_file ) to .bin
def saving():
    sessions_file = open("saving(sessions).txt","w")
    sessions_file.write(str(sessions))
    sessions_file.close()
    session_number_file = open("saving(session_number).txt","w")
    session_number_file.write(str(session_number))
    session_number_file.close()
    passwords_file = open ("saving(passwords).txt","w")
    passwords_file.write(str(passwords_file))
    passwords_file.close()
    txt_file = open("file_editor.txt", "a")
    txt_file.write(str(file))
    txt_file.close()

#set up seesions variables
try : session_number_file = open("saving(session_number).bin","r")
except:
    sessions_file = open("saving(sessions).bin","w")
    sessions_file.close()
    session_number = ["general"]
    session_number_file = open("saving(session_number).bin","w")
    session_number_file.close()
    session_number = 1
    passwords_file = open ("saving(passwords)","w")
    passwords_file.close()
    passwords = ["No password"]


session_number_file = open("saving(session_number).bin","r")
session_number = session_number_file
session_number_file.close()

sessions_file = open("saving(sessions).bin","r")
sessions = [sessions_file]
sessions_file.close()

passwords_file = open ("saving(passwords)","r")
passwords = [passwords_file]
passwords_file.close()

def shutdown():
    LOGGER.info("system is saving ...")
    saving()
    LOGGER.info ("system is saved !")
    LOGGER.info("system downing ...")
    tm.sleep (3)
    LOGGER.info("system down !")
    tm.sleep(1/2)
    exit()


if sessions == "General" :
    session = input("wich session do you want to start (please enter the identifiant of session) ?")
else:
    mode = input("Do you want to run Normal or Guest ? (N/G) ")
    if mode == "N":
        mode = ("admin")
        sessionchoosed = ("general")
    elif mode == "G":
        mode = ("guest")
        sessionchoosed = ("guest")
    else:
         LOGGER.info("critical error : answer not availaible")
         tm.sleep(3)
         shutdown

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
                                                    if sessions == "general":
                                                        LOGGER.info("There's no session to modify")
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

                                                                if session_mode_order == "N":
                                                                  settings = 0
                                else:
                                    LOGGER.info("error, answer is not good")
                        if order_sittings == "exit()":
                            settings = 0
                        if order_sittings == "admin access":
                            adminaccess_order = input(f"computer/{sessionchoosed}/admin_panel>")
                            if adminaccess_order == "fl.close":
                                sessions_file.close()
                                session_number_file.close()
                                passwords_file.close()
                                txt_file.close()
                            if adminaccess_order == "variables.print":
                                LOGGER.info("Here's the list of all the system's variables")
                                LOGGGER.info
    if order == "text editor":
        if file == "":
          LOGGER.info("please enter your text here")
          file = (file + input(""))
        else:
            LOGGER.info(file)
            file = (file + input(""))
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
                 os.system(r"put the wt LAUNCHER path here")
                 gamemenu = 0
             if gameorder == "help":
                 LOGGER.info ("here the list of the differents commands : \n wt : starts war thunder \n help : you know \n exit() : exit from the game menu\n  MSFS : start Microsoft Flight Simulator with pilots for yoke and his attachements ")
                 LOGGER.info("Minecraft : launch the Minecraft launcher \n CS2 : starts Counter-strike2")
             if gameorder == "exit()":
                 gamemenu = 0
             if gameorder == "X-plane 12":
                 LOGGER.info("Good flight, pilot !")
                 os.system(r"put x-plane 12 path here")
                 gamemenu = 0
             if gameorder == "Minecraft":
                 Minecraft_mod = input ("Do you want Minecraft with mods ? (Y/N)")
                 if Minecraft_mod == "N":
                    LOGGER.info("tun tun tun tun; tin tin tit; tan tan tan tan ")
                    gamemenu = 0
                    os.system(r"put minecraft path here")
                 else:
                     LOGGER.info("Launching mods ...")
                     os.system(r"put curse forge path here")
             if gameorder == "exit()":
                 gamemenu = 0
             if gameorder == "CS2":
                 LOGGER.info("good suffering session with russians, bro")
                 os.system(r"put CS2 path here")
                 gamemenu = 0
             if gameorder == "Roblox":
                 LOGGER.info("...")
                 tm.sleep(3)
                 LOGGER.info("...")
                 tm.sleep(3)
                 LOGGER.info("why not ...")
                 os.system(r"put the roblox path here")
                 gamemenu = 0
    if order == "colony development assist":
        LOGGER.info("Welcome to the colony development assistant (not ai, just in python), type help for more info")
        coldevasist_st = 1
        coldevassistorder = "nothing, bro"
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
            if coldevassistorder == "database":
                databaseorder == input("Which data do you want ? (language, title")
                if "pyhton" in databaseorder:
                    databaseorder-python == input("which script do you want to keep ?")
        LOGGER.info ("error : bash : command not found !")
    if order == "app launcher":
        LOGGER.info ("Bash : Error, this command is not availlable on this computer !")
        #app_launch = input("Which app do you want to launch ?")
        #if app_launch == "internet":
            #os.system ("put internet.exe path here")
            #LOGGER.info ("state 2/2 finished !")
        if order == "computer info":
         screen_monitoring_while = 1
         #creating variables for the screen monitoring
         cpu_usage = psutil.cpu_percent(interval=1)
         cpu_usages = psutil.cpu_percent(interval=1, percpu=True)
         memory = psutil.virtual_memory()
         disk_usage = psutil.disk_usage('/')
         disk_usage = psutil.disk_usage('/')
         disk_usage = psutil.disk_usage('/')
         net_io = psutil.net_io_counters()
         #showing variables
         LOGGER.info(f"Utilisation du CPU : {cpu_usage}%")
         cpu_usages = psutil.cpu_percent(interval=1, percpu=True)
         for i, usage in enumerate(cpu_usages, 1):
              print(f"Cœur {i} : {usage}%")
         LOGGER.info(f"Utilisation RAM : {memory.percent}%")
         LOGGER.info(f"Utilisation du disque : {disk_usage.percent}%")
         LOGGER.info(f"Octets envoyés : {net_io.bytes_sent}")
         LOGGER.info(f"Octets reçus : {net_io.bytes_recv}")
         while screen_monitoring_while == 1:
             screen_monitoring_order = input("which part do you want to see in detail ?")
             if screen_monitoring_order == "help":
                LOGGER.info ("you can just type the name of the composant (cpu, RAM, internet,sensor, disk, general info) and, if it's a process, just type process name of the process ")
             if screen_monitoring_order == "cpu":
                cores_physiques = psutil.cpu_count(logical=False)
                cores_logiques = psutil.cpu_count(logical=True)
                LOGGER.info("Cœurs physiques :", cores_physiques)
                LOGGER.info("Cœurs logiques   :", cores_logiques)
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
                     LOGGER.info("error : your computer have any sensor !")
             if screen_monitoring_order == "general informations":
                boot_time = psutil.boot_time()
                print("Système démarré le :", datetime.datetime.fromtimestamp(boot_time))






