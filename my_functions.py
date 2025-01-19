from datetime import datetime
import pandas as pd
import os
from tkinter import messagebox

START_DATE = "2024-11-28" # MAKE sure to change this when starting challenge

def start():
    choice = int(input("Service:\n"
                   "\t1. Body Weight tracker\n"
                   "\t2. Exercise tracker\n"
                   "\t3. Max reps tracker\n"
                   "\t4. Muscle Measurement Tracker\n"))
    while choice not in [1,2,3,4]:
        choice = int(input("Service:\n"
                       "\t1. Body Weight tracker\n"
                       "\t2. Exercise tracker\n"
                       "\t3. Max reps tracker\n"
                       "\t4. Muscle Measurement Tracker\n"))
    if choice == 1:
        body_weight()
    elif choice == 2:
        exercise()
    elif choice == 3:
        max_reps()
    else:
        measure()


def body_weight(mass):
    try:
        mass = float(mass)
    except:
        messagebox.showerror("Error", "Try again")
    truncated_mass = int(mass*10)/10
    current_hour = datetime.now().hour
    time_of_day = ""
    if 18 <= current_hour or current_hour < 4:
        time_of_day = "Night"
    else:
        time_of_day = "Day"
    df_new = pd.DataFrame({
        'date': [todays_date()],
        'day': [count_day()],
        'body_weight_kg': [truncated_mass],
        'time_of_day': [time_of_day]
    })
    file_name = './FitnessTracker/data/body_weight.csv'
    insert_file_exists(file_name, df_new)
    print("bw, APPEND SUCCESFUL!")


def exercise():
    # exercise = input(pull from table of exercises a to z using enumerate) exercise = dict[num]
    # difficulty = table again reference enumerate (exercise, difficulty [beginner,interm,adv] or [1,2,3,4])
    date = todays_date()
    days = count_day()
    # create a csv file pulling all exercises, and respective difficulty, primary exercise



def max_reps(*args):
    exercise_names = {
        0: "ceiling touches",
        1: "pushups",
        2: "pullups",
        3: "dips",
        4: "chinups",
        5: "squats",
        7: "plank hold"
    }
    date = todays_date()
    week = weeks_since(START_DATE)
    hold = 0
    file_name = './FitnessTracker/data/max_rep.csv'
    for index, value in enumerate(args):
        value = int(value)
        if index < 5:
            reps = int(value)
            df_new = max_reps_insert(date, week, exercise_names[index], reps)
            insert_file_exists(file_name, df_new)
        elif index == 6:
            hold += value*60
        else:
            hold += value
    df_new = max_reps_insert(date, week, exercise_names[7], hold)
    insert_file_exists(file_name, df_new)
    print("max reps, APPEND SUCCESFUL!")


def max_reps_insert(date, week, exercise, reps):
    df_new = pd.DataFrame({
        'date': [date],
        'week': [week],
        'exercise': [exercise],
        'reps': [reps]
    })
    return df_new

def measure(*args):
    muscle_parts = {
        0: "left_shoulders",
        1: "right_shoulders",
        2: "chest",
        3: "left_arms",
        4: "right_arms",
        5: "waist",
        6: "left_quad",
        7: "right_quad",
        8: "belly",
        9: "left_calves",
        10: "right_calves"
    }
    date = todays_date()
    week = weeks_since(START_DATE)
    file_name = './FitnessTracker/data/muscle_growth.csv'
    for index, value in enumerate(args):
        value = float(value)    # in cm
        df_new = measurement_insert(date, week, muscle_parts[index], value)
        insert_file_exists(file_name, df_new)
    print("max reps, APPEND SUCCESFUL!")


def measurement_insert(date, week, muscle, muscle_cm):
    df_new = pd.DataFrame({
            'date': [date],
            'week': [week],
            'muscle_part': [muscle],
            'circumference': [muscle_cm]
    })
    return df_new

def insert_file_exists(path, dataframe_new):
    file_name = path
    if os.path.exists(file_name):
        # Append without headers
        dataframe_new.to_csv(file_name, mode="a", index=False, header=False)
    else:
        # Write with headers
        dataframe_new.to_csv(file_name, mode="w", index=False, header=True)

def count_day():
    start_date = datetime.strptime(START_DATE, "%Y-%m-%d")
    # Get today's date
    today_date = datetime.today()
    # Calculate the difference in days
    day_count = (today_date - start_date).days
    return day_count

def todays_date():
    formatted_date = datetime.now().strftime("%Y-%m-%d")  # current date
    return formatted_date

def time_of_day():
    current_hour = datetime.now().hour
    time_of_day = ""
    if 18 <= current_hour or current_hour < 4:
        time_of_day = "Night"
    else:
        time_of_day = "Day"
    return time_of_day

def weeks_since(start_date):
    # Parse the input date if it's a string, otherwise assume it's a datetime object
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    # Get today's date
    today = datetime.today()
    # Calculate the difference in days
    days_difference = (today - start_date).days
    # Convert days to weeks (integer division)
    weeks_difference = days_difference // 7
    return weeks_difference