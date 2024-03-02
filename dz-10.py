import keyword
import string

import keyword
import string

example_word = "super_duper_value"

symbol_found = False
for char in example_word:
    if char in string.punctuation and char != "_":
        symbol_found = True
        break

if symbol_found:
    print(False)
elif example_word != example_word.lower() \
        or example_word in keyword.kwlist \
        or example_word[0].isdigit() \
        or example_word.count(" "):
    print(False)
else:
    print(True)


# if any([True if char in upd_symbols else False for char in example_word]):
#     print("False")
# elif example_word in keyword.kwlist:
#     print("False")
# elif example_word != example_word.lower():
#     print("False")
# elif example_word.count("_") > 1:
#     print("False")
# elif example_word[0].isdigit():
#     print("False")
# elif " " in example_word:
#     print("False")
# else:
#     print(True)
