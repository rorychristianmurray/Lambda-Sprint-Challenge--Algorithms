'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # recursive call

    # how would I do this
    # scan through and look for occurrences where
    # word[i] + word[i + 1] = "th"
    # how to keep track of count

    # return
    # what do we return
    # we return a count of string occurrences
    # of "th"

    # base case
    # what do we drive to
    # print(f"word : {word[0:2]}")
    # print(f"len(word) : {len(word)}")
    # print(f"word[0] : {word[0]}")
    if len(word) <= 1:
        return 0
    elif word[0:2] == "th":
        return 1 + count_th(word[1::])
    else:
        return 0 + count_th(word[1::])


werd1 = "thth"  # 2
werd2 = "realtalk"  # 0
werd3 = "ththThtH"  # 2

t1 = count_th(werd1)
# t2 = count_th(werd2)
# t3 = count_th(werd3)

print(t1)
# print(t2)
# print(t3)
