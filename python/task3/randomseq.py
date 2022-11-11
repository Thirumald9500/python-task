from datetime import date
import random
import string
year=date.today()
seq=str(year.year)+str(year.month)
seq=seq+str(random.randint(10,100))
letters = string.ascii_uppercase
for i in range(2):
    seq=seq+str(random.choice(letters))
print(seq)
