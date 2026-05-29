import psutil

                                               
def check_full_system_usage():
                              
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
                      
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    
                    
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")

                                         
def main():
    check_full_system_usage()

if __name__ == "__main__":
    main()
