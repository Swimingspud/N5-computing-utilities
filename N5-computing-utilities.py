import time
import os
import colorama
from colorama import Fore, Back
import sys
colorama.init(autoreset=True)  #automaticaly reset colorama


def typingPrint(text):   #typing out predifined text
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.10)
  
def typingInput(text):    #input text to typing out
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.10)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

# Function for implementing the loading animation
def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "starting utilties....."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 40):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
  
# Driver program
if __name__ == '__main__': 
    load_animation()

    print(
            f"{Fore.GREEN}#####################################################"
       "\n#                                                   #"
       "\n#            N5 computing utilities                 #"
       "\n#                                                   #"
       "\n#          Any issues please conatact:              #"
       "\n#                                                   #"
       "\n#         gw7MitchellCameron@glow.sch.uk            #"   #What the software does and contact info
       "\n#                                                   #"
       "\n#               Cameron Mitchell                    #"
       "\n#                     2021                          #"
       "\n#####################################################"
       )
    
    


    print()
    print()



    print(f"{Fore.MAGENTA}Please select the software you would like to use."
    "\n-------------------------------------------------"
           )
    
    print()

    print(f"{Fore.CYAN} 1. ASCII converter"
    )
    print()
    print()
 
    pick = typingInput("Please enter number: ")  #asking user to choose which software they would like to use

    while True:

        if pick == "1":
          n = 1 #setting to 1
    
          
            
          
          if __name__ == '__main__': #Loading animation
              load_animation()
          
              print(
          
                   f"{Fore.GREEN}#####################################################"
              "\n#                                                   #"
              "\n#       Charactors to ASCII decimal and binary      #"
              "\n#                                                   #"
              "\n#          Any issues please conatact:              #"
              "\n#                                                   #"
              "\n#         gw7MitchellCameron@glow.sch.uk            #"   #What the software does and contact info
              "\n#                                                   #"
              "\n#               Cameron Mitchell                    #"
              "\n#                     2021                          #"
              "\n#####################################################"
              )
              print()
              print()
          
              time.sleep(2)
          
              while n == 1:  #creating a loop whilst n = 1
          
                  char = typingInput("Please enter Charactor(s): ") #asking user for text to be converted
                  for letter in char:   # creating a loop for every charater(s)
                      deciminal = ord(letter) #getting decimal value
                      binary = bin(deciminal) #getting binary value but has b in it
                      a = bin(deciminal)      #finding the binary value of the decimal
                      b = bin(deciminal)[2:]   #found this to remove b dont know how it works
                      c = b.zfill(8)
                      print()
                      print(
                      "",letter,  #print the charactor the user entered.
                      "=",
                      f"{Fore.BLUE}Deciminal:",   # printing results in easy to read format
                      deciminal,
                      f"{Fore.MAGENTA}Binary:",
                      c
                      )
                      print()
          
              else:
                  print(f"{Fore.RED}{Back.GREEN}error")  #if n doesnt = 1 
      
        
        elif pick != "1":
            print()
            print(f"{Fore.RED}{Back.GREEN}Invalid")
            pick = input("Please try again: ")  #invalid entry if entered correctly will go back up to the software
    
        time.sleep(6) #for testing porposes
    