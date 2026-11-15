class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        alphanumeric = list(string.ascii_letters)
        number = list(string.digits)

        # Remove non alphanumeric characters
        s_with_alpha_char = []
        for i in range(len(list(s))):
            if s[i] in alphanumeric:
                s_with_alpha_char.append(s[i].lower())
            if s[i] in number:
                s_with_alpha_char.append(s[i])
        
        # Two pointer
        i, j = 0, len(s_with_alpha_char)-1
        while i < j:
            if s_with_alpha_char[i] != s_with_alpha_char[j]:
                return False
            i += 1
            j -= 1
        return True
        
        