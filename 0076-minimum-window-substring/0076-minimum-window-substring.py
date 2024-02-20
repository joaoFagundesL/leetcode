class Solution:
    def minWindow(self, s: str, t: str) -> str:
        string_size, substring_size = len(s), len(t)
        left, right, count = 0, 0, 0
        start, end = 0, string_size - 1
        required_characters = Counter(t)
        window_characters_mapping = {}
        min_window_size, curr_window_size = float('inf'), string_size
        
        while right < string_size:
            right_value = s[right]
            
            # I only need to add the values to the hash if it is a required character.
            # If I want to search for ABC and I run into a D, then no need to insert it into
            # the hash
            if right_value in required_characters:
                
                # Counting how many times I see a value.
                window_characters_mapping[right_value] = window_characters_mapping.get(right_value, 0) + 1
                
                # Ensuring that I wont increase the count variable without need. For example
                # if I have ABC and and in the hash I already have 2 A's then there's no need to increase
                # the count because I only need one A. If  I got more A's than required I must
                # not update the count
                if window_characters_mapping[right_value] <= required_characters[right_value]:
                    count += 1
            
            # At this point I already find a substring, however it may not be the minimum one.
            # Now i'll start reducing the window shifting the left pointer to the right 
            while count == substring_size:
                # before updating the pointer I get the size of the window once it is a valid one containing
                # the substring I have
                curr_window_size = right - left + 1
                
                # Updating the min
                if curr_window_size < min_window_size:
                    min_window_size = curr_window_size
                    # saving the indexes of this window
                    start, end = left, right
                left_value = s[left]
                # Here I verify if the value exists. As I only add the values who are present in the required
                # hash I dont need to verify if it exists in this hash.
                if left_value in window_characters_mapping: 
                    window_characters_mapping[left_value] -= 1
                    
                    # Here it means that when i remove the value from the hash it may happen that 
                    # i no longer satisfy the condition. I might have reduced the window and now there's a lack
                    # of characters that I need to find the substring
                    if window_characters_mapping[left_value] < required_characters[left_value]:
                        count -= 1
                        
                # Just now start moving it
                left += 1
            right += 1
        return "" if min_window_size == float('inf') else s[start : end + 1]
                    
                
            