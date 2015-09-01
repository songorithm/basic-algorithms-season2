# Basic Data Strunctures
## What Are Linear Structures?

* Stacks, queues, degues, lists 등은 순서를 가진 항목을 가진 데이터 컬렉션
* 아이템 추가, 삭제 방식 차이 있음
* 한번 아이템이 추가되면 이전과 이후에 들어온 다른 엘리먼트들과의 상대적인 위치를 유지
* 이러한 것들을 선형 데이터 구조라고 함
* 선형 구조는 두 개의 끝을 가지고 있음
* "left", "right" 혹은 "front", "rear" 혹은 "top","bottom"
* 여러 가지의 데이터 추가 및 삭제 방식을 이용하여 가장 유용한 데이터 구조를 제공
* 많은 알고리즘에서 사용되며, 여러가지 다양한 문제를 풀 수 있도록 함

## The Stack Abstract Data Type
*  Stack 추상 데이터 타입은 다음의 구조와 연산으로 정의
* Stack은 끝에 위치한 "Top"에 아이템을 추가하거나 제거하는 순서를 가지는 LIFO(Last in First Out)
* LIFO == FILO
* 마지막에 들어온 것이 첫 번째로 나옴
* 첫 번째로 들어온 것이 마지막에 나옴
* Pringles와 유사한 구조, 과자통의 맨 끝에 있는 과자가 첫 번째로 나옴. 맨 처음 들어간 과자는 마지막에 먹을 수 있음 

