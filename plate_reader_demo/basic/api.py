import labstep

def uploadDataToLabstep(user):
  user = labstep.authenticate(user['username'],user['apikey'])
  experiment = user.newExperiment('Python Test')
  experiment.addComment('Raw data from the plate reader','cache/plate_data_raw.csv')
  experiment.addComment('Script used to analyse the data','analysis.py')
  experiment.addComment('Processed data','cache/plate_data_processed.csv')
  experiment.addComment('Plot of processed data','cache/plot.png')
  print('Data Uploaded!')

  
