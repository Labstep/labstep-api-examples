import labstep

def attachData(experiment):
  experiment.addComment('Raw data from the plate reader','data/plate_data_raw.csv')
  experiment.addComment('Script used to analyse the data','analysis.py')
  experiment.addComment('Processed data','data/plate_data_processed.csv')
  experiment.addComment('Plot of processed data','data/plot.png')
  print('Data Uploaded!')

def attachDataToNewExperiment(user):
  experiment = user.newExperiment('Python Test')
  attachData(experiment)

