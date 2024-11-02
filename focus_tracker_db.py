import tkinter as tk
from datetime import datetime
import pandas as pd
import os
import json
from pymongo import MongoClient

# Global variables
focus_data = []  # Stores all the focus session data
session_data = {}  # Temporarily stores data for each session
start_time = None
lap_counter = 0
json_file = r'C:\Users\ahmty\Desktop\Python\focus_tracker\Focus_tracker\database\focus_sessions_v3.json'  # JSON dosyasının tam yolu

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # MongoDB bağlantısı
db = client["FocusTrackerDB"]  # Veritabanı adı
collection = db["sessions"]  # Koleksiyon adı

# Function to handle the first button click (Start Focusing)
def start_focusing():
    global start_time, session_data, lap_counter

    start_time = datetime.now()
    day_str = start_time.strftime("%A")  # Example: Sunday
    start_date_str = start_time.strftime("%d-%b-%y")  # Example: 20-Oct-24
    start_time_str = start_time.strftime("%H:%M:%S")  # Example: 12:51:44
    
    # Initialize the session data
    session_data = {
        "Day": day_str,  # Store the day
        "Start Time": start_date_str,
        "Start DateTime": start_time_str  # Start time for the session
    }
    
    label_status.config(text="Session started at: " + start_time_str)
    
    # Change buttons after starting the session
    btn_start.pack_forget()
    btn_lap.pack(pady=10)
    btn_terminate.pack(pady=10)
    
    lap_counter = 1  # Reset lap counter for the new session

# Function to record each lap time
def lap_click():
    global lap_counter

    lap_time = datetime.now().strftime("%H:%M:%S")  # Only the time
    session_data[f"Lap #{lap_counter}"] = lap_time  # Dynamically add lap time
    label_status.config(text=f"Lap {lap_counter} recorded at: " + lap_time)
    
    lap_counter += 1

# Function to handle session termination
def terminate_session():
    global session_data, focus_data

    # Record the end time
    end_time = datetime.now().strftime("%H:%M:%S")
    session_data["End Time"] = end_time  # Bitiş zamanını ekliyoruz
    
    # Save the session data
    focus_data.append(session_data)
    save_to_json()  # Save to JSON
    save_to_mongodb(session_data)  # Save to MongoDB

    # Reset the application state
    reset_session()

    # Exit the application and close the window
    root.quit()
    root.destroy()  # This line will close the Tkinter window


# Function to save all session data to a JSON file
def save_to_json():
    global focus_data, json_file

    # Check if the JSON file already exists
    if os.path.exists(json_file):
        # If it exists, append the new data to the existing file
        with open(json_file, 'r') as f:
            existing_data = json.load(f)
        
        # Combine existing data with new data
        existing_data.extend(focus_data)
        
        with open(json_file, 'w') as f:
            json.dump(existing_data, f, indent=4)
    else:
        # If not, create a new file and write the data
        with open(json_file, 'w') as f:
            json.dump(focus_data, f, indent=4)

    # Clear focus_data after saving to avoid duplicates
    focus_data.clear()

# Function to save the session data to MongoDB
def save_to_mongodb(session):
    try:
        collection.insert_one(session)
        print("Session saved to MongoDB.")
    except Exception as e:
        print(f"An error occurred while saving to MongoDB: {e}")

# Function to reset the session variables and buttons
def reset_session():
    global session_data, lap_counter

    session_data = {}
    lap_counter = 0
    
    # Reset the buttons and labels
    btn_lap.pack_forget()
    btn_terminate.pack_forget()
    btn_start.pack(pady=10)
    label_status.config(text="Click to start focusing")

# Tkinter setup
root = tk.Tk()
root.title("Focus Time Tracker")

label_status = tk.Label(root, text="Click to start focusing", font=("Arial", 14))
label_status.pack(pady=20)

# Start focusing button
btn_start = tk.Button(root, text="Start Focusing", font=("Arial", 12), command=start_focusing)
btn_start.pack(pady=10)

# Lap button (Initially hidden)
btn_lap = tk.Button(root, text="Lap", font=("Arial", 12), command=lap_click)

# Terminate the session button (Initially hidden)
btn_terminate = tk.Button(root, text="Terminate the Session", font=("Arial", 12), command=terminate_session, fg="red")

# Start the application loop
root.mainloop()

# After closing the application, restart with default state
reset_session()
