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

# question 1 'On my team, information is actively sought'
information_result = [x for x in culture_df['On my team, information is actively sought']]
information_ones = 0
information_twos = 0
information_threes = 0
information_fours = 0
information_fives = 0
information_sixes = 0
information_sevens = 0
for i in information_result:
    if int(i) == 1:
        information_ones += 1
    elif int(i) == 2:
        information_twos += 1
    elif int(i) == 3:
        information_threes += 1
    elif int(i) == 4:
        information_fours += 1
    elif int(i) == 5:
        information_fives += 1
    elif int(i) == 6:
        information_sixes += 1
    elif int(i) == 7:
        information_sevens += 1
        
d1 = {'Question':['On my team, information is actively sought'],'1': [information_ones],'2': [information_twos],'3': [information_threes],'4': [information_fours],'5': [information_fives],'6': [information_sixes],'7': [information_sevens]}
df = pd.DataFrame(data=d1)

# question 2 'On my team, I feel I can deliver bad news or news of a failure without retribution'
failure_result = [x for x in culture_df['On my team, I feel I can deliver bad news or news of a failure without retribution']]
failure_ones = 0
failure_twos = 0
failure_threes = 0
failure_fours = 0
failure_fives = 0
failure_sixes = 0
failure_sevens = 0
for i in failure_result:
    if int(i) == 1:
        failure_ones += 1
    elif int(i) == 2:
        failure_twos += 1
    elif int(i) == 3:
        failure_threes += 1
    elif int(i) == 4:
        failure_fours += 1
    elif int(i) == 5:
        failure_fives += 1
    elif int(i) == 6:
        failure_sixes += 1
    elif int(i) == 7:
        failure_sevens += 1
        
d2 = {'Question':'On my team, I feel I can deliver bad news or news of a failure without retribution','1': failure_ones,'2': failure_twos,'3': failure_threes,'4': failure_fours,'5': failure_fives,'6': failure_sixes,'7': failure_sevens}
df = df.append(d2, ignore_index=True)

# question 3 'On my team, responsibilities are shared'
responsibilities_result = [x for x in culture_df['On my team, responsibilities are shared']]
responsibilities_ones = 0
responsibilities_twos = 0
responsibilities_threes = 0
responsibilities_fours = 0
responsibilities_fives = 0
responsibilities_sixes = 0
responsibilities_sevens = 0
for i in responsibilities_result:
    if int(i) == 1:
        responsibilities_ones += 1
    elif int(i) == 2:
        responsibilities_twos += 1
    elif int(i) == 3:
        responsibilities_threes += 1
    elif int(i) == 4:
        responsibilities_fours += 1
    elif int(i) == 5:
        responsibilities_fives += 1
    elif int(i) == 6:
        responsibilities_sixes += 1
    elif int(i) == 7:
        responsibilities_sevens += 1
        
d3 = {'Question':'On my team, responsibilities are shared','1': responsibilities_ones,'2': responsibilities_twos,'3': responsibilities_threes,'4': responsibilities_fours,'5': responsibilities_fives,'6': responsibilities_sixes,'7': responsibilities_sevens}
df = df.append(d3, ignore_index=True)

# question 4 'On my team, cross-functional collaboration is encouraged and rewarded'
collab_result = [x for x in culture_df['On my team, cross-functional collaboration is encouraged and rewarded']]
collab_ones = 0
collab_twos = 0
collab_threes = 0
collab_fours = 0
collab_fives = 0
collab_sixes = 0
collab_sevens = 0
for i in collab_result:
    if int(i) == 1:
        collab_ones += 1
    elif int(i) == 2:
        collab_twos += 1
    elif int(i) == 3:
        collab_threes += 1
    elif int(i) == 4:
        collab_fours += 1
    elif int(i) == 5:
        collab_fives += 1
    elif int(i) == 6:
        collab_sixes += 1
    elif int(i) == 7:
        collab_sevens += 1
        
d4 = {'Question':'On my team, cross-functional collaboration is encouraged and rewarded','1': collab_ones,'2': collab_twos,'3': collab_threes,'4': collab_fours,'5': collab_fives,'6': collab_sixes,'7': collab_sevens}
df = df.append(d4, ignore_index=True)

# question 5 'On my team, failure leads to learning'
learning_result = [x for x in culture_df['On my team, failure leads to learning']]
learning_ones = 0
learning_twos = 0
learning_threes = 0
learning_fours = 0
learning_fives = 0
learning_sixes = 0
learning_sevens = 0
for i in learning_result:
    if int(i) == 1:
        learning_ones += 1
    elif int(i) == 2:
        learning_twos += 1
    elif int(i) == 3:
        learning_threes += 1
    elif int(i) == 4:
        learning_fours += 1
    elif int(i) == 5:
        learning_fives += 1
    elif int(i) == 6:
        learning_sixes += 1
    elif int(i) == 7:
        learning_sevens += 1
        
d5 = {'Question':'On my team, failure leads to learning','1': learning_ones,'2': learning_twos,'3': learning_threes,'4': learning_fours,'5': learning_fives,'6': learning_sixes,'7': learning_sevens}
df = df.append(d5, ignore_index=True)

# question 6 'On my team, new ideas are welcomed'
ideas_result = [x for x in culture_df['On my team, new ideas are welcomed']]
ideas_ones = 0
ideas_twos = 0
ideas_threes = 0
ideas_fours = 0
ideas_fives = 0
ideas_sixes = 0
ideas_sevens = 0
for i in ideas_result:
    if int(i) == 1:
        ideas_ones += 1
    elif int(i) == 2:
        ideas_twos += 1
    elif int(i) == 3:
        ideas_threes += 1
    elif int(i) == 4:
        ideas_fours += 1
    elif int(i) == 5:
        ideas_fives += 1
    elif int(i) == 6:
        ideas_sixes += 1
    elif int(i) == 7:
        ideas_sevens += 1
        
d6 = {'Question':'On my team, new ideas are welcomed','1': ideas_ones,'2': ideas_twos,'3': ideas_threes,'4': ideas_fours,'5': ideas_fives,'6': ideas_sixes,'7': ideas_sevens}
df = df.append(d6, ignore_index=True)
df.set_index('Question')

#https://www.geeksforgeeks.org/stacked-percentage-bar-plot-in-matplotlib/

df.plot(
    x = 'Question',
    kind = 'barh',
    stacked = True,
    title = 'Team Culture Check-Up',
    mark_right = True)

#df_total = df['1'] + df['2'] + df['3'] + df['4'] + df['5'] + df['6'] + df['7']
#df_rel = df[df.columns[1:]].div(df_total, 0)*100

#for n in df_rel:
#    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], df[n], df_rel[n])):
#        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', va = 'center', ha = 'center')

from itertools import cycle, islice
my_colors = list(islice(cycle(['#8b0000', '#cd5c5c', '#ffa500', '#ffff00', '#adff2f', '#7cfc00', '#006400']), None, len(df)))

df.plot(
    x = 'Question',
    kind = 'barh',
    stacked = True,
    title = 'Culture Check-Up',
    mark_right = True,
    color = my_colors)

df.plot.barh(stacked=True)
