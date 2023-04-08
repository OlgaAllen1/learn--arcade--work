import re


# This function takes in a line of text and returns
# a list of words in the line.

def split_line(line):

    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dictionary_list = []  # list of all the words in the dictionary
dictionary_file = open("dictionary.txt")  # to read
for line in dictionary_file:
    line = line.strip()
    dictionary_list.append(line)

dictionary_file.close()

print("---Linear Search---")
file = open("AliceInWonderLand200.txt")
for number, line in enumerate (file):
    word_list = split_line(line)
    for word in word_list:
        # Start at the beginning of the list
        current_list_position = 0

        # Loop until you reach the end of the list, or the value at the
        # current position is equal to the word
        while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
            # Advance to the next item in the list
            current_list_position += 1

        if current_list_position == len(dictionary_list):
            print(f"Line {number + 1}, possible misspelled word:{word}")

file.close()

print("---Binary Search---")
file = open("AliceInWonderLand200.txt")
for number, line in enumerate (file):
    word_list = split_line(line)
    for word in word_list:

        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False

        # Loop until we find the item, or our upper/lower bounds meet
        while lower_bound <= upper_bound and not found:

            # Find the middle position
            middle_pos = (lower_bound + upper_bound) // 2

            if dictionary_list[middle_pos] < word.upper():
                lower_bound = middle_pos + 1
            elif dictionary_list[middle_pos] > word.upper():
                upper_bound = middle_pos - 1
            else:
                found = True

        if not found:
            print(f"Line {number + 1}, possible misspelled word:{word}")

file.close()