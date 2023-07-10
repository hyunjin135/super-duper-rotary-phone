# import os


# folder =  "sample_dir"
# if os.path.exists(folder):
#     print("폴더가 이미 있습니다")
#     os.rmdir(folder)
#     print("폴더를 삭제합니다")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성했습니다")

# print(os.listdir())

# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일")

def say_hello(to):
    print("안녕, {0}?".format(to))

def say_goodbye(to):
    print("또 만나 {0}".format(to))


if __name__ == "__main__":
    print("이 문장은 모듈을 직접실행할 때만 출력됩니다.")
    say_hello("파이썬")
    say_goodbye("나도코딩")