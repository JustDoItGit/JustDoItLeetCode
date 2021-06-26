# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 记忆化搜索 数学 动态规划 
#  👍 1712 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b



# leetcode submit region end(Prohibit modification and deletion)

'''
# 字典法
class Solution(object):
    def __init__(self):
        self.dic = {1: 1, 2: 2}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dic[n]

# 动态规划
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]
'''