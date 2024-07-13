## Author: Francisco Bumanglag
## Project: Create Numbers 1 to 100
## Assignment: Module 3 Project 3
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 26, 2023


def write_main(): 

    #declare outfile -- open file 
    outfile = open("number_list.txt", "w")

    #write numbers 1 top 100 using for loop 
    for num in range (1, 101): 
        outfile.write(str(num) + "\n") 

    print("List of numbers were written to the number_list.txt file") 

    outfile.close()

write_main()



