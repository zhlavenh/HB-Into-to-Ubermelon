#Opening a file and assigning it to the variable log_file
log_file = open("um-server-01.txt")

#Creating a function that generates sales reports and taking in a parameter named log_file
def generate_sales_reports(log_file):
    #Looping through each line in the file 
    for line in log_file:
        #Removing the white space onteh right side of each line
        line = line.rstrip()
        #Taking the firt 3 charaters from the line and assigning it to day
        day = line[0:3]
        #Checking if the variable day matches Monday
        if day == "Mon":
            #printing the whole line if the first three letters are Mon
            print(line)

#calling the function and using the opened file as the argument
generate_sales_reports(log_file)
