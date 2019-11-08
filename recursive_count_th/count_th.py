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
    print(f"word : {word[0:2]}")
    print(f"len(word) : {len(word)}")
    print(f"word[0] : {word[0]}")
    if len(word) = 0:
        print("fart")
        return 0
    elif word[0] != "t":
        print(f"\nword before != t : {word}\n")
        recword = word[1::]
        print(f"\nrecword after != t : {recword}\n")
        return count_th(word[1::])
    elif word[0] + word[1] == "th":
        print(f"\nword before th : {word}\n")
        recword = word[2::]
        print(f"\nbase : {base}\n")
        # base = base + 1
        print(f"\nrecword after th : {recword}\n")
        return count_th(word[2::])

    pass
