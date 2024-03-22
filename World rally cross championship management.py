import time
import os


class FunctionError(Exception):
    statement = "\u001b[31mEnter A valid Function"


def console_menu():
    print("\u001b[33m*" * 12, " World Rally Cross Championship Management ", "*" * 13)
    print("\u001b[34m-" * 70)
    print("\u001b[36m\tType ADD for adding driver details")
    time.sleep(0.5)
    print("\tType DDD for deleting driver details ")
    time.sleep(0.5)
    print("\tType UDD for updating driver details")
    time.sleep(0.5)
    print("\tType VCT for viewing the rally cross standings table ")
    time.sleep(0.5)
    print("\tType SRR for simulating a random race")
    time.sleep(0.5)
    print("\tType VRL for viewing race table sorted according to the date")
    time.sleep(0.5)
    print("\tType STF to save the current data to a text file")
    time.sleep(0.5)
    print("\tType RFF to load data from the saved text file")
    time.sleep(0.5)
    print("\tType ESC to exit the program")
    print("\u001b[34m-" * 70)
    time.sleep(1)


def user_command():
    while True:  # to repeat this loop till we get a valid function as an input
        command = input("\u001b[34mType the function :")
        command = command.strip()  # trims the command variable's value
        all_commands = ("ADD", "UDD", "DDD", "ESC", 'STF', 'VCT', 'SRR', 'VRL', 'RFF')  # contains all the functions
        # user can call
        try:  # checks the validity of user input/ command variables value
            if command.upper() not in all_commands:
                raise FunctionError
        except FunctionError as e:
            print(e.statement)
            continue  # to send the python interpreter to the beginning of the loop
        break
    print("\u001b[36m", command.upper())  # to tell the user which function is running now
    return command.upper()


def get_valid_racer_name(name_statement="\u001b[34mEnter Racer Full Name : "):
    r_name = " "  # to remove a warning, r_name to get a valid racer_name
    invalid_input = "True"
    while invalid_input == "True":  # To iterate until user enters a valid r_name
        r_name = input(name_statement)
        r_name = r_name.strip()
        full_r_name = r_name.split(" ")
        for name in full_r_name:
            if not name.isalpha():
                print("\u001b[31mInvalid Input! Enter a valid Racer Name, only include english letters \n Try again")
                invalid_input = "True"  # to make sure invalid_input is set to 'True', DON'T REMOVE
                break  # if a part of racer name is invalid don't need to check for the rest.
            invalid_input = "False"
    return r_name.strip().upper()


def get_valid_racer_age(age_statement="\u001b[34mEnter Racer's age : "):
    r_age = 17  # to remove a warning
    while True:  # to iterate until user enters  a valid input for driver age
        try:
            r_age = int(input(age_statement))
        except ValueError:
            print("\u001b[31mInvalid Input! Enter an integer value as Age.")
            continue
        if r_age >= 60:
            print("\u001b[31mDriver Too Old. Cannot participate in a race. Enter an Age between 18-60.")
            continue
        elif r_age < 18:
            print("\u001b[31mDriver Too Young. Cannot participate in a race. Enter a Age between 18-60.")
            continue
        elif r_age < 0:
            print("\u001b[31mAge cannot be negative, Enter a valid age")
            continue
        break  # if user input is valid to exit the loop
    return r_age


def get_valid_racer_current_points(points_statement="\u001b[34mEnter Racer's current points : "):
    c_points = 0  # To remove a warning
    while True:  # iterate until user enters a valid c_points
        try:  # checks the validity of c_points
            c_points = int(input(points_statement))
        except ValueError:
            print("\u001b[31mInvalid Input! Enter an integer value.")
            continue
        if c_points < 0:
            print("\u001b[31mCurrent points cannot be negative. Enter a valid point")
            continue
        break
    return c_points


