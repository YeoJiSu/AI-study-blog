import random
mylist= ["jisu","jinyoung","daeuon","mango"]
print(random.choice(mylist))
print(random.sample(mylist,3))
random.shuffle(mylist)
print(mylist)
print(random.randint(1,5)) # random integer 1부터 5까지