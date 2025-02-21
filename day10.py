#버블 정렬(오름차순)
def bubble_sort(l):
    l_length=len(l) - 1
    for i in range(l_length-1):
        no_swap = True          #스왑 설정
        for j in range(l_length-1-i):   #전체 크기에서 이미 처리한 수는 제외
            if l[j] > l[j+1]:
                l[j] , l[j + 1] = l[j+1] , l[j] #둘의 위치 변경
                no_swap = False #스왑설정
                print(j,end=' ')
        if no_swap: #변경되는 내용이 없다면 확인의 필요가 없음
            return l
    return l #최종 변경 내용 제출


#삽입정렬
def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]   #비교할 변수를 백업
        while i > 0 and l[i-1] > value:#변수보다 앞의 값이 더 크면
            l[i] = l[i-1]             #앞의 위치에 이동
            i=i-1
            print(i,  end= ' ')
        l[i]=value #while이 끝나면 벨류를 현재 위치로 옮김
    return l

alist=[13,33,99,15,100,29,-11,3]
print(bubble_sort(alist))
print(insertion_sort(alist))