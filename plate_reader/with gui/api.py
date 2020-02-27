import labstep

user = labstep.login('test@labstep.com','testpass')

def attachData(experiment):
  experiment.addComment('Raw data from the plate reader','data/plate_data_raw.csv')
  experiment.addComment('Script used to analyse the data','analysis.py')
  experiment.addComment('Processed data','data/plate_data_processed.csv')
  experiment.addComment('Plot of processed data','data/plot.png')
  print('Data Uploaded!')

def attachDataToNewExperiment():
  experiment = user.newExperiment('Python Test')
  attachData(experiment)
    
def attachDataToExistingExperiment(experiment):
  experiment = user.getExperiment(experiment.id)
  attachData(experiment)

def getExperiments():
  return user.getExperiments(count=5)
