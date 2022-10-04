class Time:
    def __init__(self, t):
        self.t = t
    def convert_to_minutes(self):
        m = self.t // 60
        s = self.t % 60 
        return f'{m}:{s}' 
    def convert_to_hours(self):
        h = self.t // 3600
        m = (self.t - h*3600) // 60
        s = self.t % 60
        return f'{h}:{m}:{s}'    

time1 = Time(3700)
print(time1.convert_to_hours())  
time2 = Time(230)
print(time2.convert_to_minutes())      