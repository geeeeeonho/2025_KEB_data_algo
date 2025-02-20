class TreeNode: #각 노드 [<-,값(벨류),->]
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


#삽입(재귀함수 이용)
def insert(root, value):
    if root is None:    #현위치에 위치한 값이 없을 경우
        node = TreeNode()
        node.data = value
        return node

    if value < root.data:   #삽입하려는 값<위치한 값
        root.left = insert(root.left, value)#재귀함수(루트값에 루트의 왼쪽을)
    else:                   #삽입하려는 값>위치한 값
        root.right = insert(root.right, value)#재귀함수(루트값에 루트의 오른쪽을)
    return root


#내용 확인(후위순회)
def post_order(node):
    if node is None: #이동 한 노드의 값이 없으면 돌아간다.
        return
    post_order(node.left) #먼저 좌로 이동
    post_order(node.right)#그 다음 우로 이동
    print(f"{node.data} ", end='')#현 노드 출력이 제일 후순위


#내용 찾기(단축)
def search(root, value):
    current = root
    while current:
        if value == current.data:   #찾음
            return current
        elif value < current.data:  #검색 값<위치한 값
            current = current.left
        else:                       #검색 값>위치한 값
            current = current.right
    return None #찾아도 없으면 None


#삭제하기(재귀함수 이용)
def delete(root, value):
    if root is None:
        return root
    #a.삭제하려는 값<위치한 값
    if value < root.data:
        root.left = delete(root.left, value)#재귀함수(루트값에 루트의 왼쪽을)
    #a.삭제하려는 값>위치한 값
    elif value > root.data:
        root.right = delete(root.right, value)#재귀함수(루트값에 루트의 오른쪽을)
    # a.삭제하려는 값 = 현 노드에 위치한 값
    else:
        if root.left is None and root.right is None:#자식이 없는 경우
            return None
        elif root.left is None: #자식이 오른쪽에만 경우
            return root.right#자식 값으로 대체
        elif root.right is None:#자식이 왼쪽에만 경우
            return root.left #자식 값으로 대체
        else:  # 자식이 두 개인 경우
            root.data = find_min(root.right).data   #current.data가 된다
            root.right = delete(root.right, root.data)#원래 위치는 삭제
    return root #최종적으로는 삭제하려는 값이 위치한 노드를 리턴한다

#삭제하기에서 최소값 찾기(자식의 우측 중에서 가장 작은 값을 찾기)
def find_min(node):
    current = node  #현 노드 확인
    while current.left is not None: #가장 왼쪽의 값
        current = current.left
    return current
    """
    find_min(root.right) : ->
        current = current.left : <-
        current = current.left : <-
        ...
    """



if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    #생성
    for number in numbers: #반복문으로 삽입
        root = insert(root, number)
    print("BST 구성 완료")

    while True:
        ask=input('원하는 메뉴를 고르시오\n 1)출력 2)검색 3)삭제 4)종료 : ')
        if ask=='1': #내용 출력
            post_order(root)
            print()

        elif ask=='2': #내용 검색
            find_number = int(input('값 찾기 :'))
            if search(root, find_number):
                print(f"{find_number}을(를) 찾았습니다")
            else:
                print(f"{find_number}이(가) 존재하지 않습니다")

        elif ask == '3':  # 내용 삭제
            delete_number = int(input('삭제할 값 :'))
            #삭제할 값이 있는 지 찾아본다.
            if search(root, delete_number):
                root = delete(root, delete_number)
                print(f"{delete_number} 삭제 완료")
            else:
                print(f"{delete_number}은(는) 트리에 존재하지 않습니다.")

        elif ask == '4':  # 종료
            print('종료')
            break






