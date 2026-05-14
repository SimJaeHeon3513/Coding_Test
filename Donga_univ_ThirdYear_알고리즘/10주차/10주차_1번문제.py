import sys
import re

sys.setrecursionlimit(200000)
input = sys.stdin.readline

K = int(input())

def parse(tokens, idx, counter):
    if tokens[idx] == "(":
        name = f"r{counter[0]}"
        counter[0] += 1

        left, idx = parse(tokens, idx + 1, counter)
        right, idx = parse(tokens, idx, counter)

        return (name, left, right), idx + 1

    else:
        return tokens[idx], idx + 1


def preorder(node):
    if isinstance(node, str):
        print(node)
    else:
        root, left, right = node
        print(root)
        preorder(left)
        preorder(right)


def inorder(node):
    if isinstance(node, str):
        print(node)
    else:
        root, left, right = node
        inorder(left)
        print(root)
        inorder(right)


for _ in range(K):
    s = input().strip()

    tokens = re.findall(r"[A-Z][A-Za-z0-9]*|\(|\)", s)

    print(" ".join(tokens))
    print("Preorder")

    tree, _ = parse(tokens, 0, [0])
    preorder(tree)

    print("Inorder")
    inorder(tree)
