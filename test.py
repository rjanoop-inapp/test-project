import threading
import time

# Define the first function
def first_function():
    for i in range(20):
        print("Executing first function...")
        time.sleep(3)  # Simulate some time-consuming task

# Define the second function
def second_function():
    for i in range(20):
        print("Executing second function...")
        time.sleep(5)  # Simulate some time-consuming task

# Create threads for each function
thread1 = threading.Thread(target=first_function)
thread2 = threading.Thread(target=second_function)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both functions have finished executing.")