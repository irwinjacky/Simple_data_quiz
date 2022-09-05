#Susan's weight in Kilograms
Weight = 60
#Susan's height in meters
Height = 1.58
# uses the weight and height variable to find the BMI
BMI = Weight/(Height * Height)
#Rounds Susan's BMI to the nearest 100th place
BMI = round(BMI, 2)
#Prints the value of Susan's BMI
print(BMI)
#sets up the text to give information in a format of a sentence
txt = "Susan has a BMI of {}."
#Prints sentence "Susan has a BMI of 24.03."
print(txt.format(BMI))
