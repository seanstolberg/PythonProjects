class Formatter:

    def format_number(number):
        # Convert the number to a string
        number_str = str(number)
        
        # Initialize an empty string to store the formatted result
        formatted_number = ''
        
        # Iterate through the characters of the string in reverse order
        my_list = enumerate(reversed(number_str))
        for i, char in my_list:
            if i > 0 and i % 3 == 0:
                formatted_number = ',' + formatted_number  # Add a comma every three digits
            formatted_number = char + formatted_number
        
        return formatted_number

Formatter.format_number(1000000)