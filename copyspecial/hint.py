import os


if __name__ == "__main__":
    # linux: "prayag/shivam/vakil"
    # windows: "prayag\shivam\vakil"
    x = os.path.abspath("xyz__hello__.txt")
    print(x)

    y = os.path.abspath(os.path.join( < parent-dir > , < filename > ))
    print(y)
    # x = os.path.abspath("foo/x.txt")
    # print(x)
