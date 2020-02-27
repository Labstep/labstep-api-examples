import pandas as pd
import statistics
import matplotlib
import matplotlib.pyplot as plt

plt.ioff()
matplotlib.use('Agg')

def analyzeData(filepath):
    plate_info = pd.read_csv(filepath)
    plate_info = plate_info.iloc[1:8,0]
    plate_data = pd.read_csv(filepath, header=13)
    plate_data = plate_data.iloc[:8, 0:13]
    plate_data = plate_data.set_index('Unnamed: 0')
    plate_data = plate_data.rename_axis("")
    
    plate_data_raw = plate_data.astype(float)
    plate_data_raw.to_csv('data/plate_data_raw.csv')
    
    plate_data_processed = plate_data_raw-(statistics.mean(plate_data_raw.iloc[:,11]))
    plate_data_processed.to_csv('data/plate_data_processed.csv')
    
    times = []
    ods = []
    for i in range(10):
        times.append(i)
        ods.append(statistics.mean(plate_data_processed.iloc[:,i]))
        
    fig = plt.figure()
    plt.plot(times, ods)
    fig.savefig('data/plot.png')