def get_valid_racer_team(team_statement="\u001b[34mEnter Racer's team : "):
    r_team = " "  # to remove a warning
    invalid_input = "True"
    while invalid_input == "True":  # to iterate until user enters  a valid input for team
        r_team = input(team_statement)
        r_full_team_name = r_team.strip().split(" ")
        for i in r_full_team_name:
            if not i.isalnum():  # checks the validity of team
                print("""\u001b[31mInvalid Input! Enter a proper team name.
Team name cannot contain special characters """)
                invalid_input = "True"  # to make sure invalid_input is set to 'True', DON'T REMOVE
                break  # if a part of team name is invalid don't need to check for the rest.
            invalid_input = "False"
    return r_team.strip()


def get_valid_racer_car(car_statement="\u001b[34mEnter Racer's car : "):
    r_car = " "  # to remove a warning
    invalid_input = "True"
    while invalid_input == "True":
        r_car = input(car_statement)
        full_car_name = r_car.strip().split(" ")
        if not r_car[0].isalpha():  # to only check the first character in r_car
            print("\u001b[31mInvalid Input!!! Enter a valid car, first letter of the first word should be a letter.")
            continue
        for i in full_car_name:
            if not i.isalnum():
                print("\u001b[31mInvalid Input!!! Enter a valid car name")
                invalid_input = "True"  # to make sure invalid_input is set to 'True', DON'T REMOVE
                break  # if a part of car name is invalid don't need to check for the rest.
            invalid_input = "False"
    return r_car


def prompt_racer_details(d_name, d_age, d_car, d_team, d_current_points, n=""):  # n can be empty/'new'
    print("\t\u001b[33m1) Racer's ", n, "Full Name : ", d_name, sep="")
    time.sleep(0.5)
    print("\t2) Racer's ", n, " Age : ", d_age, sep="")
    time.sleep(0.5)
    print("\t3) Racer's ", n, " Car : ", d_car, sep="")
    time.sleep(0.5)
    print("\t4) Racer's ", n, " Team : ", d_team, sep="")
    time.sleep(0.5)
    print("\t5) Racer's ", n, " Current points : ", d_current_points, sep="")
    time.sleep(0.5)


def check_for_duplication_racer_name(d_name):
    for i in range(0, len(all_NS_racer_details)):
        if d_name == all_NS_racer_details[i][0]:
            print("\u001b[31mDetails of racer", d_name, "is already entered to the system,"
                                                        " but not saved. to save 'type STF' .")
            d_name = "Stored"
    if d_name != "Stored":
        with open("Racer_Details(draft).txt", "r") as f:
            for line in f:
                f.readline()
                # global S_racer_details_list  # to use in other functions(prompt_driver_details)
                S_racer_details_list = line.split(",")  #
                if S_racer_details_list[0] == d_name:
                    print("\u001b[31mDetails of racer", d_name, "is already saved in the 'Racer_Details(draft).txt' "
                                                                "files.")
                    print("Saved Racer details are ;")
                    prompt_racer_details(S_racer_details_list[0], S_racer_details_list[1],
                                         S_racer_details_list[2], S_racer_details_list[3],
                                         S_racer_details_list[4], n="")
                    d_name = "Stored"  # d_name is now a str called 'Stored'
                    break  # to exit loop if racer name is already saved, don't need to check rest of the lines
    return d_name


def add():
    while True:
        racer_name = get_valid_racer_name()
        racer_name = check_for_duplication_racer_name(racer_name)
        if racer_name == "Stored":
            break  # to exit add function if racer_name is already stored in Racer_Details(draft).txt
            # or in the NS-racer_detail_list
        age = get_valid_racer_age()
        team = get_valid_racer_team()
        car = get_valid_racer_car()
        current_points = get_valid_racer_current_points()
        single_racer_details = [racer_name, age, car, team, current_points]
        all_NS_racer_details.append(single_racer_details)  # NS - not saved
        break


