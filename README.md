# Fast Api
Check this [Typer Documentation](https://github.com/fastapi/typer).

1 step 

Run following to enable virtual environment (dependencies are installed only for this environment) 

Create .venv directory >> run python -m venv env >> go to env/scripts 
``` 
activate
 ```

Go to repo and install packages  pip install –r requirements.txt 
```
deactivate  -- for disable virtual environment. 
```
2 steps 

1. create main.py file and write the following code
```
def main(name: str):
    print(f"Hello {name}")
```
2. Install typer
```
$ pip install typer
```
Typer includes a typer command/program that you can use to run scripts, automatically converting them to CLIs, even if they don't use Typer internally.

3 step
```
import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
```
4 step

Run this function by typer
```
$ python main.py hello Camila
```
```
$ python main.py goodbye --formal Camila
```

## Typer dependancies

- ``rich``: to show nicely formatted errors automatically.
- ``shellingham``: to automatically detect the current shell when installing completion.
With shellingham you can just use `--install-completion`.
Without shellingham, you have to pass the name of the shell to install completion for, e.g. `--install-completion` bash.

### typer-slim
If you don't want the extra standard optional dependencies, install typer-slim instead.
```
pip install "typer-slim[standard]"
```
The standard extra dependencies are rich and shellingham.

Note: The typer command is only included in the typer package.

# Typer, the FastAPI of CLIs
```
$ pip install "fastapi[standard]"
```
create file main.py with
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```
start server
```
fastapi dev main.py
```

