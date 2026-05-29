import psutil


                                                       
def monitor_system_utilization():
                                         
    cpu_util = psutil.cpu_percent(interval=1)
    print(f"CPU Utilization: {cpu_util}%")

                                 
    mem_info = psutil.virtual_memory()
    print(f"Memory Utilization: {mem_info.percent}%")

                                     
    disk_info = psutil.disk_usage('/')
    print(f"Disk Utilization: {disk_info.percent}%")


                                        
def execute_system_checks():
    monitor_system_utilization()


if __name__ == "__main__":
    execute_system_checks()
