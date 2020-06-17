import click, statistics

class Statistic :
    @click.group()
    def sts():
        pass

    @sts.command("mean")
    @click.argument("angka", default="", type=str)
    def mean(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = statistics.mean(merge)
        print(inp)

    @sts.command("median")
    @click.argument("angka", default="", type=str)
    def median(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = statistics.median(merge)
        print(inp)

    @sts.command("mode")
    @click.argument("angka", default="", type=str)
    def mode(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = statistics.mode(merge)
        print(inp)

    @sts.command("fmean")
    @click.argument("angka", default="", type=str)
    def fmean(angka):
        inp = angka.split(" ")
        merge = []
        for x in inp:
            merge.append(int(x))
        inp = statistics.fmean(merge)
        print(inp)

if __name__ == "__main__":
    Statistic.sts()