import matplotlib.pyplot as plt 
import pandas as pd 

# df = pd.read_csv('population_by_country_2020.csv')


# print(df.dtypes)


# list1 = df['Country (or dependency)'].values.tolist()
# list2 = df['Population (2020)']
# plt.scatter(list1[:10], list2[:10])
# plt.plot(list2[:10]) 
# plt.show()

# 1. ------------------------------------------
# read the csv and make dataframe
df = pd.read_csv("dailySteps_merged.csv")

list1 = df['StepTotal'].values.tolist()
list2 = df['ActivityDay'].values.tolist()


plt.plot(list2[:10], list1[:10], marker = 'o')
plt.xlabel('Date')
plt.ylabel('Total Steps')
# plt.xticks(rotation=45, ha='right')  # Rotate labels 45 degrees
plt.show()
#---------------------------------------------


#2.-------------------------------------------
# read the csv and make dataframe
df = pd.read_csv("dailyActivity_merged.csv")

list1 = df['TotalDistance'].values.tolist()
list2 = df['ActivityDate'].values.tolist()


plt.bar(list2[:10], list1[:10])
plt.xlabel('Date')
plt.ylabel('Total Distance')
# plt.xticks(rotation=45, ha='right')  # Rotate labels 45 degrees
plt.show()
#---------------------------------------------


#3.-------------------------------------------
# read the csv and make dataframe
df = pd.read_csv("sleepDay_merged.csv")

TimeInBed = df['TotalTimeInBed'].values.tolist()
days = df['SleepDay'].values.tolist()

plt.scatter(days[:15], TimeInBed[:15])
plt.ylabel('Minutes Sleeping')
plt.xlabel('Date')
plt.xticks(rotation=20)
# plt.xticks(rotation=45, ha='right')  # Rotate labels 45 degrees
plt.show()
#---------------------------------------------


#4.-------------------------------------------
# read the csv
df = pd.read_csv('hourlySteps_merged.csv')

# Filter the data to only include the steps for April 12, 2016
df_filtered = df[df['ActivityHour'].str.contains('4/12/2016')]

# Extract the hours and steps into separate variables
activityHours = df_filtered['ActivityHour'].values.tolist()
steps = df_filtered['StepTotal'].values.tolist()

# # Plot the pie chart
plt.pie(steps, labels=activityHours)

# Add a title to the chart
plt.title('Distribution of Steps by Hour on 12th April 2016')

plt.show()
#---------------------------------------------

