# SCLifetime
Tools to measure LAr purity in the SingleCube detector.

To plot electron lifetime as a function of time, download Google sheet containing data as a csv file.  The sheet should contain columns of the following format (additional columns are fine):

```|datetime|estimate|uncertainty|```

```|mm-dd-yyyy hh:mm:ss|0.00    |0.00       |```

Once downloaded, run the command

```$ python3 plotLifetime.py <filename.csv>```

This will result in a plot of electron lifetime against time.  
