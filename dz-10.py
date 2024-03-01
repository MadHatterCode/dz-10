import keyword
import string

example_word = "super_duper_value"

upd_symbols = string.punctuation.replace('_', '')

for char in example_word:
    if char in upd_symbols:
        print(False)
        break
    if example_word != example_word.lower() or example_word in keyword.kwlist or example_word.count("_") > 1 or example_word[0].isdigit() or example_word.count(" "):
        print(False)
        break
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
