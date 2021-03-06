from  pprint import pprint
import pickle

person1 = {
    'name': '김하나',
    'height': 170,
    'weight': 60
}
person2 = {
    'name': '이대호',
    'height': 200,
    'weight': 80
}

# 데이터를 리스트로 만들었다.
people = [person1, person2]

# 데이터를 저장한다.
with open('people.pickle', 'wb') as f:   #<---- 1
    pickle.dump(people, f)               #<---- 2

# 저장된 데이터를 읽는다.
with open('people.pickle', 'rb') as f:   #<---- 3
    loaded_people = pickle.load(f)       #<---- 4

pprint(loaded_people)


class Book:
    """책 정보들을 파일이 저장하는 클래스"""

    def __init__(self, category):
        self.category = category
        self.books = []

    def addBook(self, book_title):
        if book_title not in self.books:
            self.books.append(book_title)

    def getBooks(self):
        return self.books

    def __getstate__(self):          #<---- 1
        state = self.__dict__.copy()
        # 여기서 필요없는 데이터를 삭제할 수 있다.
        return state

    def __setstate__(self, state):   #<----- 2
        self.__dict__.update(state)

if __name__ == '__main__':

    # Book 객체를 만든다.
    book = Book('my book')
    book.addBook('book 1')
    book.addBook('book 2')
    print(book.getBooks())

    # 객체를 바이너리 데이터로 만들고
    pickled_data = pickle.dumps(book)

    # 다시 객체화한다.
    new_book = pickle.loads(pickled_data)

    # 기존 데이터와 동일한 데이터의 객체
    print(book.getBooks())
