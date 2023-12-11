import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    print('Focus Time is over!')

def start_timer():
    focus_time = int(input("Enter focus time in seconds: "))
    print("Focus timer started for {} seconds.".format(focus_time))
    countdown(focus_time)

start_timer()
