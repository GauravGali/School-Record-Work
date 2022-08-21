# program to read a text file line by line and display each word separated by #.

with open('text.txt' , 'r') as fh: # opening the file

    while True: # iterating until file ends
        line = fh.readline() # reading the line

        if line == '': # checking if file ends
            break

        line = line.split() # seperating each word

        for word in line: # add the "#" after every word
            if word == line[-1]: # check if word is in end to not add "#"
                print(f'{word}')
            else:
                print(f'{word}#' , end = '')