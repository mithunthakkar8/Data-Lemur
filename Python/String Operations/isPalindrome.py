def isPalindrome(phrase):
    # Convert the phrase to lowercase and filter only alphanumeric characters
    cleaned_phrase = ''.join(i for i in phrase.lower() if i.isalnum())  # O(n) time, O(n) space
    
    # Check if the cleaned phrase is the same as its reverse
    return cleaned_phrase == cleaned_phrase[::-1]  # O(n) time, O(n) space
