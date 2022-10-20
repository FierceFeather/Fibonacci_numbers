# Fibonacci function, recursive
def fibonacci(num):
    if 0 <= num <= 1:
        return num
    return fibonacci(num - 2) + fibonacci(num - 1)


# Entry point
def main():
    while (True):
        print("################################################################")
        print('Fibonacci number is ' + str(fibonacci(int(input('Type a sequence number you want to know: ')))))


# Running the project
if __name__ == '__main__':
    main()