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
    find_group = input()
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