message = '나는야 전역 변수'
print(message)

def no_secret():
    global message
    message = '전역변수인가?'
    print(message)
    
no_secret()
print(message)