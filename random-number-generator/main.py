from datetime import datetime

def random_number_generator(max):
    # from 1 to 10
    global seed
    a = 23493743894
    b = 5675673450
    m = max
    seed = (a*total_seconds+b) % m
    return seed

now = datetime.now()
now = now.strftime("%H:%M:%S")
current_time = datetime.strptime(now,'%H:%M:%S')
total_seconds = current_time.second + current_time.minute*60 + current_time.hour*3600
try:
    max = int(input("Enter the highest limit for the random number(10 by default): ")) + 1
except:
    max = 10
print(random_number_generator(max))