![Pringles](http://www.benekeith.com/images/food/pringles_1.jpg)

* Stack() : 비어있는 새로운 stack을 생성(return empty stack)
* Push(item) : stack의 꼭대기에 새로운 아이템을 추가(return nothing)
* pop() : stack 꼭대기의 아이템을 제거(return item, stack 변경됨)
* peek() : stack의 꼭대기 아이템을 리턴하나 제거하지는 않음(stack 변경 없음)
* isEmpty() : stack이 비어있는지를 테스트(리턴 True or False)
* size() : stack의 아이템의 갯수를 리턴(리턴 integer)


Table 1: Sample Stack Operations

|Stack Operation|Stack Contents|	Return Value|
|:--------------|:-------------|--------------:|
|s.isEmpty()    |[]          	|True           |
|s.push(4)      |[4]           ||	 
|s.push('dog')|	[4,'dog']||	 
|s.peek()|	[4,'dog']|	'dog'|
|s.push(True)|	[4,'dog',True]||	 
|s.size()|	[4,'dog',True]|	3|
|s.isEmpty()|	[4,'dog',True]|	False|
|s.push(8.4)|	[4,'dog',True,8.4]||	 
|s.pop()|	[4,'dog',True]|	8.4|
|s.pop()|	[4,'dog']|	True|
|s.size()|	[4,'dog']|	2|

## Implementing a Stack in Python

* Python으로 Stack 구현해보기
* Stack이라는 새로운 클래스를 만들고(추상 데이터 타입)
* Stack 연산을 Method로 구현
* Python에서 제공하는 primitive collection 사용
* List를 활용(리스트의 끝은 스택의 Top)

```
	class Stack:
     	def __init__(self):
         	self.items = []

     	def isEmpty(self):
         	return self.items == []

     	def push(self, item):
         	self.items.append(item)

     	def pop(self):
         	return self.items.pop()

     	def peek(self):
         	return self.items[len(self.items)-1]

     	def size(self):
         	return len(self.items) 
 ```
 
 * pythonds 모듈을 이용한 Stack 클래스 활용 예
 * pythonds 모듈은 이책에서 논의되는 모든 데이터 구조들이 구현되어 있음([pythonworks.org](http://www.pythonworks.org/pythonds)에서 다운로드 가능)
* 다운로드 후 압축 해제, /Users/username/anaconda/lib/python2.7/site-packages 위치에 복사
 
```
from pythonds.basic.stack import Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
```
* list를 이용해서 Stack을 구현할 때 list의 끝 대신 시작을 "Top"으로 하는 경우 pop, append method는 사용 불가
* append를 인덱스 포지션 0을 명시한 insert로
* pop를 인덱스 포지션 0을 명시한 pop로

```
class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
	    return self.items == []
	
	def push(self, item):
	    self.items.insert(0,item)
	
	def pop(self):
	    return self.items.pop(0)
	
	def peek(self):
	    return self.items[0]
	def size(self):
		return len(self.items)
	
s = Stack()
s.push('hello')
s.push('true')
print(s.pop())

```
* append, pop() 연산은 O(1)
* insert(0), pop(0) 연산은 O(n)
* 논리적으로는 동일한 연산을 수행하더라도 성능테스트 수행 시 매우 다른 수행 시간 결과


## Simple Balanced Parentheses

* stack을 활용하여 computer science problems을 풀어봅시다.
* Balanced parenthesis

```
(()()()())

(((())))

(()((())()))

```
* Not Balanced

```
((((((())

()))

(()()(()
```
* 많은 프로그램 언어 구조에서 balanced parenthesis와 unbalanced parenthesis를 구분하는 것은 중요한 부분
* 왼쪽에서 오른쪽으로 심볼을 처리할 때 가장 최근에 열린 괄호는 다음에 닫히는 괄호와 반드시 매치되어야 함
* 맨 처음 열린 괄호는 맨 마지막 닫히는 괄호와 매칭될 때 까지 대기해야 함
* 닫히는 괄호는 나타난 순서의 역순으로 열리는 괄호와 매칭

![Figures 4: Matching Parentheses](http://interactivepython.org/courselib/static/pythonds/_images/simpleparcheck.png)

1. 빈 스택으로 시작
2. 왼쪽에서 오른쪽으로 괄호 문자를 처리
3. 만약 심볼이 열리는 괄호라면 stack에 push
4. 만약 심볼이 닫히는 괄호라면 stakck에서 pop
5. 모든 닫히는 괄호 심볼에 대해서 stack에서 pop 연산 가능하다면 balanced parenthesis
6. 만약 언제라도 닫히는 심볼에 대허서 매칭되는 열린 괄호 심볼이 없다면 unbalanced parenthesis
7. 문자열의 마지막에 모든 심볼에 대한 처리가 끝났다면, stack은 빈 상태여야 한다.

```
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))
```
## Balanced Symbols(A General Case)

* 밸런싱과 다른 종류의 열린 심볼과 닫힌 심볼의 중첩의 문제가 자주 발생
* 예를 들어 python 리스트에 사용되는 대괄호 [ ], 딕셔너리에 사용되는 중괄호 { }, 튜플이나 수치적 표현에 사용되는 괄호 ( ) 등이 열림과 닫힘 관계를 유지하면서 혼합될 수 있음

```
{ { ( [ ] [ ] ) } ( ) }

[ [ { { ( ( ) ) } } ] ]

[ ] [ ] [ ] ( ) { }
```
* 열림/닫힘 심볼 매칭 뿐만 아니라 심볼의 모양도 일치 해야 함
* 열림/닫힘 심볼은 매칭되나 심볼 모양이 매칭되지 않는 경우 예

```
( [ ) ]

( ( ( ) ] ) )

[ { ( ) ]
```

* 이전 섹션에서 작성한 간단한 괄호 체크 프로그램은 새로운 타입의 심볼([],{})을 처리를 위해 쉽게 확장이 가능
* 닫힘 심볼 처리 전까지의 모든 과정은 이전과 동일하며, 닫힘 심볼이 나타났을 때, stack의 top에 있는 열림 심볼과 동일한 종류의 심볼인지 검사하는 부분이 추가되는 것이 차이점

```
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
```

* 두 가지 예제는 stack이 computer science에서 언어 구성체 처리를 위한 매우 중요한 데이터 구조라는 것을 보여 줌
* computer science에는 많은 다른 중요한 stack의 용도가 있음
* 다음 섹션을 기대하시길...
 