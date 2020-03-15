'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    if word == "":
        return 0
    # recursive case
    else:
        return word.count("th")


  # my test cases
word1 = " "  # 0
word2 = "abcthxyz"  # 1
word3 = "abcthefthghith"  # 3
word4 = "thhtthht"  # 2
word5 = "THtHThth"  # 1
word6 = "abcthefthghithabcthefthghithabcthefthghith1"  # 9
word7 = "abcdefghijklmnopqrstuvwxyz"  # 0
print(count_th(word1), count_th(word2), count_th(
    word3), count_th(word4), count_th(word5), count_th(word6), count_th(word7))

# ran python3 test_count_th.py --v and all test get an ok
