import click

class Arithmetic:
    @click.group()
    def mtk():
        """Welcome to MyCliApp"""

    @mtk.command("add")
    @click.argument('angka', default="", type=str)
    def add(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = reduce(lambda x,y: x+y, merge)
        print(inp)

    @mtk.command("subtract")
    @click.argument('angka', default="", type=str)
    def subtract(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = reduce(lambda x,y: x-y, merge)
        print(inp)

    @mtk.command("multiply")
    @click.argument('angka', default="", type=str)
    def multiply(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = reduce(lambda x,y: x*y, merge)
        print(inp)

    @mtk.command("divide")
    @click.argument('angka', default="", type=str)
    def divide(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = reduce(lambda x,y: x/y, merge)
        print(inp) 


if __name__ == "__main__":
    Arithmetic.mtk()