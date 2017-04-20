class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a      # length of the list to be created
        self.b = b      # the step or difference between consecutive values
        self.length = list()

        for item in range(b, (a*b)+1, b):
            self.append(item)

        self.length = len(self) # returns the number of elements in the array

    #implement the binary search algorithm
    def search(self, c): # c is the value you are to find
        dict_result = {}
        count = 0
        index = None

        first_index = 0
        last_index = self.length - 1
        item_found = False

        middle_index = (first_index+last_index)//2
        middle_item = self[middle_index]

        while first_index <= last_index and item_found:
            if c == middle_item:
                item_found = True
                count += 1
                index = middle_index
                
                dict_result['count'] = count # count is the number of times your function iterated to find the index of the number in question
                dict_result['index'] = index # the index of the number in question
                return dict_result # {'count': count, 'index': index}

            elif middle_item > c:
                count += 1
                last_index = middle_index-1
                # self = self[first_index:middle_index+1]

            elif middle_index < c:
                count += 1
                first_index = middle_index+1
                
        
        # if not item_found: # Item is finally found i.e. item_found == True
            # dict_result['count'] = count # count is the number of times your function iterated to find the index of the number in question
            # dict_result['index'] = index # the index of the number in question
            # return dict_result # {'count': count, 'index': index}
        
        # else:
        #     return self.search(c)

# x = BinarySearch(100, 10)
# print(x)