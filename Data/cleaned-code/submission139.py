import threading
import time

                                                      
def print_numbers(name, delay):
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(delay)                                     

                                                                   
def main():
    thread1 = threading.Thread(target=print_numbers, args=("Thread 1", 1))
    thread2 = threading.Thread(target=print_numbers, args=("Thread 2", 0.5))
    
    thread1.start()
    thread2.start()
    
    thread1.join()                               
    thread2.join()                               

if __name__ == "__main__":
    main()
