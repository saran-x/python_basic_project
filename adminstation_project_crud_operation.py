"""
Add/edit/search/delete contact details
"""
import json
class Operation_system:
    def __init__(self):
        self.details=[]
    def add (self):
        while True:
            accpeted=input("Add Contact Or Exit: ")
            if accpeted == "exit":
                print("Thanks For Adding Contact")
                break
            dic={}
            catindate_name=input("Enter a Name: ")
            catindate_age=input("Enter a Age: ")
            catindate_address=input("Enter a Address: ")
            dic["Name"]=catindate_name
            dic["Age"]=catindate_age
            dic["Address"]=catindate_address
            self.details.append(dic)
            with open("dataset.json","a") as demo:
                json.dump(self.details,demo)
                print("succesfully Add Contact!")
    def show(self):
        with open("dataset.json","r") as demo:
            person=demo.read()
            person_convert=json.loads(person)
            print("----"*10)
            column=["S.NO","Name","Age","Address"]
            print(f"{column[0]:<7}{column[1]:<10}{column[2]:<10}{column[3]:<10}")
            print("----"*10)
            for index ,i in enumerate(person_convert,start=1):
                print(f"{index:<7}{i["Name"]:<10}{i["Age"]:<10}{i["Address"]:<10}")
            print()
            print("which column edit")
            while True :
                select=input("Enter a column:")
                serial=int(input("Enter a Serial Number: "))
                if serial <= len(person_convert):
                    if select == "name":
                        if(0<=serial):
                            new_name=input("Enter a updated name:")
                            old_name=person_convert[serial-1]["Name"]
                            person_convert[serial-1]["Name"]=new_name
                            print(f"old detail: {old_name} into updated: {new_name}")
                            with open("dataset.json","w") as demo:
                                names_updated=json.dumps(person_convert)
                                demo.write(names_updated)
                                print("succesfully Edit Contact!")
                                break
                                
                    elif select == "age":
                        if(0<=serial):
                            new_age=input("Enter a updated age:")
                            old_age=person_convert[serial-1]["Age"]
                            person_convert[serial-1]["Age"]=new_age
                            print(f"Old detail: {old_age} into updated New detail: {new_age}")
                            with open("dataset.json","w") as demo:
                                age_updated=json.dumps(person_convert)
                                demo.write(age_updated)
                                print("succesfully Edit Contact!")
                                break
                                
                    elif select == "address":
                        if(0<=serial):
                            new_address=input("Enter a updated address:")
                            old_address=person_convert[serial-1]["Address"]
                            person_convert[serial-1]["Address"]=new_address
                            print(f"Old detail: {old_address} into updated New detail: {new_address}")
                            with open("dataset.json","w") as demo:
                                names_updated=json.dumps(person_convert)
                                demo.write(names_updated)
                                print("succesfully Edit Contact!")
                                break
                                
                    else:
                        print("Something Wrong!")
                        
                else:   
                    print("Not Found!")
                    
    def search(self):
        with open("dataset.json","r")as demo:
            searchs=demo.read()
            search_in=json.loads(searchs)
            while True:
                search_sn=int(input("Enter your S.No: "))
                if search_sn == len(search_in):
                    search_person=input("Enter a person name:")
                    search_name=[]
                    for i in search_in:
                        search_name.append(i["Name"])
                    if 0 <= search_sn and search_person in search_name:
                        print("----"*10)
                        column=["S.NO","Name","Age","Address"]
                        print(f"{column[0]:<7}{column[1]:<10}{column[2]:<10}{column[3]:<10}")
                        print("----"*10)
                        search_details=search_in[search_sn-1]
                        print(f"{search_sn:<7}{search_details["Name"]:<10}{search_details["Age"]:<10}{search_details["Address"]:<10}")
                        break    
                    else:
                        print("----"*10)
                        column=["S.NO","Name","Age","Address"]
                        print(f"{column[0]:<7}{column[1]:<10}{column[2]:<10}{column[3]:<10}")
                        print("----"*10)
                        str1="Not Found!"
                        cen=str1.center(30)
                        print(cen)
                            
                else:
                    print("Not found")
                    print("Stay or Close")
    def delete(self):
        with open("dataset.json","r") as demo:
            person=demo.read()
            person_convert=json.loads(person)
            print("----"*10)
            column=["S.NO","Name","Age","Address"]
            print(f"{column[0]:<7}{column[1]:<10}{column[2]:<10}{column[3]:<10}")
            print("----"*10)
            for index ,i in enumerate(person_convert,start=1):
                print(f"{index:<7}{i["Name"]:<10}{i["Age"]:<10}{i["Address"]:<10}")
        delete_sn=int(input("Enter a Serial Number: "))
        if 0 <= delete_sn :
            person_convert.pop(delete_sn-1)
            print("success fully delete!")
            with open("dataset.json","w") as demo:
                str2=json.dumps(person_convert)
                demo.write(str2)
                print("Saved in Contact Dataset..!")
        else:
            print("Not Found Serial Number")
action=Operation_system()
class ChoiceError(Exception):
    pass
admin={"Karthik":"kar@2007",
       "Kaviya":"kaviya@2004",
       "lingaesh":"1234@ling"}
print("------Welcome to Adim Login pannel------")
count=0
while count < 3:
    user=input("Enter a User Name: ")
    password=input("Enter a password: ")
    if user in admin:
        if password == admin[user]:
            while True:
                print("----Welcome to Adim pannel----")
                print("Contact Detail Operation")
                print("1.Add Contact")
                print("2.Edit Contact")
                print("3.Search Contact")
                print("4.Delete Contact")
                print("5.Logout")
                choice=int(input("Enter your choice: "))
                
                try:
                    if choice >=6:
                        raise ChoiceError
                    else:
                        if choice == 1:
                            print("---Enter a New Contact Details!---")
                            print("Fill The Details Carefully!")
                            action.add()
                        elif choice == 2:
                            print()
                            print("---Edit Under The Data Table---")
                            action.show()
                        elif choice == 3:
                            print()
                            print("---Enter a Name in the Contact---")
                            action.search()
                        elif choice == 4:
                            print()
                            print("---Attention Carefully Delete a information---")
                            action.delete()
                        else:
                            print("Thanks for visited...")
                            break
                except ChoiceError as e:
                    print("please enter a correct choice!")
                except TypeError:
                    print("please enter a correct choice!")
                except ValueError:
                    print("please enter a correct formate!")
            break
        else:
            print("Invalid Password!")
            count+=1
            
    else:
        print("UserName Not found!")
        count+=1
        
if count == 3:
    print("30 Second After Login!")
