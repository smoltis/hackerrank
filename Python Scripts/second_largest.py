def second_largest2(numbers):
    maxN = max(numbers)
    numbers = list(filter(lambda x: x!=maxN, numbers))
    numbers.sort()
    return numbers[-1]
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(second_largest2(list(arr)))