import psutil

                                         
def check_network_and_cpu():
                              
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
                                
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")

                                        
def main():
    check_network_and_cpu()

if __name__ == "__main__":
    main()
