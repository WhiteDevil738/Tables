# Table's
while True:
    user = int(input("Enter the Number"))
    for i in range(1,11):
        print(user,"X",i,"=",user*i)
    print("Exit  press 1 else 2")
    exit_ = int(input())
    if exit_ == 2:
        pass
    else:
        print("Thank's For Using")
        break
    
