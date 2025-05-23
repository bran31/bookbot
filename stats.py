def count_letters(file):
    number = file.split()
    return len(number)

def repeats(file):
    letters = file.lower()
    p = 0
    t = 0
    c = 0
    e = 0
    for letter in letters:
        if letter == 'p':   
             p += 1
        elif letter == 't':
            t += 1
        elif letter == 'c':
            c += 1
        elif letter == 'e':
            e += 1
    ans = {'t' : t,'p' : p,'c' : c, 'e' : e}
    return ans   

def report(file):
    q = file
    for i,j in q.items():   
        if i == 't':
            count = {{'char': i, 'num': j}}
        elif i == 'e':
            count = {{'char': i, 'num': j}}
    return count
            