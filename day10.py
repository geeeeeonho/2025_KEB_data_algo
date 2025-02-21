#버블 정렬(오름차순)
def bubble_sort(l):
    l_length=len(l) - 1
    for i in range(l_length-1):
        for j in range(l_length-1-i):   #전체 크기에서 이미 처리한 수는 제외
            if l[j] > l[j+1]:
                l[j] , l[j + 1] = l[j+1] , l[j] #둘의 위치 변경
            print(j, end = ' ')
    return l #최종 변경 내용 제출

alist=[33,8,-11,9,1]
print(bubble_sort(alist))