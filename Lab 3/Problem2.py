import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from csv
df = pd.read_csv('train.csv')
# All columns except the 'TYPE' label
symptoms = df.columns[:-1]  
# map the disease
typesMapping = {'ALLERGY': 0, 'COVID': 1, 'COLD': 2, 'FLU': 3}
df['TYPE'] = df['TYPE'].map(typesMapping)
reverseTypeMapping = {v: k for k, v in typesMapping.items()}
# Create scatter plots for each
for symptom in symptoms:
    plt.scatter(df[symptom], df['TYPE'])
    plt.title(f'Scatter plot between {symptom} and TYPE')
    plt.xlabel(symptom)
    plt.ylabel('Disease')
    # Setup of the y-ticks to be the disease names
    plt.yticks(ticks=list(reverseTypeMapping.keys()), labels=list(reverseTypeMapping.values()))
    plt.show()

    

#3. --------------------------------------------------
# Load data from csv
trainDf = pd.read_csv('train.csv')
testDf = pd.read_csv('test.csv')

# Create a dictionary for the type mapping
typesMapping = {'ALLERGY': 0, 'COVID': 1, 'COLD': 2, 'FLU': 3}

# Convert 'TYPE' column to numerical values for both main and test datasets
trainDf['TYPE'] = trainDf['TYPE'].map(typesMapping)

# Function to calculate Euclidean distance
def euclideanDistance(row1, row2):
    return np.sqrt(np.sum((row1 - row2) ** 2))

# Prepare the output list
assigned_labels = []

# Iterate over each entry in the test dataset
for _, test_row in testDf.iterrows():
    min_distance = float('inf')  # Initialize minimum distance to infinity
    assigned_label = None
    
    # For each test entry, calculate the distance with each entry in the main dataset
    for _, main_row in trainDf.iterrows():
        # Calculate Euclidean distance between the symptoms of test and main data
        distance = euclideanDistance(test_row[:-1], main_row[:-1])
        
        # If this distance is smaller, store it and assign the current main_row's label
        if distance < min_distance:
            min_distance = distance
            assigned_label = main_row['TYPE']
    
    
    assigned_labels.append(assigned_label)


#4. --------------------------------------
# Convert numerical labels back to string labels using reverse mapping
finalData = testDf.copy()
reverseTypeMapping = {v: k for k, v in typesMapping.items()}
assigned_labels = [reverseTypeMapping[label] for label in assigned_labels]

# Add the assigned labels to the test dataset
finalData['Assigned Label'] = assigned_labels

print(finalData)


#6.------------------------------------------
Part1 = trainDf.copy()  # Data with labels
Part2 = trainDf.drop(columns=['TYPE'])


#7.------------------------------------------
count = 0
totalCount = len(Part2)

for _, row in Part2.iterrows():
    minDistance = float('inf')
    assignedLabel = None

    for _, mainRow in Part1.iterrows():
        distance = euclideanDistance(row, mainRow[:-1])

        if distance < minDistance:
            minDistance = distance
            assignedLabel = mainRow['TYPE']

    if assignedLabel == mainRow['TYPE']:
        count += 1

percentage = (count/totalCount) * 100
print("Correctly assigned label: ", percentage)


#8.--------------------------------------------------
def recursive_nearest_neighbor(test_row, train_data, index=0, closest_label=None, min_distance=float('inf')):
    if index >= len(train_data):
        return closest_label
    
    main_row = train_data.iloc[index]
    distance = euclidean_distance(test_row, main_row[:-1])  # Exclude label
    
    if distance < min_distance:
        min_distance = distance
        closest_label = main_row['TYPE']
    
    return recursive_nearest_neighbor(test_row, train_data, index + 1, closest_label, min_distance)

# Applying the recursive function to Part2
correct_count = 0
total_count = len(Part2)

for _, test_row in Part2.iterrows():
    assigned_label = recursive_nearest_neighbor(test_row, Part1)
    if assigned_label == test_row['TYPE']:  # If you have original labels for Part2, ensure they are compared correctly
        correct_count += 1

accuracy = (correct_count / total_count) * 100
print("Correctly assigned label: ", accuracy)






