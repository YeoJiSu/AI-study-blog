# set에 관하여 
# unordered, 중복 X, index가 없기에 slicing, sort, reverse 안된다. 
bric = {1,2,3,4,5}
bri = bric.copy()
bri.add(6)
bric.remove(2)
bric.discard(1) # discard 나 remove나 같음 
print(bric)
print(bri)
print(bric.issuperset(bri))
print(bric.issubset(bri))
print(bric.intersection(bri) , bric&bri)
# 아까 파일읽을 떄 intersection하면 훨씬 간편 
print(bric.union(bri), bri | bric)
print(bric.difference(bri), bric - bri) # bric - bri 는 없음
print(bri.difference(bric), bri - bric) # bri - bric 은 2랑 6
print(bri ^ bric) # symmetric difference
bri.clear()
print(bri)

words = ['nudge', 'nudge', 'wink', 'wink']
tuple(words) # ('nudge', 'nudge', 'wink', 'wink')
terms = set(words)
print(terms) # {'wink', 'nudge'}
list(terms) # ['wink', 'nudge']
tuple(terms) # ('wink', 'nudge')
alpha =('a', 'b', 'c')
set(alpha) # {'a', 'c', 'b'}

bric = {'brazil', 'china', 'india', 'russia'} 
sorted(bric) # sorted를 하면 list로 바뀐다. ['brazil', 'china', 'india', 'russia']
sorted(bric, key=len, reverse=True) #['brazil', 'russia', 'china', 'india'] 
bric # 순서 무작위 {'china', 'india', 'brazil', 'russia'}

{x * x for x in range(-3, 3)} # {0, 9, 4, 1}