class Sorting(object):
    # Quick Sort
    def quickSort(self, nums, begin, end):
        if begin >= end: return
        pivot_index = self.partition(nums, begin, end)
        self.quickSort(nums, begin, pivot_index - 1)
        self.quickSort(nums, pivot_index + 1, end)

    def partition(self, nums, begin, end):
        pivot = nums[begin]
        mark = begin
        for i in range(begin + 1, end + 1):
            if nums[i] < pivot:
                mark += 1
                nums[i], nums[mark] = nums[mark], nums[i]
        nums[mark], nums[begin] = nums[begin], nums[mark]
        return mark

    # Merge Sort
    def mergeSort(self, nums, left, right):
        if left >= right: return
        mid = (left + right) >> 1
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        i, j, temp = left, mid + 1, []
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= right:
            temp.append(nums[j])
            j += 1
        nums[left: right+1] = temp

    # Heap Sort
    def heapSort(self, nums):
        for i in range((len(nums)-2)//2, -1, -1):
            self.heapify(i, len(nums), nums)
        for j in range(len(nums)-1, 0, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.heapify(0, j, nums)

    def heapify(self, parent_index, length, nums):
        temp, child_index = nums[parent_index], 2 * parent_index + 1
        while child_index < length:
            if child_index + 1 < length and nums[child_index + 1] > nums[child_index]:
                child_index += 1
            if temp > nums[child_index]: break
            nums[parent_index], parent_index = nums[child_index], child_index
            child_index = 2 * parent_index + 1
        nums[parent_index] = temp

S = Sorting()
S.heapSort(nums = [4,1,3,5,8,4])
