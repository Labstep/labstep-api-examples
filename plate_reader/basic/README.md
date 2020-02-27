## Basic Plate Reader Integration Example

This basic example can be set up to watch multiple folders on a computer connected to the plate reader.

When a csv is saved to a watched folder, it automatically runs and analysis on the data and uploads processed data to labstep, along with a plot, the raw data and the analytical script used.

1. Install all dependancies

2. In `users.py` enter the usernames, apikeys and path to the folder to watch for each user.

3. Navigate to the folder containing `master.py` and run the script. 

4. Add a csv to the watched folder.

5. Login to your Labstep account.

6. Go to Experiments.

7. Click on the 'Python Test' experiment that was just created and go to 'Results / Notes'.