def ddd():
    del_racer_name = get_valid_racer_name("\u001b[34mEnter racer name you wish to remove from the system : ")
    print("\u001b[33mSearching racer details ", end="")
    for i in range(0, 6):  # Improve user interface
        print(".", end="")
        time.sleep(0.5)
    print("\n")
    f = open("Racer_Details(draft).txt", "r")
    deleted = "False"  # to confirm that the driver was found and necessary details are deleted
    count = 0  # to get the exact line number in the file for the relevant driver details
    for line in f:
        S_single_racer_details = line.split(",")  # assigning a line in the file to a list (S- saved)
        if del_racer_name == S_single_racer_details[0]:
            with open("Racer_Details(draft).txt", "r") as f:
                all_lines_in_file = f.readlines()
            with open("Racer_Details(draft).txt", "w") as f:
                for number, all_lines_in_file in enumerate(all_lines_in_file):
                    if number != count:
                        f.write(all_lines_in_file)
                        deleted = "True"
            # referred, https://pynative.com/python-delete-lines-from-file/
            print("\u001b[33mSuccessfully deleted racer details.")
        count += 1
    if deleted == "False":
        print("\u001b[31mRacer Not Found.")
        if not all_NS_racer_details == []:  # to check whether user has saved all entered data to the draft file
            print("\u001b[31m Some entered racer details are not saved, Save it and try again. to save type 'stf'.")
    f.close()


def stf_racer_details():
    with open("Racer_Details.txt", "w") as f_1:  # overwrites the main file and saves the draft file data to the main
        f_1.write("Name,Age,Car,Team,Current_points")
        f_1.write("\n")
        with open("Racer_Details(draft).txt", "r") as file:
            for line in file:
                f_1.write(line)
    print("\u001b[33mRacer details are saved to main file 'Racer_Details.txt' ")


def stf_random_race_details():
    check_file = os.path.getsize("Random_Race_Details(draft).txt")  # checks whether any unsaved random race data
    # are there or not
    if check_file != 0:
        while True:
            save_main_file = input("\u001b[34mDo u want to save the Random race details to the main file "
                                   "'Random_Race_Details.txt' if so type 'YES', if not Type 'NO': ")
            if save_main_file.strip().upper() == "YES":
                with open("Random_Race_Details.txt", "w") as f:
                    with open("Random_Race_Details(draft).txt", "r") as file:
                        for line in file:
                            f.write(line)
                print("\u001b[33mRandom race details are saved in 'Random_Race_Details.txt' file.")
                break
            if save_main_file.strip().upper() == "NO":
                print("\u001b[33mRandom Race details are not saved to main file.")
                break
            else:
                continue


