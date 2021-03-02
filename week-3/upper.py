class String_print():
    
    def get_String(self):
        self.str = input()

    def print_String(self):
        print(self.str.upper())

str1 = String_print()
str1.get_String()
str1.print_String()