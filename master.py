data=[]
def insert_data():
    title=input("Enter the title")
    amount=input("Enter the Amount")
    date=input("Enter the date")
    #print(title+" "+amount+" "+date)
    data.append((title,amount,date))
def display_data():
    for index,item in enumerate(data):
         print(str(index+1)+ " " +item[0]+" "+item[1]+" "+item[2])

def delete_data(): 


    display_data()   
    index=int(input("Enter the index of the data you want to delete"))      

    if 0<index<=len(data):  
        delete_item=data.pop(index-1)
        print(f"delete record: {delete_item[0]} | {delete_item[1]} | {delete_item[2]}")

    else:
        print("invalid record number")

def update_data():
    display_data()       
    index=int(input("Enter the record of number to be updated"))

    if 0<index<=len(data):
        title=input("Enter the new title(leave empty to keep unchanged)")
        amount=input("Enter the new amount(leave empty to keep unchanged)")
        date=input("Enter the new date(leave empty to keep unchanged)")
        old_title,old_amount,old_date=data[index-1]

        data[index-1]=(
            title or old_title,
            amount or old_amount,
            date or old_date,
        )
        print("data updated sucessfully")
    else:
        print("invalid index")
           

y=0
while(y==0):
    print("1->For Insert")
    print("2->For Display")
    print("3->For Delete")
    print("4->For Update")
    opt=int(input("Enter the option you want to perform"))
    if(opt==1):
       insert_data()
    if(opt==2):
       
       display_data()
    if(opt==3):
       delete_data() 
    if opt==4:
        update_data()
    y=int(input("Do you want to continue? press 0 for yes"))
