def add_pwd():
    user_name=input("Account Name:")
    pwd_name=input("password:")
    with open('password.txt','a') as f:
        f.write(f"{user_name} | {pwd_name}{"\n"}")
def view_pwd():
    with open('password.txt','r') as f:
         for line in f.readlines():
             print(line.strip())
             
         
while True:
       print("welcome to password manager!")
       print(" password manager \n"
               "1.Add password\n"
               "2.view password\n"
               "3.exit")
       
       user=int(input("Enter your operation:"))
       
       if user==1:
           add_pwd()

       elif user==2:
           view_pwd()
           
       elif user==3:
           break
       
       else:
           print("Invalied operation please try again 😔")  