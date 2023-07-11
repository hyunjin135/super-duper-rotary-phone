# def price(people):
#     print("{0}명, 영화표 가격은 {1}원입니다.".format(people, people*10000))
# def price_morning(people):
#     print("{0}명, 조조영화표 가격은 {1}원입니다.".format(people, people*6000))
# def price_soldier(people):
#     print("{0}명, 군인영화표 가격은 {1}원입니다.".format(people, people*4000))

import greeting

if __name__ == "__main__":
    print("이 문장은 모듈을 직접실행할 때만 출력됩니다.")
else:
    print("외부에서 호출됨")
greeting.say_hello("파이썬")