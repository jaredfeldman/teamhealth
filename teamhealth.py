import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
#from scipy import stats
#import seaborn as sns
#import math
#import random
#import textwrap

# create dataframe from spreadsheet using pandas
culture_df_start = pd.read_csv("culturecheckup.csv", header= 0,
                        encoding= 'unicode_escape', names=['ID','Start time','Completion time','Email','Name','Which team do you contribute to?'
                                                          ,'On my team, information is actively sought'
                                                          ,'On my team, I feel I can deliver bad news or news of a failure without retribution'
                                                          ,'On my team, responsibilities are shared'
                                                          ,'On my team, cross-functional collaboration is encouraged and rewarded'
                                                          ,'On my team, failure leads to learning'
                                                          ,'On my team, new ideas are welcomed'
                                                          ,'Is there any additional information to help frame your submissions above? Examples?'])

#drop unused columns for sharing 6 likert responses
del culture_df_start["Email"]
del culture_df_start["Name"]
del culture_df_start["Is there any additional information to help frame your submissions above? Examples?"]
del culture_df_start["ID"]
del culture_df_start["Start time"]
del culture_df_start["Completion time"]
#del culture_df_start["Which team do you contribute to?"]

#drop null values to keep only rows with entries for questions
culture_df = culture_df_start.dropna()

#let's see that dataframe!
culture_df
