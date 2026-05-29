import logging

def is_valid_integer(n):
                                                       
    return isinstance(n, int) and n >= 0

def factorial(n):
                                                            
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def log_result(n, result):
                                             
    logging.basicConfig(filename='factorial.log', level=logging.INFO)
    logging.info(f"Factorial of {n} is {result}")

def calculate_factorial():
    try:
        num = int(input("Enter a non-negative integer: "))
        if not is_valid_integer(num):
            raise ValueError("Input must be a non-negative integer.")
        result = factorial(num)
        log_result(num, result)
        print(f"Factorial of {num} is {result}")
    except ValueError as e:
        print(e)

def main():
    while True:
        calculate_factorial()
        cont = input("Do you want to calculate another factorial? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
