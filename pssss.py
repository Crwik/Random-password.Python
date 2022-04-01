#crwik
import random
a = "abcdefghijklmnopqrstuvwxyz" #lowercase letters
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #capital letters
m = "1234567890" #numbers
d = "[]{}()*;/,._-@"#character
al = a + b + m + d
length = 23 #flexible
p = "".join(random.sample (al,length))
print(p)
#crwik
