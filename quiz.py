def quiz(): 
    print("Which of the following is not a fruit?\n") 
    answers_1 = {'A':'Rhubarb', 'B':'Tomatoes', 'C':'Avocados'}
    score = 0 
    for key, value in answers_1.items(): 
        print(f"{key}) {value}") 

    answer_1 = input("\nAnswer: ").lower()
    if answer_1 == "a": 
        print("\nCorrect!") 
        score += 1 
    else: 
        print("\nIncorrect!") 

    print("\nWhich of the following languages has the longest alphabet?\n") 
    answers_2 = {'A':'Greek', 'B': 'Russian', 'C':'Arabic'}
    for key, value in answers_2.items(): 
        print(f"{key}) {value}") 

    answer_2 = input("\nAnswer: ").lower() 
    if answer_2 == "b":
        print("\nCorrect!")
        score += 1 
    else:
        print("\nIncorrect!") 

    print("\nWhat is the largest US state (by landmass)?")
    answers_3 = {'A':'Texas', 'B':'Alaska', 'C':'California'}
    for key, value in answers_3.items(): 
        print(f"{key}) {value}") 

    answer_3 = input("\nAnswer: ").lower()
    if answer_3 == "b":
        print("\nCorrect!") 
        score += 1 
    else: 
        print("\nIncorrect") 

    print(f"\nScore = {score}") 

quiz()