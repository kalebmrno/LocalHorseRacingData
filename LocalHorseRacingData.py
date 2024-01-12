# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 07:01:25 2024

@author: Kaleb

LocalHorseRacingData.py 
A SIMPLE data plotting application made in Python by Kaleb Moreno

How to use: As script runs, you are presented with a VERY simple option menu in a cmd line/ terminal interface. 3 Options being to view existing horse data, add new data, or exit. Data already exists by default, you can add your own in the code or add new via interface. It all plots in a html file ready to be viewed.
Data input types: Horse Name - as name entails, Speed Index = SI - metric used in horse racing, LTE = Life Time Earnings - how much the horse has made over its lifetime of racing

"""


import pandas as pd
import plotly.express as px

#INITIAL DATA
data = {
    'Horse Name': [
        'Cat Daddys Lil Girl', 'RyansManOnTheMoon', 'GirlOnTheGo',
        'Flash Devine', 'Takiana Romanova B', 'Teana Fay',
        'Bevs Fast Lane', 'Cartels Star Daddy'
    ],
    'Speed Index': [102, 106, 96, 1, 93, 94, 1, 99],
    'Life Time Earnings': [565806, 410081, 174146, 129001, 192687, 176597, 103577, 166008]
}

#DATA FRAME FOR HORSE DATA
horse_data_df = pd.DataFrame(data)

# ADD NEW HORSE DATA FUNCTION
def add_new_horse():
    name = input("Enter horse name: ")
    speed_index = input("Enter speed index (use 1 for UNKNOWN): ")
    earnings = input("Enter life time earnings: ")

    # ADD NEW ENTRY TO DATAFRAME
    new_entry = {'Horse Name': name, 'Speed Index': int(speed_index), 'Life Time Earnings': int(earnings)}
    return new_entry

# SAVE DATA TO CSV FUNCTION
def save_data(df):
    df.to_csv('horse_data.csv', index=False)
    print("Data saved successfully.")
    
    
    

# DASHBOARD CREATION FUNCTION_________________________________________________________________________________________
def create_dashboard(df):
    fig = px.scatter(df, x='Speed Index', y='Life Time Earnings',
                     size='Life Time Earnings', color='Life Time Earnings',
                     hover_name='Horse Name', hover_data=['Horse Name', 'Speed Index', 'Life Time Earnings'],
                     title='Quarter Horse Racing: Earnings Dashboard')
    fig.show()
    fig.write_html('horse_earnings_dashboard.html')
    print("Dashboard saved as HTML.")


#_____________________________________________________________________________________________________________________
# MAIN LOOP CMD LINE INTERFACE________________________________________________________________________________________
while True:
    print("\nHorse Racing Data Application")
    print("1. View Dashboard")
    print("2. Add New Horse Data")
    print("3. Exit")
    user_choice = input("Enter your choice (1, 2, or 3): ")

    if user_choice == '1':
        #DASHBOARD CREATION AND VIEWING
        create_dashboard(horse_data_df)
    elif user_choice == '2':
        #PROMPTS TO ADD NEW DATA
        new_horse = add_new_horse()
        horse_data_df = horse_data_df.append(new_horse, ignore_index=True)
        save_data(horse_data_df)
        create_dashboard(horse_data_df)  #UPDATE THE DASH
    elif user_choice == '3':
        #EXIT OPTION
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
#_____________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________

