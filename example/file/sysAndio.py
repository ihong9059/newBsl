f = open('todo.txt', 'wt')
f.write('2016-05-01\n')
f.write(' - [ ] 책읽기\n')
f.write(' - [ ] 커피 한잔\n')
f.write(' - [ ] 회의\n')
f.close( )

f = open("todo.txt", "r")
data = f.read( )
print(data)
f.close( )

f = open('todo.txt', 'r+')
f.seek(16, 0)
f.write('X')
f.close

f = open("todo.txt", "r")
data = f.read( )
print(data)
f.close( )

import sys
print("This is message for standard output")
print("Thie is message for standard output by sys.stdou", file=sys.stdout)
sys.stdout.write("Thie is message for standard output")

import io
f = io.StringIO( )
f.write('2016-05-01\n')
f.write(' - [ ] 책읽기\n')
f.write(' - [ ] 커피한잔\n')
f.write(' - [ ] 회의\n')

# getvalue()로 출력한 내용을 볼 수 있음
print(f.getvalue( ))
f.close( )
