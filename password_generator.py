import random
      
while True:      
      print("Welcome to password generator!:")
      number_of_password= int(input("Enter number of password you need:"))
      password_char= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&"
      password_length= int(input("Enter the length of the password:"))
      print("your password is:")
      for x in range(number_of_password):
          password=""
          for y in range(password_length):
              password=password+random.choice(password_char)
          print(password)