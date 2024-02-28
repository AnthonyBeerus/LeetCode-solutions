from collections import deque

def palindrome(x):
    # Check if the number is negative, as negative numbers cannot be palindromes
    if x < 0:
        return False

    # Convert the input number to a string to access individual digits
    string_of_x = str(x)
    
    # Create an array of digits by converting each character in the string to an integer
    digits_array = [int(char) for char in string_of_x]

    # Create a deque (double-ended queue) to efficiently pop from both ends
    digits_queue = deque(digits_array)

    # Loop for comparing digits from both ends of the deque
    while len(digits_queue) > 1:
        # Pop the leftmost digit
        first_num = digits_queue.popleft()
        # Pop the rightmost digit
        last_num = digits_queue.pop()

        # Compare the first_num and last_num digits
        if first_num != last_num:
            # If digits are not equal, the number is not a palindrome
            return False

    # If the loop completes without returning, the number is a palindrome
    return True
