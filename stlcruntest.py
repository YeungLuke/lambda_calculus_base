import os

from stlcrun import run


def run_file(path):
    with open(path) as fd:
        run(fd.read())


if __name__ == "__main__":
    for filename in os.listdir("./tests"):
        if filename.endswith(".lc"):
            run_file(os.path.join("./tests", filename))
