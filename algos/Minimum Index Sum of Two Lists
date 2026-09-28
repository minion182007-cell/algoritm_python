class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        str1={name:i for i , name in enumerate(list1)}
        best=float('inf')
        list1=[]
        for i,name in enumerate(list2):
            if name in str1:
                total=str1[name]+i
                if total==best:
                    list1.append(name)
                if total<best:
                    best=total
                    list1=[name]
        return list1
        
        
                
        

        
