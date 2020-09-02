def Fibonacci(n):
    if n <= 0: return n
    memo = [-1] * (n+1)

    return fib(n, memo)


def fib(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    print(memo)
    return memo[n]


if __name__ == '__main__':
    print(Fibonacci(4))

