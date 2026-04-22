#program to manage student data such as name , age, marks , and subjects.
students = []
try:
    with open("database.txt","r") as f:
        for line in f:
            name, age, marks = line.strip().split("|")
            students.append({"name": name,"age":age, "marks":marks})
except FileNotFoundError:
    pass
while True  :
    print("\n---Student Management---")
    print("1.Add |2.View |3. Edit | 4. Delete | 5. Exit")
    choice = input("Select option: ")

    #add
    if choice == '1':
        name = input("Name:")
        age = input("Age: ")
        marks = input("Marks:")
        students.append({"name": name, "age":age, "marks":marks})
        print("Student added locally1")
    #View
    elif choice == '2':
        print("\n---Current Records---")
        for s in students:
            print(f"Name: {s['name']} | Age: {s['age']} | Marks: {s['marks']}")
    #edit
    elif choice == '3':
        target = input("enter name to edit :")
        for s in students:
            if s['name'].lower() == target.lower():
                s['age'] = input("New Age:")
                s['marks']=input("New Marks: ")
                print("Updated!")
                break
    #delete
    elif choice == '4':
        target = input("enter name to delete :")
        students = [s for s in students if s ['name'].lower() != target.lower()]
        print("Deleted!")
    #exit and save
    elif choice == '5':
        with open("database.txt", "w")as f :
            for s in students:
                f.write(f"{s['name']} | {s['age']} | {s['marks'] }\n")
            print("Data saved to database.txt. Goodbye!")
            break
         
    
