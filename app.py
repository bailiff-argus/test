import defstr as ds


def surroundString(s: str) -> str:
    newS = f"SUR({s})ROUND"
    return newS


def printSurround(s: str) -> None:
    print(surroundString(s))


def main() -> None:
    string: str = ds.STRING
    print(f"original: {string}")
    print(f"surrounded: {surroundString(string)}")

if __name__ == "__main__":
    main()
