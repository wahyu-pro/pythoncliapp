import click, publicip

@click.group()
def app():
    pass

@app.command("ip-external")
def ip():
    print(publicip.get())

if __name__ == "__main__":
    app()