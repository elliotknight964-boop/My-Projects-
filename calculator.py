def calculate(x, y, z): 
    while True: 
        if y == "+": 
            result = x + z
            print(result)  
            break          
        elif y == "-": 
            result = x - z
            print(result)     
            break      
        elif y == "*": 
            result = x * z
            print(result) 
            break          
        elif y == "/": 
            result = x / z
            print(result) 
            break 
        
x = float(input("First number: "))
y = input("Operation: ")
z = float(input("Second number: ")) 

calculate(x, y, z) 
