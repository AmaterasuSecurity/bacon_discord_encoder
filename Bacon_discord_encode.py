import os
import ctypes
import sys
import shutil


# function to return key for any value
def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"


# create a bit_mask for the hidden_text
def get_bit_mask(hide_me, dictionary_choice):
    mask = ""
    for char in hide_me:
        if char in dictionary_choice:
            mask += dictionary_choice[char]
    return mask


# *********************************************
#              usage instructions
print(" ")
print("To use the original Bacon cipher alphabet start with command line option --original")
print(" ")
# *********************************************
green_text = "\033[32;1m"
red_text = "\033[31m"
reset_text = "\033[0m"

original_bacon_dictionary = {"a": "00000",
                             "b": "00001",
                             "c": "00010",
                             "d": "00011",
                             "e": "00100",
                             "f": "00101",
                             "g": "00110",
                             "h": "00111",
                             "i": "01000",
                             "j": "01000",
                             "k": "01001",
                             "l": "01010",
                             "m": "01011",
                             "n": "01100",
                             "o": "01101",
                             "p": "01110",
                             "q": "01111",
                             "r": "10000",
                             "s": "10001",
                             "t": "10010",
                             "u": "10011",
                             "v": "10011",
                             "w": "10100",
                             "x": "10101",
                             "y": "10110",
                             "z": "10111"}

complete_bacon_dictionary = {"a": "00000",
                             "b": "00001",
                             "c": "00010",
                             "d": "00011",
                             "e": "00100",
                             "f": "00101",
                             "g": "00110",
                             "h": "00111",
                             "i": "01000",
                             "j": "01001",
                             "k": "01010",
                             "l": "01011",
                             "m": "01100",
                             "n": "01101",
                             "o": "01110",
                             "p": "01111",
                             "q": "10000",
                             "r": "10001",
                             "s": "10010",
                             "t": "10011",
                             "u": "10100",
                             "v": "10101",
                             "w": "10110",
                             "x": "10111",
                             "y": "11000",
                             "z": "11001"}
# sensible defaults
ascii_low_end = 33  # above space(32)
ascii_high_end = 125
dictionary_choice = complete_bacon_dictionary

# Makes it functional in cmd
if os.name == "nt":
    # if we are in windows setup the console for ansi escape characters
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
if "--original" in sys.argv:
    dictionary_choice = original_bacon_dictionary

# prompts for the text that you want to hide in discord.
hidden_text = input("Hidden Text >" + green_text).lower()
print(reset_text, end="")  # reset
bit_mask = get_bit_mask(hidden_text, dictionary_choice)
cover_text = "" # prompts for the text that you would like shown in discord.
while (len(cover_text) - cover_text.count(" ")) < len(bit_mask):
    if len(cover_text) > 0:
        print(red_text + "You need a longer cover text." + reset_text)  # red, reset
    cover_text += input("Shown Text >" + cover_text + green_text)
    print(reset_text, end="")  # reset

# prints hidden text in bold in discord but in asterisk in cmd
cipher_output = ""
hidden_index = 0
letter_typeface = "normal"
# print(f"The Bacon cipher is {bit_mask}")
print("")

for letter in cover_text:
    if ascii_low_end < ord(letter) < ascii_high_end and hidden_index < (len(bit_mask) - 1):
        # BOLD
        if int(bit_mask[hidden_index]) == 1:
            if letter_typeface == "normal":
                letter_typeface = "bold"
                cipher_output += "**"
            cipher_output += letter
        # NORMAL
        if int(bit_mask[hidden_index]) == 0:
            if letter_typeface == "bold":
                letter_typeface = "normal"
                cipher_output += "**"
            cipher_output += letter
        # ALL letters
        hidden_index += 1
    else:
        if letter_typeface == "bold":
            cipher_output += "**"
            letter_typeface = "normal"
        cipher_output += letter

print(cipher_output)
