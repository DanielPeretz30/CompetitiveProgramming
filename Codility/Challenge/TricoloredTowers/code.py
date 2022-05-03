def solution(T):
   dict = {}
   for i in T:
       op1 = i
       op2 = i[1]+i[0]+i[2]
       op3 = i[0]+i[2]+i[1]
       S = set((op1,op2,op3))
       for item in S:
           if item in dict:
               dict[item] = dict[item]+1
           else:
               dict[item] = 1
   return max(dict.values())
