def greet(name: str = "World") -> str:
    """Return a simple greeting message."""
    return f"Hello, {name}!"


def main() -> None:
    message = greet()
    print(message)


if __name__ == "__main__":
    main()
