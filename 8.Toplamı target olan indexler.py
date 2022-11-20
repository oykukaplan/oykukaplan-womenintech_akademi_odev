class Solution:  
    def twoSum(self, nums, target):  
        #tüm değerleri takip etmek için bir dictionary bildirme   
        visited_numbers = dict()  
          
        # tüm dizi üzerinde yineleme
        for index, num in enumerate(nums):  
              
            #çiftini aramak için targetdan numu çıkarmak  
            number_to_be_search = target - num  
              
            #çift bulunursa, her iki sayının indeksini döndürür  
            if number_to_be_search in visited_numbers:  
                return [index, visited_numbers[number_to_be_search]]  
            #aksi takdirde tekrar bakmak için dictionarye ekleriz  
            else:  
                visited_numbers[num] = index  
       
list1 = [2, 7, 11, 15]      
target = 18  
obj = Solution()  
print(obj.twoSum(list1, target))  
