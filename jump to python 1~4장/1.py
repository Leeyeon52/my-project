class BlackBox:

    def __init__(self, name, price):
            self.name = name
            self.price = price

class VideoMaker:
 def make(self):
 print('추억용 여행 영상제작')

class MailSender:
 def send(self):
 print('메일 발송')
        
class TravelBlackBox(BlackBox, VideoMaker):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

     def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행모드 on')
        
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_on(self, min):
        print(str(min)+'분 동안 여행모드 on')
        self.make()
        self.send()

b1 = TravelBlackBox('끼망이', 2000000, 64)
b1 = set_travel_on(30)