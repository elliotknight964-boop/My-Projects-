def add_item(items, shopping_cart): 
    user_choice = input("Pick an item: ").lower()
    while True: 
        if user_choice in items: 
            shopping_cart.append(user_choice) 
            additional = input("Would you like to add anything else? ").lower()
            if additional == "yes": 
                user_choice = input("Pick an item: ").lower()
            elif additional == "no":                 
                print("Here is your shopping cart:")   
                for item in shopping_cart:
                    print(item.title())     

                return shopping_cart                     
        else:
            print("Sorry we don't stock that item") 
            additional = input("Would like to add something else? ").lower()
            if additional == "yes": 
                user_choice = input("Pick an item: ").lower()
            elif additional == "no": 
                print("Here is your shopping cart:")
                for item in shopping_cart: 
                    print(item.title())

                return shopping_cart 
               
items = ['milk', 'bread', 'eggs', 'chicken', 'potatoes', 'bannanas', 'apples', 'dates'] 
shopping_cart = [] 

add_item(items, shopping_cart)