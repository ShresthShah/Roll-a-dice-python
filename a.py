# import time 
# seconds = input("Enter the time in number of seconds ")
# def countdown_timer(seconds):
#     while seconds>0:

#         mins = int(seconds//60)
#         secs = int(seconds%60)
#         timer = f"{mins}:{secs}"
#         print(timer,end= " ")
#         time.sleep(1)
#         print(timer)
#         seconds = seconds-1
#     print("Time Up!")
# countdown_timer(int(seconds))

# num = 5
# while num>0:
#     print(num)
#     num = num-1

# import random

# while True:
#     number = random.randint(1,6)
#     if number == 1:
#         print("[-----]")
#         print("[     ]")
#         print("[  0  ]")
#         print("[     ]")
#         print("[-----]")
#     elif number == 2:
#         print("[-----]")
#         print("[ 0   ]")
#         print("[     ]")
#         print("[   0 ]")
#         print("[-----]")
#     elif number == 3:
#         print("[-----]")
#         print("[     ]")
#         print("[0 0 0]")
#         print("[     ]")
#         print("[-----]")
#     elif number == 4:
#         print("[-----]")
#         print("[ 0 0 ]")
#         print("[     ]")
#         print("[ 0 0 ]")
#         print("[-----]")
#     elif number == 5:
#         print("[-----]")
#         print("[0   0]")
#         print("[  0  ]")
#         print("[0   0]")
#         print("[-----]")
#     elif number == 6:
#         print("[-----]")
#         print("[ 0 0 ]")
#         print("[ 0 0 ]")
#         print("[ 0 0 ]")
#         print("[-----]")

#         ans = input("Enter Y or N")
#         if ans == "y":
#             continue
#         if ans == "n":
#             break


import random 
  

response = "y"
   
while response == "y": 
      
    
    no = random.randint(1,6) 

    # conditions to check the number value  
    if no == 1: 
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]") 
    if no == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if no == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if no == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if no == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 
          
    
    response=input("press y to roll again and n to exit:") 
    print("\n") 