def stf():
    saved = "False"  # as a confirmation
    with open("Racer_Details(draft).txt", "a") as f:
        count = 0
        if len(all_NS_racer_details) > 0:  # (NS- not saved, S- saved)
            print("\u001b[33mSaving racer/(s) details ", end="")  # Improves user interface
            for i in range(0, 6):
                print(".", end="")
                time.sleep(0.5)
            print("\n")
            while count < len(all_NS_racer_details):  # repeats until all the nested lists are saved
                NS_single_racer_details = all_NS_racer_details[count]
                y = 0  # to use as the index place value for the single_racer_details list
                for i in NS_single_racer_details:
                    if y < 4:
                        f.write(str(i))
                        f.write(",")
                    else:
                        f.write(str(i))
                        f.write("\n")
                    y += 1
                count += 1
                prompt_racer_details(NS_single_racer_details[0], NS_single_racer_details[1],
                                     NS_single_racer_details[2], NS_single_racer_details[3],
                                     NS_single_racer_details[4])
                if count < len(all_NS_racer_details):
                    print("-" * 50)
            print("\u001b[33mSuccessfully saved the above racer/(s) details to 'Racer_Details(draft).txt' text file.")
            saved = "True"

            while True:  # to repeat until user enters a valid input
                save_to_main_file = input("""\u001b[34mDo you want to save these racer/(s) details in main files, 
    in need of resume capabilities
    >If so, Type 'yes' 
    >if not, Type 'no' : """)
                if save_to_main_file.strip().upper() == "YES":
                    if rff_called == "True":  # overwrites the main file cuz is already loaded to the system draft files
                        stf_racer_details()
                        stf_random_race_details()
                        break
                    else:
                        while True:  # to repeat til user enters a valid input
                            over_write = input("""\u001b[34mDo you want to overwrite or append to the main file
    >to overwrite type 'o'
    >to append type 'a' : """)
                            if over_write.strip().upper() == "O":
                                # overwrites the main file cuz user need to overwrite
                                stf_racer_details()
                                stf_random_race_details()
                                break
                            elif over_write.strip().upper() == "A":
                                # appends draft file data into the main file if it is
                                # not already saved in the main file
                                with open("Racer_Details(draft).txt", "r") as f_1:
                                    f_1.readline()
                                    for line in f_1:
                                        single_racer_details = line.split(",")
                                        with open("Racer_Details.txt", "r") as f_2:
                                            for line_main in f_2:
                                                single_racer_details_main = line_main.split(",")
                                                if single_racer_details_main[0] == single_racer_details[0]:
                                                    print("Racer detail of racer", single_racer_details[0], """is 
already stored in the main file 'Racer_Details.txt'""")
                                                    break
                                            else:
                                                with open("Racer_Details.txt", "a") as file_2:
                                                    file_2.write(line)
                                    print("\u001b[33mRacer details are saved to main file 'Racer_Details.txt' ")
                                check_file = os.path.getsize("Random_Race_Details(draft).txt")
                                if check_file != 0:
                                    while True:
                                        save_main_file = input("\u001b[34mDo u want to save the Random race details"
                                                               " to the main file 'Random_Race_Details.txt' "
                                                               "if so type 'YES',"
                                                               " if not Type 'NO': ")
                                        if save_main_file.strip().upper() == "YES":
                                            with open("Random_Race_Details.txt", "a") as f_4:
                                                with open("Random_Race_Details(draft).txt", "r") as file:
                                                    for line in file:
                                                        f_4.write(line)
                                            print("\u001b[33mRandom race details are saved in 'Random_Race_Details.txt'"
                                                  " file.")
                                            break
                                        if save_main_file.strip().upper() == "NO":
                                            print("\u001b[33mRandom Race details are not saved to main file.")
                                            break
                                        else:
                                            print("\u001b[31mInvalid Input! Try again.")
                                            continue
                                break
                            else:
                                print("Invalid Input! Try again")
                                continue
                        break
                elif save_to_main_file.strip().upper() == "NO":
                    print("\u001b[33mDetails are not saved to main files")
                    break
                else:
                    print("\u001b[31mInvalid Input! Try again")
                    continue
    if rff_called == "True":
        stf_random_race_details()
    elif rff_called == "False":
        check_file = os.path.getsize("Random_Race_Details(draft).txt")
        if check_file != 0:
            while True:
                save_main_file = input("\u001b[34mDo u want to save the Random race details"
                                       " to the main file 'Random_Race_Details.txt' "
                                       "if so type 'YES',"
                                       " if not Type 'NO': ")
                if save_main_file.strip().upper() == "YES":
                    with open("Random_Race_Details.txt", "a") as f_4:
                        with open("Random_Race_Details(draft).txt", "r") as file:
                            for line in file:
                                f_4.write(line)
                    print("\u001b[33mRandom race details are saved in 'Random_Race_Details.txt'"
                          " file.")
                    break
                if save_main_file.strip().upper() == "NO":
                    print("\u001b[33mRandom Race details are not saved to main file.")
                    break
                else:
                    print("\u001b[31mInvalid Input! Try again.")
                    continue
    else:
        print("\u001b[31mNo data entered to save to a file. Enter data before trying to save.")


