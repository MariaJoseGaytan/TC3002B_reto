import threading
import time

                                     
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)                                     

                                              
def main():
    thread1 = threading.Thread(target=print_numbers)
    thread1.start()
    thread1.join()                                   

if __name__ == "__main__":
    main()
