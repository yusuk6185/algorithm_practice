# 떡볶이를 만드려고 하는데 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
# 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기에 높이(H) 를 지정하면 줄지어진 떡을 한번에 절단한다. 높이가 H보다
# 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를 들어 높이가 19, 14, 10, 17cm 인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면
# 자른 뒤 떡의 높이는 15, 14, 10, 15cm 가 될것이다. 잘린 떡의 길이는 차례대로
# 4, 0, 0, 2cm 이다. 손님은 6cm 만큼의 길이를 가져간다.

# 손님이 왔을 때 요청한 길이가 일 때 적어도 M 만큼의 떡을 얻기 위해 절단기에
# 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

n, m = map(int, input().split())

d_list = list(map(int, input().split()))

# set start and end with the possible length of the ddeok
start = 0
end = max(d_list)

# set the binary search
result =0
while(start<=end):
    total = 0
    mid = (start + end) // 2
    # Add the length of each ddeok - current height
    for x in d_list:
        if x > mid:
            total += x - mid
    # if the total cut length is smaller than required length, make the height shorter to get bigger length 
    if total < m:
        end = mid - 1
    # if the total cut length is bigger than required length, set the current height as result and check if the height can be bigger.
    else:
        result = mid
        start = mid + 1
    
print(result)
    