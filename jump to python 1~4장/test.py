#a=80
#b=75
#c=55
#d=(a+b+c)/3
#print(d)

#num =13
#if num %2 == 8:
#    print('짝수')
#else:
 #   print('홀수')


#num = '881120-1068234'
#print(num[:6])
#print(num[7:])
#print(num.split('-'))


#str = 'a:b:c:d'
#new_str = str.replace(':','#')
#print(new_str)


#a = [1, 3, 5, 4, 2]
#a.sort()
#print(a)
#a.reverse()
#print(a)


#a = [‘Life’, ‘is’, ‘too’, ‘short’]
#print(''.join(a))


#a = (1,2,3)
#b = (4,)
#print(a+b)


#a=dict()
#a['name']='python'
#print(a)

#a[('a',)]=;python
#print(a)


#a[(1)]='python'
#a[250]='python'
#print(a)

#a = {'A':90, 'B':80, 'C':70}
#print(a['B'])

 #a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
 #set_a=set(a)
 #print(set_a)

 #last_lisr(set_a)
 #print(last_a)
'''
a=b=[1,2,3]
print((a),id(b))

a=[1,2,3]
b=[1,2,3]
print((a),id(b))

a[1]=4
print(b)
'''
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt', 'w')
f.write(body)
f.close()
