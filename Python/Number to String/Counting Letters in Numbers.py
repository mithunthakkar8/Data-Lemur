def total_letters(N):
    """
    Calculates the total number of letters used when writing out numbers from 1 to N in words,
    without spaces or hyphens.
    
    Parameters:
    N (int): The upper limit of numbers to consider (e.g., 1000 for numbers 1 to 1000).
    
    Returns:
    int: The total count of letters used.
    """
    
    # Mapping of numbers to their word equivalents
    mapping = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
        7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve',
        13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 
        100: 'Hundred',
        1000: 'OneThousand'
    }

    letters = ''  # String to store the concatenated words

    for i in range(1, N + 1):  # Iterate through all numbers from 1 to N

        # Special case for 1000
        if i == 1000:
            letters += mapping[1000]

        # Handle hundreds place (e.g., 300 -> "ThreeHundred")
        if i // 100 > 0 and i != 1000:
            letters += mapping[i // 100]  # Add word for hundred's digit
            letters += mapping[100]  # Add "Hundred"
            
            # If there's a remainder (e.g., 315 -> "ThreeHundredAndFifteen")
            if i % 100 > 0:
                letters += 'and'

        # Handle numbers below 20 directly from mapping
        if i % 100 < 20 and i % 100 > 0:
            letters += mapping[i % 100]

        # Handle numbers 20-99 (e.g., 42 -> "FortyTwo")
        if i % 100 >= 20 and i % 100 <= 99:
            letters += mapping[i % 100 - i % 10]  # Add tens place word (e.g., "Forty")
            
            # Add ones place word if not zero (e.g., "Two" in "FortyTwo")
            if i % 10 > 0:
                letters += mapping[i % 10]

    return len(letters)  # Return total letter count
