class Try:
    def rsp(self, mine, yours):
        allowed = ['가위','바위', '보']
        if mine not in allowed:
            raise ValueError
        if yours not in allowed:
            raise ValueError

try:
    myTry = Try()
    myTry.rsp('가위', '바위보')
    print('OK')
    
except ValueError:
    print('가위 바위 보를 입력하시오')

try:
    # 테스트를 위해 파일 생성
    open('__test.txt', 'w').close()

    # 파일을 읽기로 연다.
    f = open('__test.txt','r')
    # 파일에 뭔가를 쓰면 예외
    f.write('xxx')
except OSError as e:
    print('Exception: {}'.format(e))

finally:                           #<---- 1
    f.close()                      #<---- 2
    print('release file')
