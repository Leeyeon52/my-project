'''def is_odd(number):
  if number % 2 == 1:
    return True
  else:
    return False

a = is_odd(3)
b = is_odd(4)
print(a)
print(b)


def avg_numbers(result):
  result = 0
  for i in args:
    result += i
  return result / Ien(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))




input1 = int(input('첫 번째 숫자를 입력하세요:'))
input2 = int(input('두 번째 숫자를 입력하세요:'))

total = input1 + input2

print('두 수의 합은 %s입니다.' % total)



print('you''need''python')
print('you'+ 'need'+ 'python')
print('you','need','python')
print(''.join(['you','need','python']))



f1 = open('test.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('test.txt', 'r')
print(f2.read())
f2.close()
'''

user_input = input('저장할 내용을 입력하세요 : ')
f = open('test.txt', 'a'endcoding,UTF-8)
f.write(user_input)
f.write('\n')
f.close()


f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt', 'w')
f.write(body)
f.close()

