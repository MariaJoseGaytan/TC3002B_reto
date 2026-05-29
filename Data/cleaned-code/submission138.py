import threading
import time

                                             
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)                                     

                                              
def print_letters():
    for letter in "ABCDE":
        print(f"Thread 2: {letter}")
        time.sleep(0.5)                                        

                                                    
def main():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    
    thread1.start()
    thread2.start()
    
    thread1.join()                               
    thread2.join()                               

if __name__ == "__main__":
    main()
