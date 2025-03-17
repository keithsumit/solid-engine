# open the list of words to search for
list_file = open('listfilesinDir.txt')

search_words = []

# loop through the words in the search list
for word in list_file:

    # save each word in an array and strip whitespace
    search_words.append(word.strip())

list_file.close()

# this is where the matching lines will be stored
matches = []

# open the master file
master_file = open('test_engineer_valimar.txt')

# loop through each line in the master file
for line in master_file:

    # split the current line into array, this allows for us to use the "in" operator to search for exact strings
    current_line = line.split()

    # loop through each search word
    for search_word in search_words:

        # check if the search word is in the current line
        if search_word in current_line:

            # if found then save the line as we found it in the file
            matches.append(line)

            # once found then stop searching the current line
            break

master_file.close()


# create the new file
new_file = open('list_Owners.txt', 'w+')

# loop through all of the matched lines
for line in matches:

    # write the current matched line to the new file
    new_file.write(line)

new_file.close()