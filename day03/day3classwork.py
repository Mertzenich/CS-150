clock = 24
current_time = int(input("Enter the current time "))
wait_time = int(input("Enter the wait time "))
final_time = current_time + wait_time #%clock
print("Final Time: " , final_time % clock)