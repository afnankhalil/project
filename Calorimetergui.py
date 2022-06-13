from breezypythongui import EasyFrame

class calori(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        
        #it is initializing the list so that when the user input the diet, the food is going to enter this list.
        self.food_list = []
        
        #this adding the label 'Diet' in the gui and it is also setting the position the label.
        self.addLabel(text="Diet", row=0, column=0)
        #it is adding the field where the user can enter their diet and it is setting the position of the field.
        self.diet = self.addTextField(text="enter your diet", row=0, column=2, width=20)
        
        #this adding the label 'weight' in the gui and it is also setting the position the label.
        self.addLabel(text="Weight", row=2, column=0)
        #it is adding the field where the user can enter their weight and it is setting the position of the field.
        self.weight = self.addFloatField(value="enter your weight", row=2, column=2, width=20)
        
        #this adding the label 'height' in the gui and it is also setting the position the label.
        self.addLabel(text="Height", row=4, column=0)
        #it is adding the field where the user can enter their height and it is setting the position of the field.
        self.height = self.addFloatField(value="enter your height in meters", row=4, column=2, width=20)
        
        #it is adding the buttons to the gui so that when the user presses the button the program starts working.
        self.addButton(text="Calculate", row=6, column=2, command=self.calculate)
        self.addButton(text="Input", row=1, column=2, command=self.input)
        
    #this function puts the food that the user inputs inside the food_list.
    def input(self):
        self.food_list.append(self.diet.getText())
    
    #this function calculates and gives out the result.
    def calculate(self):
        #it is opening the text file where there is a list of foods and calories of those foods.
        myfile = open("textfile_caloriemeter","r")
        data = {}
        for line in myfile:
            #it is taking the data from the text file and putting all the data in the data dictionary.
            data[line.split()[0]] = int(line.split()[2])
        
        temp = 0
        food = ""
        for x in self.food_list:
            food = x
            for i in [food]:
                #it is calculating the calorie intake for the specific day
                temp = temp + data[i]
       
        weight = self.weight.getNumber()
        height = self.height.getNumber()
        #it is calculating the body mass index.
        BMI = weight/(height**2)
    
    #these if else statements shows that there is a certain condition.
    #if the conditions are met then the calori intake and BMI is gonna be shown in the message box.
    #Depending on the BMI the program is going to show if the user is underweight or healthy or overweight or obese in the message box.  
        if BMI < 18.5:
            self.messageBox(title="result", message="your BMI is " +str(BMI) + "\nthe amount of calorie intake today is " +str(temp) + "\nyou are underweight", width=30, height=20)
        
        elif 18.5<=BMI<=24.9:
            self.messageBox(title="result", message="your BMI is " +str(BMI) + "\nthe amount of calorie intake today is " +str(temp) + "\nyou are healthy", width=30, height=20)
        
        elif 25<=BMI<=29.9:
            self.messageBox(title="result", message="your BMI is " +str(BMI) + "\nthe amount of calorie intake today is " +str(temp) + "\nyou are overweight", width=30, height=20)
        
        elif BMI >= 30:
            self.messageBox(title="result", message="your BMI is " +str(BMI) + "\nthe amount of calorie intake today is " +str(temp) + "\nyou are obese", width=30, height=20)
    
calori().mainloop()
