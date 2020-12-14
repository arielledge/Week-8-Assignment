## Import OS library/mod
import os  


## If User wants to go again
def again():
    Valid = input("Would you like to try again? Type 'yes' or 'no': ")
    if (Valid == "yes"):
        main()
    else:
        quit()

## Main function layout
def main():    
    ## Directory path as user input 
    dir = input("What is the directory you'd like to lookup and validate? ")
   
    if os.path.isdir(dir):
        print ("Awesome. We found it. Let's write your file.")
        filename = input("Enter the name for the file you want to create: ")
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        phone_number = input("Enter your phone number: ")
        ## Writing the actual file
        writeFile = open(os.path.join(dir,filename),'w')
        ## Write the contents of the file
        writeFile.write("Name: " name+','"Address: "+address+','"Phone Number: "+phone_number+'\n')
        ## Close File
        writeFile.close()
        print("File contents:")
        ## Did the file writing function work?
        readFile = open(os.path.join(dir,filename),'r')

        for line in readFile:
            print(line)
        readFile.close()

        again()

    else:
        print("Sorry! That directory doesn't actually exist.")
        again()

main()