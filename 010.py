import click

@click.group()
def app():
    pass

@app.command("sum")
def sum():
    total = 0
    while True:
        try:
            number = input("Please enter number: ")
            total += int(number)
        except Exception:
            print("Result : ", total)
            break

if __name__ == "__main__":
    app()