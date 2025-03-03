import sys

option=sys.argv[1] #프로그램 실행 옵션 값
if option=='-a':
    memo=sys.argv[2] #메모내용
    f=open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()

#메모 출력 부분
elif option=='-v':
    f=open('memo.txt')
    memo=f.read()
    f.close()
    print(memo)