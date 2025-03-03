frult = 'apple'
for x in frult:
    print(x)


max = 25 # 최대 허용 무게
weight = 0 # 현재 캐리어 무게
item = 3 # 각 짐의 무게
while weight + item <= max:
    weight += item
    print(“짐을 추가합니다”)
print(f“총 무게는 {weight} 입니다”)



i=3
while i <=5:
    print(i)
    i+=1

 drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
 for x in drama:
  if x == '시즌3':
    print('재미없대, 건너 뛰자')
    continue
  prnit(f'{x}시청')
  break


for x in range(10):
  if x % 2 == 1:
    continue
  print(x)


products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = []
for p in products:
  if p.startswith('SIRO'):
    recall.append(p)

print(recall)



my_list[1,2,3,4,5]
new_list = [x * 2 for in mt_list is x >3]
print(new_list)