class TreeNode: #각각의 노드[<-, 값, ->]
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


if __name__ == "__main__":
    groups = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    #groups = [10,15,8,3,9]
    root = None

    node = TreeNode()
    node.data=groups[0] #루트 작업
    root = node     #초기화 작업

    #데이터 만들기
    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data: #노드값이 지금 입력하려는 값보다 크면
                if current.left is None: #노드가 비어있다면
                    current.left = node
                    break
                current = current.left #한번 이동
            else:                   #노드값이 지금 입력하려는 값보다 작으면
                if current.right is None: #노드가 비어있다면
                    current.right = node
                    break
                current = current.right #한번 이동

    print("구성완료")

    # 데이터 찾기
    find_group = input("찾을 그룹명을 입력하시오:")
    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f'{find_group}이(가) 존재하지 않습니다.')
                break
            current = current.left
        else:

            if current.right is None:
                print(f'{find_group}이(가) 존재하지 않습니다.')
                break
            current = current.right

    #데이터 삭제
    del_group = input("삭제할 그룹명을 입력하시오:")
    current = root #시작을 루트로
    parent = None #부모노드를 지정
    while True:
        #a.삭제하려는 값과 현재 노드의 값이 일치 할때
        if del_group == current.data:
            #자식이 없는 경우
            if current.left == None and current.right == None:
                if parent.left == current:#자신이 부모의 왼쪽에 있다면
                    parent.left = None
                else:                     #자신이 부모의 오른쪽에 있다면
                    parent.right =None
                del(current)

            #자식이 좌측에 있을 경우
            elif current.left != None and current.right == None:
                if parent.left == current:#자신이 부모의 왼쪽에 있다면
                    parent.left = current.right#자식의 위치를 부모의 방향에
                else:                     #자신이 부모의 오른쪽에 있다면
                    parent.left = current.right#자식의 위치를 부모의 방향에
                del(current)

            #자식이 우측에 있을 경우
            elif current.left == None and current.right != None:
                if parent.left == current:#자신이 부모의 왼쪽에 있다면
                    parent.left = current.right#자식의 위치를 부모의 방향에
                else:                     #자신이 부모의 오른쪽에 있다면
                    parent.left = current.right#자식의 위치를 부모의 방향에
                del(current)

            print(del_group,'이(가) 삭제됨.')
            break

        # a.삭제하려는 값 < 현재 노드의 값
        elif del_group < current.data:
            if current.left == None:
                print(del_group, '이(가) 트리에 없음')
                break
            parent =current
            current =current.left
        # a.삭제하려는 값 > 현재 노드의 값
        else:
            if current.right == None:
                print(del_group, '이(가) 트리에 없음')
                break
            parent =current
            current =current.right