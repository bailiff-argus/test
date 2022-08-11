def surroundString(s: str) -> str:
    return f"SUR({s})ROUND"


def main() -> None:
    string: str = "something"
    print(f"original: {string}")
    print(f"surrounded: {surroundString(string)}")

if __name__ == "__main__":
    main()
