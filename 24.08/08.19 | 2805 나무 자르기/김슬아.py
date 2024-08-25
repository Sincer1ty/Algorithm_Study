import sys
input=sys.stdin.readline
N,M = map(int,input().split())
trees=list(map(int,input().split()))
trees_max =  max(trees)
def max_cutHeight(tree_max):
    # 절단기 높이 0 에서 시작
    tree_min = 0
    result=0
    # min max 값 역전될 때 while문 빠져나옴
    while tree_min<= tree_max :
        # 중간값 구해 절단
        mid = (tree_min+tree_max)//2
        total=0
        for tree in trees:
            # 중간값 초과하는 높이들만 계산하여 더함
            if tree>mid:
                total+=tree-mid
        if total >= M:
            result=mid
            tree_min=mid+1
        else:
            tree_max = mid-1
    return result
print(max_cutHeight(trees_max))
