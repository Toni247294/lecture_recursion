def recursive_nth_fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)

def main():
    print(recursive_nth_fibo(5))


if __name__ == "__main__":
    main()
