def print_fibonacci(length):
    """Prints a list of the Fibonacci sequence up to the specified length."""
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        list_fib = [0, 1]
        while len(list_fib) < length:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        print(list_fib)

# You can keep the example usage for manual testing if needed:
# print(print_fibonacci(9))