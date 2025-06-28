weight_lb = int(input("Please Enter Your weight in pounds:  "))  # weight in pounds
height_ft = float(input("Please Enter Your Height in Feet: "))  # height in feet

# Convert height to inches
height_in = height_ft * 12

# Calculate BMI
bmi = (weight_lb * 703) / (height_in ** 2)

# Interpret BMI
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
