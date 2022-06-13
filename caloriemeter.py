def caloriemeter():
    myfile = open("textfile_caloriemeter","r")
    data = {}
    for line in myfile:
        #it is taking the data from the text file and putting all the data in the data dictionary.
        data[line.split()[0]] = int(line.split()[2])
    
    food_list = []
    while True:
        diet = input("enter your diet or enter '' to quit: ")
        #it is telling that if the user inputs "" then the loop will break
        if diet == '':
            break        
        #it is entering all the user input in the food_list 
        food_list.append(diet)

    temp = 0
    food = ""
    for x in food_list:
        food = x
        for i in [food]:
            #it is calculating the calorie intake for the specific day
            temp = temp + data[i]
    
    weight = float(input("enter your weight: "))
    height = float(input("enter your height in meters: "))
    #it is calculating the body mass index.
    BMI = weight/(height**2)
    
    if BMI < 18.5:
        print("your BMI is " +str(BMI))
        print("the amount of calorie intake today is " +str(temp))
        print("you are underweight")
     
    elif 18.5<=BMI<=24.9:
        print("your BMI is " +str(BMI))
        print("the amount of calorie intake today is " +str(temp))
        print("you are healthy")
        
    elif 25<=BMI<=29.9:
        print("your BMI is " +str(BMI))
        print("the amount of calorie intake today is " +str(temp))
        print("you are overweight") 
        
    elif BMI >= 30:
        print("your BMI is " +str(BMI))
        print("the amount of calorie intake today is " +str(temp))
        print("you are obese")
    
    
print(caloriemeter())

        