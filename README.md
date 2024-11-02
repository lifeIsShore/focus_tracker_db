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

1. **Main Screen**: Shows the initial screen with a "Start Focusing" button.
   - **Screenshot Tip**: Capture the application window showing only the "Start Focusing" button.

2. **Session in Progress**: Shows the screen after starting a session, displaying the start time and the "Lap" and "Terminate the Session" buttons.
   - **Screenshot Tip**: Capture the screen with the session in progress, showing the start time and available buttons.

3. **Lap Recorded**: Shows a lap recorded in the session, updating the status message with lap information.
   - **Screenshot Tip**: Capture the screen after recording at least one lap.

4. **Session Terminated**: Shows the final state after clicking "Terminate the Session," with a confirmation that data was saved to MongoDB.
   - **Screenshot Tip**: Capture the screen right after terminating the session to confirm that data is saved successfully.

## Code Structure

- **focus_tracker_db.py**: Main application file with the Tkinter GUI and MongoDB integration.
