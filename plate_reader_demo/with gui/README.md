# Plate Reader Integration With GUI Example

This basic example can be set up to watch multiple folders on a computer connected to the plate reader. When a csv is saved to a watched folder, it prompts the user to select an experiment from Labstep then runs analysis on the data and attaches the processed data to the selected experiment, along with a plot, the raw data and the analytical script used.

## Usage

1. Navigate to this folder.

2. Install all dependancies `pip install -r requirements.txt`.

2. In `users.py` enter the usernames, apikeys and path to the folder to watch for each user.

3. Run `python main.py`. You should see the GUI launch.

4. Add a csv to the watched folder (see `data/example_data.csv` for an example of the shape required)

5. Select an Experiment from the GUI.

5. Click 'Open' to go to the experiment.

## Code Structure

`users.py` - contains an array of user credentials along with the folder path each user wants to watch.
`analysis.py` - module that performs the analysis on the raw data from the plate reader.
`api.py` - module that interacts with the labstep api. Attaches the data to the selected labstep experiment.
`gui.py` - code for the user interface that allows you to select the experiment you want to attach to.
`main.py` - this is the script that controls everything. Initialises the folder watcher for each user. 