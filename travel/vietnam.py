class VietnamPackage:
    def detail(self):
        print("[베트남 3박 5일 패키지], 다낭 효도 여행 50만원")


if __name__ == "__main__": 
    print("vietnam모듈 직접실행")
    print("이 문장은 모듈을 직접 실행할 때만 출력돼요")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("외부에서 vietnam에서 호출")