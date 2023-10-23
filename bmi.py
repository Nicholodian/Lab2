def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #Add code here to calculate BMI
    bmi = weight/(height * height)
    #Add code here to display calculate BMI
    print(bmi)
    if bmi< 18.5:
        print("Under Weight")
    elif bmi>= 18.5:
        print("Normal Weight")
    elif bmi<= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")


calculate_bmi(weight=57, height=1.73)

