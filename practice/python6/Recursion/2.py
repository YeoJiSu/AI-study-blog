def up(word):
    word = word.upper()
    if len(word) <= 1:
        return True
    elif word[0]==word[-1]:
        word = word[1:-1] # 자르고 
        return up(word)
    else:
        return False
print(up("jssj"))