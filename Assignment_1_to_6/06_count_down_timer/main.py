import time

def count_down(t):
    while t:
        mins, secs = divmod( t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        t -= 1
        time.sleep(1)
    print("Run...!")

user_input = int(input("Enter the seconds: "))
count_down(user_input)