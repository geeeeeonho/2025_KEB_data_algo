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


#내용 확인(후위순회)
def post_order(node):
    if node is None: #이동 한 노드의 값이 없으면 돌아간다.
        return
    post_order(node.left) #먼저 좌로 이동
    post_order(node.right)#그 다음 우로 이동
    print(f"{node.data} ", end='')#현 노드 출력이 제일 후순위


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    #생성
    for number in numbers: #반복문으로 삽입
        root = insert(root, number)

    #내용 출력
    print("BST 구성 완료")
    post_order(root)

    #검색
    print()
    find_number = int(input('값 찾기 :'))
    if search(root, find_number):
        print(f"{find_number}을(를) 찾았습니다")
    else:
        print(f"{find_number}이(가) 존재하지 않습니다")