def udd():
    upd_racer_name = ""  # to remove a warning
    change_racer_name = get_valid_racer_name("\u001b[34mEnter racer name you want to update : ")
    f = open("Racer_Details(draft).txt", "r")
    count = 0  # to get the line number in the file for the relevant racer details
    updated = "False"  # to confirm that the racer was found and necessary details are updated.
    for line in f:
        S_single_racer_details = line.split(",")  # assigning a line in the file to a list (S- saved)
        if change_racer_name == S_single_racer_details[0]:  # S_single_racer_details[0] is the name of
            # the relevant racer
            print("\u001b[33mSearching racer details ", end="")  # Improve user interface
            for i in range(0, 6):
                print(".", end="")
                time.sleep(0.5)
            print("\n")
            print("\u001b[36mSaved details of", S_single_racer_details[0], "are :")
            prompt_racer_details(S_single_racer_details[0], S_single_racer_details[1], S_single_racer_details[2],
                                 S_single_racer_details[3], S_single_racer_details[4], n=" ")
            invalid_input = "True"
            num_list = []  # to remove a warning
            while invalid_input == "True":  # till user enter a valid input for num variable
                num = input("""\u001b[34mEnter the respective number/(s) of the record/(s) you want to update "
(keep a space between number/(s) if you are entering multiple numbers) : """)
                num_list = num.split()  # we get the input/(s) as a string to make it a list
                for num in num_list:
                    try:
                        int_num = int(num)
                        if int_num < 1 or int_num > 5:
                            raise ValueError
                    except ValueError:
                        print('\u001b[31mInvalid input/(s)! Try again.')
                        invalid_input = "True"
                        break
                    invalid_input = "False"
                if invalid_input == "False":
                    break
                # num = str(num)  # to use split function (split function cannot be used for ints)
                # num_list = num.split()
            for num in num_list:  # num is as a str value
                if num == "1":
                    upd_racer_name = get_valid_racer_name("\u001b[34mEnter new Driver name : ")  # (upd- update)
                    upd_racer_name = check_for_duplication_racer_name(upd_racer_name)
                    if upd_racer_name == "Stored":
                        break
                    S_single_racer_details[0] = upd_racer_name
                elif num == "2":
                    S_single_racer_details[1] = str(get_valid_racer_age("\u001b[34mEnter new age : "))
                elif num == "3":
                    S_single_racer_details[2] = get_valid_racer_car('\u001b[34mEnter new car : ')
                elif num == "4":
                    S_single_racer_details[3] = get_valid_racer_team("\u001b[34mEnter new team : ")
                elif num == "5":
                    S_single_racer_details[4] = str(get_valid_racer_current_points("\u001b[34mEnter new current point : "))
                    # get current_points as a str value (to enter it to the list)
            if upd_racer_name == "Stored":
                break
            else:
                print("\u001b[33mUpdating racer details ", end="")  # Improve user interface
                for i in range(0, 6):
                    print(".", end="")
                    time.sleep(0.5)
                print("\n")
                racer_details_list = [S_single_racer_details[0], S_single_racer_details[1], S_single_racer_details[2],
                                      S_single_racer_details[3], S_single_racer_details[4]]
                with open("Racer_Details(draft).txt", "r") as f:
                    all_lines_in_file = f.readlines()
                with open("Racer_Details(draft).txt", "w") as f:
                    for number, all_lines_in_file in enumerate(all_lines_in_file):
                        if number != count:
                            f.write(all_lines_in_file)
                        elif number == count:
                            y = 0  # to use as the index place value for the driver_details_list
                            for num in racer_details_list:
                                if y < 4:
                                    f.write(str(num))
                                    f.write(",")
                                else:
                                    f.write(str(num))
                                    f.write("\n")
                                y += 1
                            updated = "True"
                            print("\u001b[33mSuccessfully updated driver details")
                            print("New details of", S_single_racer_details[0], "are :")
                            prompt_racer_details(S_single_racer_details[0], S_single_racer_details[1],
                                                 S_single_racer_details[2], S_single_racer_details[3],
                                                 S_single_racer_details[4], n="new")
                break
        count += 1
    if updated == "False" and upd_racer_name != "Stored":
        print("\u001b[31mRacer Not Found.")
        if not all_NS_racer_details == []:  # to check whether user has used the STF function and saved the data
            # user entered
            print("\u001b[31m Some entered racer details are not saved, Save it and try again.")
    f.close()


