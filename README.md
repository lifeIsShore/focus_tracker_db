# Focus Time Tracker

This is a Python Tkinter application for tracking focus sessions. The application allows users to start a session, record lap times, and terminate the session. Session data, including start time, laps, and end time, is saved in both JSON and MongoDB formats.

## Features

- **Start Focus Session**: Begin a session and record the start time.
- **Record Laps**: Track lap times during the session.
- **Terminate Session**: End the session and save data.
- **Data Persistence**: Save session data to a JSON file and MongoDB.

## Requirements

- Python 3.7 or newer
- Install the following libraries:
  ```bash
  pip install pymongo
  ```

## Setup

1. **Clone the repository** or copy the code into your project directory.

2. **Update MongoDB Connection**:
   Replace the MongoDB URI `"mongodb://localhost:27017/"` with your own MongoDB connection URI if needed.

3. **Define JSON File Path**:
   Modify the `json_file` path in the code to the location where you want to save the JSON file.

## Usage

1. **Start the Application**:
   Run the application by executing the following command:
   ```bash
   python focus_tracker_db.py
   ```

2. **Starting a Session**:
   Click on "Start Focusing" to begin a focus session. The start time will be displayed.

3. **Recording Laps**:
   During the session, click "Lap" to record each lap time. Each lap is saved under a new label.

4. **Terminating a Session**:
   Click "Terminate the Session" to end the session. This saves the session data in both JSON and MongoDB.

5. **Data Retrieval**:
   The session data is saved in:
   - A JSON file at the specified location.
   - The MongoDB collection specified in the code (`FocusTrackerDB` > `sessions`).

## Screenshots

1. **Main Screen**: 
     ![image](https://github.com/user-attachments/assets/ce50d5c3-9f70-4481-933c-e462d7d1486c)


2. **Session in Progress**: 
     ![image](https://github.com/user-attachments/assets/29837ebf-2c34-4898-87ae-253c3dda638c)


3. **Lap Recorded**: 
     ![image](https://github.com/user-attachments/assets/b95e609f-1c2b-4a2a-9040-c6578a53bf1f)


4. **MongoDB**:
  ![image](https://github.com/user-attachments/assets/828c74eb-4cd5-49c8-a50a-6e692c3db1e2)


5. **MongoDB Records**:
  ![image](https://github.com/user-attachments/assets/fb3b027d-b809-4428-9c7c-a7e0b65253ad)



## Code Structure

- **focus_tracker_db.py**: Main application file with the Tkinter GUI and MongoDB integration.
