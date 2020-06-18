import click, random, string

class Random:
    @click.group()
    def rand():
        pass

    @rand.command("random")
    @click.option('--length', default=8)
    @click.option('--letter', default=True)
    @click.option('--number', default=True)
    @click.option('--uppercase', is_flag=True)
    @click.option('--lowercase', is_flag=True)
    def random(length, letter, number, uppercase, lowercase):
        if length == ():
            length = 8

        if number == True and letter == True:
            letters = string.ascii_letters + string.digits
        elif number == True and letter == True:
            letters = string.ascii_uppercase + string.digits
        elif letter == False:
            letters = string.digits
        else:
            letters = string.ascii_letters
        result = ''.join(random.choice(letters) for i in range(length))
        if uppercase:
            print(result.upper())
        elif lowercase:
            print(result.lower())
        else:
            print(result)


if __name__ == "__main__":
    Random.rand()