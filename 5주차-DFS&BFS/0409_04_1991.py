"""
    백준 1991 : 트리순회
"""

def ensure_size(tree, idx):
    """tree 리스트가 idx까지 접근 가능하도록 확장"""
    if idx >= len(tree):
        tree.extend([''] * (idx - len(tree) + 1))

def preorder(tree, p):
    if p >= len(tree) or tree[p] == '.' or tree[p] == '':
        return
    print(tree[p], end='')
    preorder(tree, p*2)
    preorder(tree, p*2+1)

def inorder(tree, p):
    if p >= len(tree) or tree[p] == '.' or tree[p] == '':
        return
    inorder(tree, p * 2)
    print(tree[p], end='')
    inorder(tree, p*2+1)

def postorder(tree, p):
    if p >= len(tree) or tree[p] == '.' or tree[p] == '':
        return
    postorder(tree, p * 2)
    postorder(tree, p * 2 + 1)
    print(tree[p], end='')

"""
    첫째줄 : N - 이진 트리 노드의 개수
    다음 N개의 줄 : 각 노드와 그의 왼쪽 자식, 오른쪽 자식이 주어진다. ( A B C )
    노드는 A부터 차례대로 매겨짐. 항상 A가 루트, 자식 노드가 없다면 '.'으로 표현
"""
N = int(input())
"""
    이진 트리를 배열로 구현할 때,
    부모 = 자식/2   (루트는 1부터 시작)
    왼쪽 자식 = 부모*2
    오른쪽 자식 = 부모*2+1
"""
tree = ['', 'A']
for _ in range(N):
    parent, left, right = input().split()
    p = tree.index(parent)

    ensure_size(tree, p * 2 + 1)
    tree[p * 2] = left
    tree[p * 2 + 1] = right
    pass

preorder(tree, 1)
print()
inorder(tree, 1)
print()
postorder(tree, 1)