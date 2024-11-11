
#d입력1
# a, b, c = map(int, input().split())
# print(a,b,c,)

#입력2
# import sys 
#문자열 입력받기 
# data = sys.stdin.readline().rstrip()
# print(data)

#출력할 변수들
# a = 1
# b = 2
# print(a,b)
# print(7, end= " ")
# print(8, end= " ")
# #출력할변수들
# answer = 7
# print("정답은 " + str(answer)+ "입니다.")

# 입출력
# n = int(input())
# data = list(map(int, input().split()))
# print(n)
# print(data)

# 조건문 
# score = 85
# result = "Suc123cess" if score >= 80 else "Fail"

# print(result)

# 조건문2
# x = 15
# if 0 < x < 20:
#     print("x는 0이상 20미만의 수입니다.") 

#for문 
# result = 0
# for i in range(1,10):
#     if i % 2 == 0:
#         continue
#     result += i
# print (result)

#반복문 예제 
# score = [90, 85, 77, 65, 97]
# cheating_strudent_list = {2,4}

# for i in range (5):
#     if i+1 in cheating_strudent_list:
#         continue
#     if score[i] >= 80:
#         print(i+1, "번 학생은 합격입니다.")

# in 사용하기
# fruits = ["apple", "banana","cherry"]
# if "apple" in fruits:
#     print("사과가 리스트에 있습니다.")

# sentence = "Hello, welcome to the world of Python!"
# if "Python" in sentence:
#     print("문장에 Python이 포함되어 있습니다.")

# person = {"name": "Alice", "age": 25}
# if "name" in person:
#     print("이름이 딕셔너리에 있습니다.")    

# colors = ("red", "blue", "green")
# if "blue" in colors:
#     print("파란색이 튜플에 포함되어 있습니다.")

# fruits = ["apple", "banana", "cherry"]
# if "orange" not in fruits:
#     print("오렌지는 리스트에 없습니다.")

# 구구단예제
# for i in range(2,10):
#     for j in range(1,10):
#         print(i, "X",j, "=", i*j)
#     print()

# global 키워드 

# a = 0

# def func():
#     global a 
#     a += 1 
    
# for i in range(10):
#     func()

# print(a)


# # 람다 표현식으로 구현한 add() 메서드
# def add(a,b):
#     return a+b
# # 일반적인 add()메서드 사용
# print(add(3,7))

# # 람다 표현식
# print((lambda a, b: a+b)(3,4))

# 람다표현식 예시: 내장 함수에서 자주 사용되는 람다 함수

# array = [('홍길동', 50),('이순신', 32),('아무개', 74)]
# def my_key(x):
#     return x[1]
# print(sorted(array, key=my_key))

# array = [('홍길동', 50),('이순신', 32),('아무개', 74)]
# sorted_array  = sorted(array, key=lambda x: x[1])
# print(sorted_array)

# 람다 표현식 예시 : 여러개의 리스트에 적용 
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# result = map(lambda a, b: a + b, list1, list2)
# print(list(result))

# 실전에서 유용한 표준 라이브러리
