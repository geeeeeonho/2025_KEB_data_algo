class TreeNode: #각각의 노드[<-, 값, ->]
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


#트리 생성 함수
def make_tree(ingroups):
    node = TreeNode()
    node.data = ingroups[0]  # 루트 작업
    root = node  # 초기화 작업
    global rootGB   #글로벌 루트 생성
    rootGB=root

    # 루트 아래의 노드 생성
    for group in ingroups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:  # 노드값이 지금 입력하려는 값보다 크면
                if current.left is None:  # 노드가 비어있다면
                    current.left = node
                    break
                current = current.left  # 한번 이동
            else:  # 노드값이 지금 입력하려는 값보다 작으면
                if current.right is None:  # 노드가 비어있다면
                    current.right = node
                    break
                current = current.right  # 한번 이동

    print("구성완료")

#찾기 함수
def tree_search(find_group):
    root = rootGB #초기 루트 설정(글로벌)
    current = root #현재 위치 지정(루트)
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

#삭제 함수
def tree_delete(del_group):
    # 데이터 삭제
    root = rootGB #초기 루트 설정(글로벌)
    current = root  # 시작을 루트로
    parent = None  # 부모노드를 지정
    while True:
        # a.삭제하려는 값과 현재 노드의 값이 일치 할때
        if del_group == current.data:
            # 자식이 없는 경우
            if current.left == None and current.right == None:
                if parent.left == current:  # 자신이 부모의 왼쪽에 있다면
                    parent.left = None
                else:  # 자신이 부모의 오른쪽에 있다면
                    parent.right = None
                del (current)

            #b.자식이 좌측에 있을 경우
            elif current.left != None and current.right == None:
                if parent.left == current:  # 자신이 부모의 왼쪽에 있다면
                    parent.left = current.left  #b.자식의 위치를 부모의 방향에
                else:  # 자신이 부모의 오른쪽에 있다면
                    parent.right = current.left  #b.자식의 위치를 부모의 방향에
                del (current)

            #c. 자식이 우측에 있을 경우
            elif current.left == None and current.right != None:
                if parent.left == current:  # 자신이 부모의 왼쪽에 있다면
                    parent.left = current.right  #c. 자식의 위치를 부모의 방향에
                else:  # 자신이 부모의 오른쪽에 있다면
                    parent.right = current.right #c. 자식의 위치를 부모의 방향에
                del (current)

            #d. 자식이 두개인 경우
            elif current.left != None and current.right != None:
                if parent.left == current:  # 자신이 부모의 왼쪽에 있다면
                    #임시 부모주소 생성
                    sub_parent = current
                    #삭제할 값의 자식 중에서 가장 중간 찾기(우->좌->좌...)
                    sub_current = current.right
                    while sub_current.left is not None:
                        sub_parent = sub_current
                        sub_current = sub_current.left
                    sub_parent.left =None #기존의 위치에서는 값이 사라져야 함
                    current=sub_current #자식의 값으로 바꾼다.
                    parent.left = current #위치를 업데이트
                    del current
                else:  # 자신이 부모의 오른쪽에 있다면
                    # 임시 부모주소 생성
                    sub_parent = current
                    # 삭제할 값의 자식 중에서 가장 중간 찾기(우->좌->좌...)
                    sub_current = current.right
                    while sub_current.left is not None:
                        sub_parent = sub_current
                        sub_current = sub_current.left
                    sub_parent.left = None  # 기존의 위치에서는 값이 사라져야 함
                    current = sub_current  # 자식의 값으로 바꾼다.
                    parent.right = current  # 위치를 업데이트
                    del current

            print(del_group, '이(가) 삭제됨.')
            break

        # a.삭제하려는 값 < 현재 노드의 값
        elif del_group < current.data:
            if current.left == None:
                print(del_group, '이(가) 트리에 없음')
                break
            parent = current
            current = current.left
        # a.삭제하려는 값 > 현재 노드의 값
        else:
            if current.right == None:
                print(del_group, '이(가) 트리에 없음')
                break
            parent = current
            current = current.right



if __name__ == "__main__":
    groups = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']
    make_tree(groups)

    while True:
        ask=input('원하는 메뉴를 고르시오 1)찾기 2)삭제 3)종료:')
        if ask == '1':
            ask1 = input('찾기를 원하는 그룹명:')
            tree_search(ask1)
        elif ask == '2':
            ask1 = input('삭제를 원하는 그룹명:')
            tree_delete(ask1)
        elif ask == '3':
            print('종료')
            break