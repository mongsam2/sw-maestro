# https://www.acmicpc.net/problem/1991

n = int(input())
tree = dict()
for _ in range(n):
    node, left, right = input().split()
    tree[node] = [left, right]

'''
전위: node -> left -> right
중위: left -> node -> right
후위: 
'''

def action(tree, current, order):
    if current == ".":
        return ""
    if order == "pre":
        return current + action(tree, tree[current][0], order) + action(tree, tree[current][1], order)
    
    elif order == "in":
        return action(tree, tree[current][0], order) + current + action(tree, tree[current][1], order)
    
    elif order == "post":
        return action(tree, tree[current][0], order) + action(tree, tree[current][1], order) + current

for order in ["pre", "in", "post"]:
    print(action(tree, "A", order))