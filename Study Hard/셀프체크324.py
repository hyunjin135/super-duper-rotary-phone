class ParkingManager:
    def __init__(self, capacity):
        self.capacity=capacity
        self.count = 0
        print("총 {0}대를 등록할 수 있습니다.".format(self.capacity))
        
    def register(self):
        if self.count>=self.capacity:
            print("더 이상 등록할 수 없습니다.")
               
        else:
            self.count+=1
            print("차량 신규 등록 {0}/{1}".format(self.count, self.capacity))
        
manager = ParkingManager(5)
for car in range(6):
    manager.register()


    