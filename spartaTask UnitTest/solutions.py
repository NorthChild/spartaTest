#################################### NOTE ####################################
#################################### NOTE ####################################

# These are the solutions to the tasks, going by memory so i apologise if outputs are slightly different
# left a bunch of print statements for when i was testing the code etc, left if in just in case
# IMPORTANT: you can run this script to test whether or not the solutions give the right output, REMEMBER TO de-comment print statement following the functions
# IMPORTANT: you can de-comment print statements activating the functions to test whether or not the give correct output
# IMPORTANT: to run the testing, make sure to run the 'test_solutions.py' script and rememeber to keep both scripts in the same folder


#################################### NOTE ####################################
#################################### NOTE ####################################


################################## TASK I ####################################

print(" ")
# make a calculator using functions

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('Can not divide by 0')
    return n1 / n2

# print('TASK I')
# print(add(1,2), end="\n")
# print(divide(4,2), end="\n")
# print(multiply(1,2), end="\n")
# print(subtract(1,2), end="\n")

################################## TASK II ####################################

# get a string containing a genetic sequence containing C A T G and count individual elements of the string

# C = 10
# A = 8
# T = 14
# G = 16


string = 'CCTGGGACGTCGTAAGCTAGCTGTATGCTGAGTGTCTAGTCGTAGCGT'

def string_counter(string):

    C = []
    A = []
    T = []
    G = []

    for i in string:

        if i == 'C':
            C.append(i)
        elif i == 'A':
            A.append(i)
        elif i == 'T':
            T.append(i)
        elif i == 'G':
            G.append(i)

    countC = len(C)
    countA = len(A)
    countT = len(T)
    countG = len(G)

    return f'C:{countC},A:{countA},T:{countT},G:{countG}'


# print('TASK II')
# print(string_counter(string), end="\n")

################################## TASK III ###################################


# determine the value of given words following the rules of scrabble
one_point = ["E", "A", "I", "O", "N", "R", "T", "L", "S", "U"]
two_points = ["D", "G"]
three_points = ["B", "C", "M", "P"]
four_points = ["F", "H", "V", "W", "Y"]
five_points = ["K"]
eight_points = ["J", "X"]
ten_points = ["Q", "Z"]

string1 = 'zoo'
string2 = 'scrabble'
string3 = 'faraday'

def scrabble_counter(string):

    word_to_analyse = []

    counter = 0

    for i in string:
        word_to_analyse.append(i.upper())

    for element in word_to_analyse:
        if element in one_point:
            # print("one point el:", element)
            counter += 1
        elif element in two_points:
            # print("two points el:", element)
            counter += 2
        elif element in three_points:
            # print("three points el:", element)
            counter += 3
        elif element in four_points:
            # print("four points el:", element)
            counter += 4
        elif element in five_points:
            # print("five points el:", element)
            counter += 5
        elif element in eight_points:
            # print("eight points el:", element)
            counter += 8
        elif element in ten_points:
            # print("ten points el:", element)
            counter += 10
    return string, counter

# print('TASK III')
# print(scrabble_counter(string1), end="\n")
# print(scrabble_counter(string2), end="\n")
# print(scrabble_counter(string3), end="\n")


#
