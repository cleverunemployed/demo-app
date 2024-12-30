class Car():
    def __init__(self, mark: str, model: str, year: int, *args, **kwargs) -> None:
        self.mark = mark
        self.model = model
        self.year = year


def calculate(random_value: int = 0) -> int:
    return random_value**random_value


def main() -> None:
    print("Hello world!")


if __name__ == "__main__":
    main()