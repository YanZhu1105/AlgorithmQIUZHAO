# Given a non-empty array of integers, return the k most frequent elements. 
# 
#  Example 1: 
# 
#  
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1] 
#  
# 
#  Note: 
# 
#  
#  You may assume k is always valid, 1 ≤ k ≤ number of unique elements. 
#  Your algorithm's time complexity must be better than O(n log n), where n is t
# he array's size. 
#  It's guaranteed that the answer is unique, in other words the set of the top 
# k frequent elements is unique. 
#  You can return the answer in any order. 
#  
#  Related Topics 堆 哈希表 
#  👍 402 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    import heapq
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = collections.defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        heap = []

        for num in set(nums):
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]

    #近乎于作弊
    def topKFrequentCounter(self, nums, k):
        counter = collections.Counter(nums)
        return [x[0] for x in counter.most_common(k)]
# leetcode submit region end(Prohibit modification and deletion)
