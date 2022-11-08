"""
Write a function called process that receives a variable number of keyword arguments
The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
-If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument
and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
-If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
-If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.

The function will return the processed numbers.
"""


def sum_digits(x):
    return sum(map(int, str(x)))


def generate_fibonacci(n):
    ans = [0, 1]
    for i in range(2, n):
        ans.append(ans[i - 2] + ans[i - 1])

    return ans


def process(**kwargs):
    fibonacci_seq = generate_fibonacci(1000)
    if "filters" in kwargs.keys():
        for filtru in kwargs["filters"]:
            fibonacci_seq = list(filter(filtru, fibonacci_seq))
            
    if "offset" in kwargs.keys():
        fibonacci_seq = fibonacci_seq[kwargs["offset"]:]

    if "limit" in kwargs.keys():
        fibonacci_seq = fibonacci_seq[:kwargs["limit"]]

    return fibonacci_seq


if __name__ == '__main__':
    result = process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=2,
        offset=2
    )
    print(result)