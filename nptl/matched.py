def matched(s):
    ob = 0
    cb = 0
    pos = "closed"
    for i in s:
        if i == "(":
            ob = ob + 1
            pos = "open"
        elif i == ")":
            cb = cb + 1
            pos = "closed"
    
    if ob == cb and pos == "closed":
        return True
    else:
        return False
