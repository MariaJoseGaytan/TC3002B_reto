import psutil

                             
def check_cpu_usage():
                              
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

                                    
def main():
    check_cpu_usage()

if __name__ == "__main__":
    main()
