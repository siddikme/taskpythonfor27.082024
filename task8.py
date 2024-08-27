def harmonic_sum(n):
    sum = 0.0
    for i in range(1, n + 1):
        sum += 1 / i
    return sum

n = int(input("Enter the number of terms for the harmonic series: "))

result = harmonic_sum(n)
print(f"The harmonic sum of {n} terms is: {result}")
