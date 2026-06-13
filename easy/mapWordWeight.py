class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        
        # Process each word in the input list
        for word in words:
            total = 0
            # Calculate the total weight of the word
            for letter in word:
                idx = ord(letter) - ord('a')
                total += weights[idx]
            
            # Reduce the total weight to fit within the 26-letter alphabet bounds
            total = total % 26
            
            # Map the reduced total inversely to a character (0 -> 'z', 1 -> 'y', etc.)
            transformed_char = chr(ord('a') + 26 - total - 1)
            result.append(transformed_char)
            
        # Combine the character results into a single string
        return ''.join(result)