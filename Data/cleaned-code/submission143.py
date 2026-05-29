import psutil

                                        
def check_system_usage():
                              
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
                      
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

                                            
def main():
    check_system_usage()

if __name__ == "__main__":
    main()
