def taskList(): #i create a function name taskList
    todoList =[] #empty variable with list data type, we will add data in this list
    todoCount = int(input("Enter the number of tasks : ")) #asking user to enter the number of task they want to add
    for i in range(1, todoCount+1): #using loop to enter the number of task entered by user (started from 1 and added +1  because default value is 0)
        task = input(f"Enter the tsk {i} : ") #asking user to enter the task until the number of times entered by user
        todoList.append(task) #append helps to add data of variable name task into emptly list todoList

    while True: #while following  all statements are true
        try:
            operation = int(input("1.Add \n 2.Update \n 3.Delete \n 4.View Data \n 5.Exit\n Please Choose one  :  "))#asking user to do CRUD operation
        
            if operation == 1:  #1 to add more data
                taskAdd = input("Enter the task : ")
                todoList.append(taskAdd)
                print(f"The Task {taskAdd} Has Been Added To Your Todo List.")

            elif operation == 2: # to update the existing data 
                taskupdate = input("Enter the task you want to update : ") #new variable defined to compare the user input data and data in list
                if taskupdate in todoList: #if comparison is true
                    newupdateTask = input("Enter the task you want to replace : ") #asking user to enter the new data to replace with existing data
                    extaskindex = todoList.index(taskupdate) #created variable name (extaskindex) to define existing task index where index will be taskupdate
                    todoList[extaskindex] = newupdateTask #ex task index in todo list will be replace with new variables (newudateTask) data 
                    print(f"The Task {taskupdate} Has Been Replaced With {newupdateTask}")

            elif operation == 3:
                deleteTask = input("Enter the task you want to delete : ")
                if deleteTask in todoList:
                    deIndex = todoList.index(deleteTask)
                    del todoList[deIndex] #del will perform delete task
            elif operation == 4:
                print(todoList)
            elif operation == 5:
                print("Closing Program....")
                break
        except ValueError: #if the input data type of (operation variable) doesn't match the data type inserted by user, it will give following error
            print("The entry doesn't match, Please Enter valid number")
taskList()

