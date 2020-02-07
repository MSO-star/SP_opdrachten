def palindroom_version2(woord):
    letters_woord= list(woord)
    pali= True
    for i in letters_woord:
        if i ==letters_woord[-1]:
            letters_woord.pop(-1)
        else:
            pali= False
            break
    return pali
print(palindroom_version2("malayalam"))


def palindroom_version1(woord):
    woord_rev= reversed(woord)
    if list(woord) == list(woord_rev):
        print("True")
    else:
        print("False")

print(palindroom_version1("malayalam"))