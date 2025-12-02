from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "teste.txt", "a") as f:
    dados = f.write("Oie")