# Medium

class Solution:
    def checkSum(self, root):
        total, count = [0], [0]
        curr = root
        def dfs(node, total, count):
            if not node:
                return
            total[0] += node.val
            count[0] += 1
            dfs(node.left, total, count)
            dfs(node.right, total, count)
        dfs(curr, total, count)
        return total[0]//count[0] == root.val
    
    def sumAvgSubtree(self, root, ans):
        if not root:
            return
        # Check sumAverage equal to root.val:
        if self.checkSum(root):
            ans[0] += 1
        # Create SubTree
        self.sumAvgSubtree(root.left, ans)
        self.sumAvgSubtree(root.right, ans)
    
    def averageOfSubtree(self, root) -> int:
        ans = [0]
        self.sumAvgSubtree(root, ans)
        return ans[0]
        