#버블 정렬(오름차순)
def bubble_sort(l):
    l_length=len(l) - 1
    for i in range(l_length):
        for j in range(l_length):
            if l[j] > l[j+1]:
                l[j] , l[j + 1] = l[j+1] , l[j] #둘의 위치 변경
    return l #최종 변경 내용 제출

alist=[8,-11,9,1]
print(bubble_sort(alist))