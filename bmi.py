weight = input('Inserto your weight(kg): ')
height = input('Inserto your height(m): ')

bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
  print('Your BMI is', bmi, 'and you are underweight')
elif bmi >= 18.5 and bmi < 25:
  print('Your BMI is', bmi, 'and you are normal')
elif bmi >= 25 and bmi < 30:
  print('Your BMI is', bmi, 'and you are overweight')
elif bmi >= 30 and bmi < 35:
  print('Your BMI is', bmi, 'and you are obese')
else:
  print('Your BMI is', bmi, 'and you are clinically obese')