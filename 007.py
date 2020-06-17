import click, socket

@click.group()
def app():
    pass

@app.command("ip")
def ip():
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)

if __name__ == "__main__":
    app()