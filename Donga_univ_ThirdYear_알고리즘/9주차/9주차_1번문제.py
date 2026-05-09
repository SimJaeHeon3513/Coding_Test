import sys

n = int(sys.stdin.readline().strip())
ino = []
preo = []
posto = []
k = []

# 전위, 중위, 후위 순회 결과 입력받기
for _ in range(2):
    k_input = int(sys.stdin.readline().strip())
    k.append(k_input)
    if k_input == -1:
        for j in range(n):
            v = int(sys.stdin.readline().strip())
            preo.append(v)
    elif k_input == 0:
        for j in range(n):
            v = int(sys.stdin.readline().strip())
            ino.append(v)
    elif k_input == 1:
        for j in range(n):
            v = int(sys.stdin.readline().strip())
            posto.append(v)

# print(preo, ino, posto, k)
def print_preorder(post_start, post_end, in_start, in_end, postorder, idx_map):
    if post_start > post_end or in_start > in_end:
        return None

    root = postorder[post_end]
    print(root)

    root_idx = idx_map[root]
    left_size = root_idx - in_start
    
    # 문제의 구간 (인덱스 계산 및 호출)
    print_preorder(post_start, post_start + left_size - 1, in_start, root_idx - 1, postorder, idx_map)
    print_preorder(post_start + left_size, post_end - 1, root_idx + 1, in_end, postorder, idx_map)

def print_postorder(pre_start, pre_end, in_start, in_end, preorder, idx_map):
    if pre_start > pre_end or in_start > in_end:
        return None

    root = preorder[pre_start]
    root_idx = idx_map[root]
    left_size = root_idx - in_start

    print_postorder(pre_start + 1, pre_start + left_size, in_start, root_idx - 1, preorder, idx_map)
    print_postorder(pre_start + left_size + 1, pre_end, root_idx + 1, in_end, preorder, idx_map)
    print(root)

m = {val: i for i, val in enumerate(ino)}
if 1 in k:
    print_preorder(0, len(posto) - 1, 0, len(ino) - 1, posto, m)
elif -1 in k:
    print_postorder(0, len(preo) - 1, 0, len(ino) - 1, preo, m)