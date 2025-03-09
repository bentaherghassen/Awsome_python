def reverse_string(string):
        """Reverses a string.

       Args:
            string: A string.

        Returns:
            A reversed string.
        """

        reversed_string = ""
        for i in range(len(string) - 1, -1, -1):
            reversed_string += string[i]
        return reversed_string


# Example usage
string = input("Enter a text: ")
reversed_string = reverse_string(string)
print(reversed_string)