def save_new_total_point(r_name, Total_points):
    f = open("Racer_Details(draft).txt", "r")
    single_racer_details = ''  # to remove a warning
    count = 0
    for line in f:
        single_racer_details = line.split(",")
        if r_name == single_racer_details[0]:
            single_racer_details[4] = str(Total_points)
            break
        count += 1
    f.close()
    with open("Racer_Details(draft).txt", "r") as f:
        all_lines_in_file = f.readlines()
    with open("Racer_Details(draft).txt", "w") as f:
        for number, all_lines_in_file in enumerate(all_lines_in_file):
            if count != number:
                f.write(all_lines_in_file)
            else:
                for i in range(0, len(single_racer_details)):
                    if i < 4:
                        f.write(single_racer_details[i])
                        f.write(",")
                    else:
                        f.write(single_racer_details[i])
                        f.write("\n")


def srr():
    check_file = os.path.getsize("Racer_Details(draft).txt")
    if check_file == 0:
        print("Cannot generate a race without any racer, First Enter some racer details to generate a random race.")
    else:
        import random as r
        import datetime as dt
        race_name = input("Give a name for the race : ")
        race_name = "$$Race : " + race_name
        print("\u001b[33mGenerating a random race ", end="")  # Improves user interface
        for i in range(0, 6):
            print(".", end="")
            time.sleep(0.5)
        print("\n")
        date_duplicated = "True"
        random_date = "Date"  # to remove warning
        while date_duplicated == "True":
            start = dt.datetime(2020, 1, 1)
            end = dt.datetime.now()
            random_date = start + (end - start) * r.random()
            random_date = "Date : " + str(random_date)
            # print(random_date[0:17])
            # referred from Stackoverflow answered by Pieter bos
            with open("Random_Race_Details(draft).txt", "r") as f:  # check for date duplication
                for line in f:
                    S_single_race_detail = line
                    separate_single_race_details = S_single_race_detail.split(",")
                    if random_date[0:17] == separate_single_race_details[0]:
                        # random_date[0:17] gives out >> 'Date : YYYY-MM-DD'
                        break
                else:
                    date_duplicated = "False"
        race_destination = ["Nyirád", "Höljes", "Montalegre", "Barcelona", "Riga", "Norway"]
        venue = ""  # to remove a warning
        r.shuffle(race_destination)
        for element in race_destination:  # used a set to get a random venue
            venue = "$$Venue : " + element
            break  # Only wanted to get the 0 th index element
        S_all_racer_names = []
        S_all_racer_details = []
        with open("Racer_Details(draft).txt", "r") as f:
            f.readline()
            for line in f:
                S_single_racer_details = line.split(",")
                S_all_racer_names.append(S_single_racer_details[0])  # appending only the name
                S_all_racer_details.append(S_single_racer_details)  # appending all racer details
        r.shuffle(S_all_racer_names)  # shuffling the order of the list
        race_standings = S_all_racer_names  # race_standings list gives the place of each racer
        with open("Random_Race_Details(draft).txt", "a") as f:
            f.write(random_date[0:17])
            f.write(venue)
            f.write(race_name)  # writes users entered race name to the file
            # f.write(race_details_table_fields)
            f.write("***")
            position = 1
            for name in race_standings:
                count = 0  # to find the relevant racers details from S_all_racer_details
                while count < len(S_all_racer_details):
                    if name == S_all_racer_details[count][0]:
                        f.write(str(position))
                        f.write(",")
                        sublist_index = 0  # to get the necessary detail of a racer
                        while sublist_index <= 4:
                            if sublist_index == 4:
                                if position == 1:
                                    f.write("+10")
                                    f.write(",")
                                    total_current_points = int(S_all_racer_details[count][4]) + 10
                                    save_new_total_point(name, total_current_points)
                                    # updates the current_points in 'racer_details.txt' file
                                elif position == 2:
                                    f.write("+7")
                                    f.write(",")
                                    total_current_points = int(S_all_racer_details[count][4]) + 7
                                    save_new_total_point(name, total_current_points)
                                elif position == 3:
                                    f.write("+5")
                                    f.write(",")
                                    total_current_points = int(S_all_racer_details[count][4]) + 5
                                    save_new_total_point(name, total_current_points)
                                else:
                                    f.write("+0")
                                    f.write(",")
                            else:
                                f.write(S_all_racer_details[count][sublist_index])
                                f.write(",")
                            sublist_index += 1
                    count += 1
                f.write("####")
                position += 1
            f.write("\n")
        print("""\u001b[33mA random race was generated. 
The details regarding the race is saved in 'Random_Race_Details(draft).txt' file.""")
        # with open("Racer_Details(draft).txt","a+") as f:
        #     f.readline()


