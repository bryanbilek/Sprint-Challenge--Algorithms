'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # count how many times lowercase 'th' is in word
    # no loops so maybe we'll have a counter via index or check the first 2 indexes & repeat?
    
    # TBC - when we have checked all the letters & are left with 1, we finish as we can no longer get a 'th' that requires at least 2 letters to get checked
    # also return 0 so the count can't be added onto or is 0 in general if no 'th' was found
    if len(word) < 2:
        return 0
    # let's slice through the first 2 indexes to check for 'th'
    # if 'th' is there, return 1 to the count & re-do this time starting at the index after those first 2 spots
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    # if 'th' isn't in indexes 0 & 1, it won't matter if 'h' was at index 1 because we need 't' at index 0 at least
    # so we will call the recursion again this time after index 0 until any of our cases are met
    else:
        return count_th(word[1:])
