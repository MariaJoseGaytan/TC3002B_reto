import psutil

                                     
def monitor_cpu_utilization():
                                         
    utilization = psutil.cpu_percent(interval=1)
    print(f"Current CPU Utilization: {utilization}%")

                                             
def run_monitor():
    monitor_cpu_utilization()

if __name__ == "__main__":
    run_monitor()
