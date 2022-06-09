def multiply(num1, num2):
    if num1 == 0:
        return 0
    ans = num2
    ans += multiply(num1 - 1, num2)

    return ans

print(multiply(12,3))
