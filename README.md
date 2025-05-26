Mermaid.live Diagram
![image](https://github.com/user-attachments/assets/4385397a-04f8-4a9b-a0e4-52e08d0c6c4a)






## `book.py`

주요 구성
- `class Book`  
  - `__init__(self, title, author)`  
    책 객체를 생성하는 생성자입니다. `title`과 `author` 속성을 가집니다.


- 이 모듈은 오직 책 데이터를 표현하는 역할만 하고 있어서 구조가 매우 단순함
- 다른 모듈에 의존하지 않으며, 데이터 구조 변경도 쉽게 할 수 있음

---

## `storage.py`

주요 함수
- `save_books(books, filename="books.txt")`  
  `Book` 객체 리스트를 텍스트 파일에 저장합니다. 한 줄에 한 권씩 `"제목,저자"` 형태로 씁니다.

- `load_books(filename="books.txt")`  
  텍스트 파일에서 책 목록을 읽어들여 `Book` 객체 리스트로 반환합니다.

- 파일 입출력 관련 기능만 따로 분리함
- `Book` 클래스는 필요하지만, UI나 흐름 제어와는 완전히 분리되어 있어 독립성이 높음

---

## `ui.py`

주요 함수
- `show_books(books)`  
  책 리스트를 순회하면서 `"제목 by 저자"` 형식으로 출력

- `get_book_info()`  
  사용자로부터 책의 제목과 저자를 입력받아 반환

- 사용자 입출력만 전담하고 있어 역할이 명확함
- 저장이나 데이터 구조와 분리되어 있어 다른 방식의 UI로 바꾸기도 수월함

---

## `main.py`

주요 구성
- `books = storage.load_books()`  
  기존 책 목록을 불러옵니다.

- `ui.show_books(books)`  
  책 목록을 출력합니다.

- `title, author = ui.get_book_info()`  
  사용자로부터 새 책 정보를 입력받음

- `new_book = Book(title, author)`  
  입력받은 정보를 기반으로 `Book` 객체를 생성

- `books.append(new_book)`  
  새 책을 목록에 추가

- `storage.save_books(books)`  
  전체 목록을 파일에 저장

- 프로그램 전체 흐름을 깔끔하게 조율하는 메인 파일
- 여러 모듈을 가져다 쓰기 때문에 상대적으로 결합은 있으나, 각 기능은 분리된 모듈에 위임해 구조가 안정적

