import labstep

user = labstep.login('test@labstep.com','testpass')

def attachData(experiment):
  experiment.addComment('Here is the raw data','data/plate_data_raw.csv')
  experiment.addComment('Here is the processed data','data/plate_data_processed.csv')
  experiment.addComment('Here is the plot','data/plot.png')
  print('Data Uploaded!')

def attachDataToNewExperiment():
  experiment = user.newExperiment('Python Test')
  attachData(experiment)
    
def attachDataToExistingExperiment(user, experiment_id):
  experiment = user.getExperiment(experiment_id)
  attachData(experiment)