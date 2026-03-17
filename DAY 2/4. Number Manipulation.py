#ROUND

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height**2))

print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))


### ASSIGNMENT OPERATORS

score = 0

score += 1
print(score)

#f-string
print(f"Your score is {score}, your height is {height} and your weight is {weight}.")