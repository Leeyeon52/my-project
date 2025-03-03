
a = "a:b:c:d"
split_a = a.split(":")

join_a = "#".join(split_a)
print(join_a)





a = {'A':90,'B':80,}

if a.get('C')==None:
    a['C'] = 70

print(a['C'])





a = [1,2,3]
a = a + [4,5]
print(a)
print(id(a))

a = [1,2,3]
a.extend([4,5]) 
print(a)
print(id(a))

# 위의 두개를 비교해보면 위에꺼 id(a) 를 확인한 결과 2.00000000몆에 저장이 되고 아래의 id(a)를 확인한 결과 3.000000소수점에 저장이 되는것을 확일 하여싿.




A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0

for a in A:
    if a>=50:
        sum += a
print(sum)




inputval = input("값을 입력하세요 : ")
a = map(int, inputval.split(','))

result = 0
for i in a:
    result += i 

print(result)



a = input('구구단을 출력할 숫자를 입력하세요(2~9) : ')
a_num = int(a)

for i in range(1,10):
    print('%d'%(a_num*i),end=' ')

n = input("숫자 입력 : ")
n = int(n)

pib = [0,1]
result = 0
if n==1:
    print(pib[0])
elif n>1:
    for i in range(1,n-1):
        pib.append(pib[i-1]+pib[i])

print(pib)

