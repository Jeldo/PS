class Solution:
    def pancakeSort(self, A):
        starting_states = list()

        def flip(arr, i):
            start = 0
            while start < i:
                arr[start], arr[i] = arr[i], arr[start]
                start += 1
                i -= 1

        def find_index_of_max(arr, sub_length):
            index_of_max = 0
            for i in range(0, sub_length):
                if arr[index_of_max] < arr[i]:
                    index_of_max = i
            return index_of_max

        def p_sort(arr, sub_length):
            current_size = sub_length
            while current_size > 1:
                index_of_max = find_index_of_max(arr, current_size)
                if index_of_max != current_size - 1:
                    flip(arr, index_of_max)
                    flip(arr, current_size-1)
                    starting_states.extend([index_of_max+1, current_size])
                current_size -= 1
        p_sort(A, len(A))
        return starting_states


arr = [
    [3, 2, 4, 1],
]
for a in arr:
    s = Solution().pancakeSort(a)
    print(s)
