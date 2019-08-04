class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        if(len(A)>0):
            for i in range(len(A)):
                if(A[i]%2 == 0):
                    even_list.append(A[i])
                else:
                    odd_list.append(A[i])
            result_list = even_list + odd_list
            return result_list
        else:
            return A
        
