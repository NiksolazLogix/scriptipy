# Create 2 new lists height and weight
height = [1.69]
weight = [82.4]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Print out the type of np_height
print(type(np_height))
print(type(np_weight))

# Calculate bmi
'''
BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
'''
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

if bmi <= 18.5:
    print("Sottopeso")
elif bmi > 18.5 and bmi <= 25:
    print("Normopeso")
elif bmi > 25 and bmi <= 30:
    print("Sovrapeso")
elif bmi > 30:
    print("Obeso")

