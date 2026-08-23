class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        half = n // 2

        left_half = num[:half]
        right_half = num[half:]
        
        left_sum = 0
        right_sum =0

        for ch in left_half:
            if ch != '?':
                left_sum += int(ch)

        for ch in right_half:
            if ch != '?':
                right_sum += int(ch)

        left_q = left_half.count('?')
        right_q = right_half.count('?')


        sum_diff = left_sum - right_sum 

        if(left_q + right_q) % 2 == 1:
            return True

        return sum_diff * 2 != 9 * (right_q - left_q)



        
        