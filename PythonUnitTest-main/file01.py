# =============================================================================
# (a) Key checker function
# This function checks if the key is between 0 and 94.
# =============================================================================
def check_key(key):
    if key in range(0, 95):
        return True

    return False


# =============================================================================
# (b) Function to count number of upper case and lower case letters
# This function counts the number of upper case and lower case letter of a
# given string and returns a list of [upper, lower]
# =============================================================================
def check_upper_lower(s):
    upper = 0
    lower = 0

    upper = sum(map(str.isupper, s))
    lower = sum(map(str.islower, s))

    return [upper, lower]


# =============================================================================
# (c) Function to encrypt or decrypt a string of printable characters.
# Encrypt or decrypt a string s1 with a key based on the option
# and return a string value.
# Option = 1 for encrypt, option =2 for decrypt, default option =1,
# other option value returns message "Invalid option!".
# Key value between 0 and 94, default key=3. Other key value returns
# "Invalid key!"
# =============================================================================
def encrypt_decrypt_string(s1, key=3, option=1):

    if option != 1 and option != 2:
        output = "Invalid option!"
        return output

    if check_key(key) is False:
        output = "Invalid key!"
        return output

    if option == 1:
        char_list = []
        for char in s1:
            if (ord(char)+key) > 126:
                char_list.append(chr(((ord(char)+key) % 127) + 32))
            else:
                char_list.append(chr(ord(char)+key))

    if option == 2:
        char_list = []
        for char in s1:
            if (ord(char)-key) < 32:
                char_list.append(chr((127 - (ord(char)-key) % 32)))
            else:
                char_list.append(chr(ord(char)-key))

    output = ''
    for x in char_list:
        output += x
    return output


# =============================================================================
# (d) Function to count occurrence of words in a text file
# This function count the occurrences of each word in a txt file (sfile) and
# returns the occurences of each word in a dictionary format. It returns
# "Wrong file or file path" if sfile is not found.
# =============================================================================
def count_words_in_file(sfile):
    wordlist = {}
    try:
        file = open(sfile, "r")
        count_line = file.readline()
        words_list = []
        while count_line != "":
            line = count_line.split()
            for word in line:
                word = word.rstrip("\n.,?!")
                words_list.append(word.upper())
            count_line = file.readline()
        for word in words_list:
            if word not in wordlist:
                count = 0
                for x in words_list:
                    if x == word:
                        count += 1
                wordlist[word] = count
        return wordlist

    except (FileNotFoundError, IOError):
        return "Wrong file or file path"


# =============================================================================
# (e) Function to find max, min, sum, count, and mean
# This function find the maximum, minumum, sum, count, and mean values of
# a column (as specified by col_index) in a text file (infile). The function
# returns a list with the value for the maximum, the minimum, the sum, the
# count on the number of values, and the mean value for that particular
# column, e.g [max_value, min_value, sum_value, count, mean_value].
# Format the mean value to two decimal points. If a file is not found,
# explicitly raise the FileNotFoundException
# =============================================================================
def summarise_data(infile, col_index):
    try:
        with open(infile) as f:
            f.readline()
    except FileNotFoundError:
        raise 

    results = []
    return results
