import time
import random
#시간 체크
def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper




#버블 정렬(오름차순)
@time_decorator
def bubble_sort(l):
    l_length=len(l) - 1
    for i in range(l_length):
        no_swap = True          #스왑 설정
        for j in range(l_length-i):   #전체 크기에서 이미 처리한 수는 제외
            if l[j] > l[j+1]:
                l[j] , l[j + 1] = l[j+1] , l[j] #둘의 위치 변경
                no_swap = False #스왑설정
        if no_swap: #변경되는 내용이 없다면 확인의 필요가 없음
            return l
    return l #최종 변경 내용 제출


#삽입정렬
@time_decorator
def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]   #비교할 변수를 백업
        while i > 0 and l[i-1] > value:#변수보다 앞의 값이 더 크면
            l[i] = l[i-1]             #앞의 위치에 이동
            i=i-1
        l[i]=value #while이 끝나면 벨류를 현재 위치로 옮김
    return l

#무작위의 백만개 리스트
lists1 = [random.randint(1,100000) for _ in range(10000)]
lists2=lists1.copy()
print('버블 정렬 과정\n')
bubble_sort(lists1)
print('삽입 정렬 과정\n')
insertion_sort(lists2)