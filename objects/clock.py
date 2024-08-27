
import pygame, time



    
class Clock:
    def __init__(self):
        self.prev_time = time.time()
        self.min = 0
        self.hour = 5
        self.ampm_tracker = 2
        self.ampm = ('PM', 'AM')
        self.paused_time = (0, 0, 2)

    
    def format_time(self) -> str:
        min = str(self.min)
        if self.min < 10:
            min = '0' + min
        hour = str(self.hour)
        if self.hour < 10:
            hour = '0' + hour
        return f'{hour}:{min} {self.ampm[self.ampm_tracker%2]}'
    
    def update(self) -> None:
        self.cur_time = time.time()
        if self.cur_time - self.prev_time > 2.5:
            self.prev_time = self.cur_time
            self.min += 1
        if self.min == 60:
            self.min = 0
            self.hour += 1
        if self.hour > 12:
            self.hour = 1
            self.ampm_tracker += 1
            
    def set_time(self, time: (int, int, int)) -> None:
        self.hour = time[0]
        self.min = time[1]
        self.ampm_tracker = time[2]
        self.prev_time = time.time()
        
    def pause_time(self) -> None:
        self.paused_time = (self.hour, self.min, self.ampm_tracker)
            
    def unpause_time(self) -> None:
        self.set_time(self.paused_time)
    
        

class RaceClock:
    def __init__(self):
        self.prev_time = time.time()
        self.sec = 0
        self.min = 0
        self.hour = 0
        
    def format_time(self) -> str:
        sec = str(self.sec)
        if self.sec < 10:
            sec = '0' + sec
        min = str(self.min)
        if self.min < 10:
            min = '0' + min
        hour = str(self.hour)
        if self.hour < 10:
            hour = '0' + hour
        return f'{hour}:{min}:{sec}'

    def update(self) -> None:
        self.cur_time = time.time()
        if self.cur_time - self.prev_time > 0.0416:
            self.prev_time = self.cur_time
            self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
        if self.min == 60:
            self.min = 0
            self.hour += 1
        if self.hour > 12:
            self.hour = 1
            self.ampm_tracker += 1
            
    def start(self) -> None:
        self.prev_time = time.time()
        
    def get_time(self) -> (int, int, int):
        return (self.hour, self.min, self.sec)
    
class Timer:
    def __init__(self, length: (int, int, int)):
        self.prev_time = time.time()
        self.complete = True
        self.sec = 0
        self.min = 0
        self.hour = 0
    
    
    def format_time(self, hour: int, min: int, sec: int) -> str:
        if sec < 10:
            sec = '0' + str(sec)
        if min < 10:
            min = '0' + str(min)
        if hour < 10:
            hour = '0' + str(hour)
        return f'{hour}:{min}:{sec}'

    def update(self) -> bool:
        if self.get_time() >= self.timer_amnt:
            self.complete = True
            return
        
        self.cur_time = time.time()
        if self.cur_time - self.prev_time > 0.0416:
            self.prev_time = self.cur_time
            self.sec += 1
            
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            
        if self.min == 60:
            self.min = 0
            self.hour += 1
            
        if self.hour > 12:
            self.hour = 1
            
    
    def set_timer(self, timer_amnt: (int, int, int)) -> None:
        self.timer_amnt = timer_amnt
        self.prev_time = time.time()
        self.complete = False
        
    def get_time(self) -> (int, int, int):
        return (self.hour, self.min, self. sec)
    
    def get_timer_amnt(self) -> str:
        return self.format_time(self.timer_amnt[0], self.timer_amnt[1], self.timer_amnt[2])

    def get_remaining_time(self) -> str:
        return self.format_time(self.timer_amnt[0] - self.hour, self.timer_amnt[1] - self.min, self.timer_amnt[2] - self.sec)
    
    def get_elapsed_time(self) -> (int, int, int):
        return self.format_time(self.hour, self.min, self.sec)
        
    