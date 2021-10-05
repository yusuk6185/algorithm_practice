# 전자 매장에 부품 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이
# M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 떄를
# 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None             

# check the item list in the store
n = int(input())
n_list = list(map(int, input().split()))

# check the required item list
m = int(input())
m_list = list(map(int, input().split()))

# sort to use binary search
n_list.sort()
result = []

# use binary search for each item required
for i in m_list:
    result.append(binary_search(n_list, i, 0, n-1))

# print yes if there is such item or no if not
for i in range(m):
    if result[i] == None:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')
