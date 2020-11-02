'''
Plots electron lifetime against elapsed time for SingleCube detector.  Required input is csv file with the following columns(0s in estimate & uncertainty columns only to show number of decimal places):

|datetime           |estimate|uncertainty|
|mm-dd-yyyy hh:mm:ss|0.00    |0.00       |

Usage: python3 plotLifetime.py filename.csv
'''

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys

def plot_lifetime(df):
    #prepare data 
    a = df.index.tolist()
    b = df['estimate'].tolist()
    c = df['uncertainty'].tolist()

    #format error bar caps
    plt.figure(figsize=(12,5))
    (_, caps, _) = plt.errorbar(a, b, yerr=c, fmt='o', markersize=4, capsize=4, linestyle='None')
    for cap in caps:
        cap.set_markeredgewidth(1)

    #plot
    plt.title('SingleCube Electron Lifetime')
    plt.xlabel('Date(mm-dd hh)')
    plt.ylabel('Lifetime(ms)')
    plt.ylim(ymin=0)
    plt.show()

def main(*args):
    
    #load csv (after downloading google sheets as csv)
    in_file = args[0]
    df = pd.read_csv(in_file, parse_dates=['datetime'])
    df['datetime'] = pd.to_datetime(df['datetime'])
    df  = df.set_index('datetime')
    return df
    

if __name__ == '__main__':
    df = main(*sys.argv[1:])
    plot_lifetime(df)
