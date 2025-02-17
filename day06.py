import random as rd


try:
    with open("students.csv",'r') as fp:
        open_list=fp.readlines()
        open_list.remove("이상혁\n")
        open_list.remove("조윤하\n")
        open_list.remove("김철중n")
        open_list.remove("김현민\n")
        open_list.remove("김찬빈\n")
        n=int(input('뽑을 사람의 수:'))
        for i in range(n):
            randpick=rd.choice(open_list)
            print(randpick, end='')
            open_list.remove(randpick)
except FileNotFoundError as err:
    print(err)