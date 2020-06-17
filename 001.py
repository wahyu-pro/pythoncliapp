import click

class StringTransformation:

    @click.group()
    def strTransform():
        """Welcome to MyCliApp"""

    @strTransform.command("lowerCase")
    @click.argument('text')
    def lowerCase(text):
        string  = text
        low = string.lower()
        print(low)

    @strTransform.command("upperCase")
    @click.argument('text')
    def upperCase(text):
        string  = text
        upp = string.upper()
        print(upp)

    @strTransform.command("capitalize")
    @click.argument('text')
    def upperCase(text):
        string  = text
        cap = string.title()
        print(cap)

if __name__ == "__main__":
    StringTransformation.strTransform()