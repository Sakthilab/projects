print('''     
                _
               (  )         ,,,,,
                 \\         . .  ,
                  \\       | -   D
                  (._)     \__-  |
                             |   |
                 \\|_  , ,---- _ |----.
                  \__ ( (           /  )       _
                     | \/ \.   '  _.|  \     (  )
                     |  \ /(   /    /\_ \    //
                      \ /  (       / /  )   //
                           (  ,   / / ,   (_.)
                           |......\ |  \,
                          /  /     ) \---
                   b'ger /___/___^// ''')

print("------BMI CALCULATOR------")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = round(weight / height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, and you are Under Weight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, and you are Normal Weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, and you are Over Weight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, and you are Obese")
else:
    print(f"Your BMI is {BMI}, and you are Clinically Obese")
