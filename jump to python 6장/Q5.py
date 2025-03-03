import os

def search(dirname):
    try:
        filenames=os.listdir(dirname) #해당 디렉터리에 있는 파일들의 리스트
        for filename in filenames:
            full_filename=os.path.join(dirname,filename) #디렉터리와 파일 이름 이어줌
            if os.path.isdir(full_filename): #디렉터리인지 파일인지 구별
                search(full_filename) #디렉터리 파일이 디렉터리인 경우, 재귀 호출
            else:
                ext=os.path.splitext(full_filename)[-1] #확장자만 추출
                if ext=='.py':
                    print(full_filename)
    except PermissionError: #수행 권한없는 디렉터리에 접근할 때
        pass
    
search('C:\py')