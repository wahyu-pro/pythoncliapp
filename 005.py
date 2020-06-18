import click

@click.group()
def obf():
    pass

@obf.command("obfuscate")
@click.argument("text")
def obfuscate(text):
    res = ''.join(map(lambda a: "&#{};".format(ord(a)), text))
    print(res)

if __name__ == "__main__":
    obf()