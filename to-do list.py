tasks = {
    'learn new python concept': 'incomplete', 
    'build python project': 'incomplete', 
    'work shift at sainsburys': 'incomplete' 
} 

def main(tasks): 
    while True:
        add_task = input("Add item on to do list (type 'Done' when finished): \n").title()
        if add_task.rstrip() == "Done": 
            complete_task(tasks)
            return tasks
        else: 
            tasks[add_task] = "Incomplete"
            for task, status in tasks.items(): 
                print(f"[{task.title()}: {status.upper()}]")                          
         
def complete_task(tasks):    
        for task, status in tasks.items(): 
            compl = input(f"{task.title()}, Complete or Incomplete? ")
            tasks[task] = compl    
        print("\n")
        
        for task, status in tasks.items(): 
            print(f"{task.title()}: {status.upper()}") 

        return tasks

main(tasks) 