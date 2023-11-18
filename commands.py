#dynamic command output
#takes in show_commands.txt file that contains all your commands

my_commands = [] #defines a list of my commands
command_index = 0 #setting a counter integer for dynamic counting of the number of commands that i have

file = open("show_commands.txt", "r") #opens the file and reads it in
lines = file.readlines() #reads each line and puts it into a list
stripped_lines = [line.rstrip('\n') for line in lines] #strips the carriage return '\n' from each line
count = (len(stripped_lines) - 1 ) #grabs the number of commands in the list, factors in the fact that the list index will always start at 0 so the while loop doesn't overcount

#then use a while loop to iterate through each command
while command_index <= count:
    print(stripped_lines[command_index])
    command_index += 1