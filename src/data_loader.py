from pathlib import Path


# Loads all csv file directories 
def load_all_csv():
    base = Path(__file__).resolve().parent.parent / "data" / "titanic"
    dfs = {}
    for file in base.glob("*.csv"):
        key = file.stem
        dfs[key] = file.resolve()
        print(f"{file} directory is loaded as: {key}")
    return dfs
