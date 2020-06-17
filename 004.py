import click, string

class Palindrome:
    @click.command()
    @click.argument('text', type=str)
    def palindrome(text):
        word = text
        word = "".join(i.lower() for i in word if i in string.ascii_letters)
        rev = word[::-1]

        if (word == rev):
            print("Yes, it is a palindrome")
        else:
            print("No, it is not a palindrome")

if __name__ == "__main__":
    Palindrome.palindrome()