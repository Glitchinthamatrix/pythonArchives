import random

#--------1st---------: you guess the number and the comuter the tells if it's the correct one
# human guesses the number
# def human_guess(x):
#     rand_num=random.randint(1,x)
#     guess=0
#     while guess!=rand_num:
#         guess=int(input(f"guess a number between 1 and {x}: "))
#         if guess<rand_num:
#             print("too low")
#         elif guess>rand_num:
#             print("too high")  
#     print(f"you guessed the number {rand_num} right") 

# human_guess(10)  
#---------------------------------------------------------------------------------------------



#-----------2nd----------: computer guesses the number and you tell if it's the correct one
# def computer_guess(x):
#     low=1
#     high=x
#     feedback=''
#     while feedback != 'c':
#         if low>=high:
#             print('malfunction')
#             feedback="c"
#         if low!=high and feedback!="c":
#             guess=random.randint(low,high)
#         else:
#             guess=low

#         if feedback!="c":
#             feedback=str(input(f"is {guess} too high or too low: "))

#         if feedback=='l':
#             low=guess+1
#         elif feedback =="h":
#             high=guess-1    
    
#     print(f"low = {low}, high ={high}")   
#     print("computer guessed the number" if low<high else "low value cannot be greater than or equal to high")   
    
# computer_guess(1000) #computer chooses a random number 1-1000 while you tell it if it's the correct one
#--------------------------------------------------------------------------------------------------------------





#----------3rd: 
    