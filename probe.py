import random

rec = ['hi', 'while', 'How', 'Eva', 'Petrov', '145236', '74526312']
password = []
ch = ''
# random.randint(2,6)
for i in range(25):
    while len(ch) <= 12 or not len(ch) >= 16:
        w = random.choice(rec)
        if ch.count(w) == 0:
            ch += w
    password.append(ch)
    ch = ''
print(password)