def vct():
    check_file = os.path.getsize("Racer_Details(draft).txt")
    if check_file == 0:
        print("\u001b[31mNo Racer/(s) details found, Enter some racer details to create a championship standing table")
    else:
        total_current_points = []
        all_racer_details = []
        with open('Racer_Details(draft).txt', 'r') as f:
            f.readline()
            for line in f:
                single_racer_details = line.split(",")
                single_racer_details[-1] = single_racer_details[-1].strip()
                total_current_points.append(single_racer_details[4])
                all_racer_details.append(single_racer_details)
        non_ordered_total_current_points = total_current_points.copy()
        set_total_points = set(total_current_points)
        total_current_points = list(set_total_points)
        for i in range(0, len(total_current_points)):
            for j in range(0, len(total_current_points)):
                if total_current_points[i] >= total_current_points[j]:
                    total_current_points[i], total_current_points[j] = total_current_points[j], total_current_points[i]
        table_title = "\u001b[33mVCT STANDING TABLE"
        print(table_title.center(96))
        gap = "  "  # defines the gap between fields
        print("\u001b[36m=" * 96)
        heading = f"{'Position':8s}{gap}{'Total Points':12s}{gap}{'Name':20s}{gap}{'Age':3s}{gap}" \
                  f"{'Car':15s}{gap}{'Team':15s}"
        print(heading)
        print("-" * 96)
        vct_position = 1
        for point in total_current_points:
            index = 0
            for j in non_ordered_total_current_points:
                if point == j:
                    single_racer_details = all_racer_details[index]
                    record = f"{vct_position:<8d}{gap}{single_racer_details[4]:^12s}{gap}" \
                             f"{single_racer_details[0]:<20s}{gap}{single_racer_details[1]:3s}{gap}" \
                             f"{single_racer_details[2]:<15s}{gap}{single_racer_details[3]:<15s}"
                    print(record)
                index += 1
            vct_position += 1
        print("=" * 96)


def vrl():
    check_file = os.path.getsize("Random_Race_Details(draft).txt")
    if check_file == 0:
        print("\u001b[31mRandom Race details not found, Race table is empty, Generate a random "
              "race before checking for race details")
    else:
        race_dates = []
        all_race_details = []
        racers_standings_records = []
        with open("Random_Race_Details(draft).txt", "r") as f:
            for line in f:
                S_race_details = line
                Single_full_race_details = S_race_details.split("***")
                # single race detail is separated to 2 elements in a list
                race_details = Single_full_race_details[0].split("$$")  # race detail list contain date/venue/race name
                all_race_details.append(race_details)
                racers_standings_records.append(Single_full_race_details[1])
                # appends each race standing records to the list
                race_dates.append(race_details[0])  # appends only race dates
        non_order_race_dates = race_dates.copy()
        for i in range(0, len(race_dates)):
            for j in range(0, len(race_dates)):
                if race_dates[i] > race_dates[j]:
                    race_dates[i], race_dates[j] = race_dates[j], race_dates[i]
        # gets the date in descending order
        # Referred YouTube https://www.youtube.com/watch?v=Sdjs2FQ8YRo&t=60s
        for date in race_dates:
            count = 0
            for j in non_order_race_dates:
                if date == j:
                    print("\u001b[33m",all_race_details[count][0], all_race_details[count][1],
                          all_race_details[count][2], sep="\t\t")
                    # prints the Date/Venue and Race name
                    # print("\n")
                    gap = "  "  # defines the gap between fields
                    print("\u001b[36m=" * 90)
                    heading = f"{'Position':8s}{gap}{'Name':20s}{gap}{'Age':3s}{gap}{'Car':15s}{gap}{'Team':15s}{gap}" \
                              f"{'Points':6s}{gap}"  # {'Total_current_points':20s}
                    print(heading)
                    print("\u001b[36m-" * 90)
                    single_racer_standing_records = racers_standings_records[count].split("####")
                    for y in range(0, len(single_racer_standing_records) - 1):
                        racer_detail = single_racer_standing_records[y].split(",")
                        record = f"{racer_detail[0]:^8s}{gap}{racer_detail[1]:<20s}{gap}{racer_detail[2]:3s}{gap}" \
                                 f"{racer_detail[3]:<15s}{gap}{racer_detail[4]:<15s}{gap}{racer_detail[5]:^6s}"
                        # "{gap}{racer_detail[6]:^20s}"
                        print(record)
                count += 1
            print("=" * 90)
            print("\n\n")


def rff():
    with open("Racer_Details(draft).txt", "w") as f:
        f.write("Name,Age,Car,Team,Current_points")
        f.write("\n")
        with open("Racer_Details.txt", "r") as file:
            file.readline()  # to ignore the first line
            for line in file:
                line_in_file = line
                f.write(line_in_file)

    with open("Random_Race_Details(draft).txt", "w") as f:
        with open("Random_Race_Details.txt", "r") as file:
            for line in file:
                line_in_file = line
                f.write(line_in_file)

    print("\u001b[33mData from saved text files have been loaded to the system.")


draft_file_1 = open("Racer_Details(draft).txt", "w")
draft_file_1.close()
draft_file_2 = open("Random_Race_Details(draft).txt", "w")
draft_file_2.close()
console_menu()
running_command = user_command()
# saved_all_driver_details_list = []
# S_racer_details_list = []
all_NS_racer_details = []
rff_called = "False"  # when saving data to files to confirm whether rff function was called or not
while running_command != "ESC":
    if running_command == "ADD":
        add()
    elif running_command == "DDD":
        ddd()
    elif running_command == "UDD":
        udd()
    elif running_command == "STF":
        stf()
        all_NS_racer_details = []  # empty the list after saving the data to the file
    elif running_command == "SRR":
        srr()
    elif running_command == "VRL":
        vrl()
    elif running_command == "VCT":
        vct()
    elif running_command == "RFF":
        all_NS_racer_details = []
        rff()
        rff_called = "True"
    print("\u001b[34m-" * 70)
    call_back_console_menu = input("To read the console menu again, Type 'Yes' : ")
    if call_back_console_menu.strip().upper() == "YES":
        print("\n\n")
        console_menu()
    running_command = user_command()
input("Close the Program.")
