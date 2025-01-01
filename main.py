class Car():
    def __init__(self, mark: str, model: str, year: int, *args, **kwargs) -> None:
        self.mark = mark
        self.model = model
        self.year = year
        self.amount_kilometres = 10000

    def to_track(self, kilometres: int) -> bool:
        if self.amount_kilometres <= 0:
            return False
        
        self.amount_kilometres -= kilometres

        return True

    def to_repair(self, percent_repair: int) -> None:
        self.amount_kilometres += 10000*percent_repair//100

def calculate(random_value: int = 0) -> int:
    return random_value**random_value


def main() -> None:
    print("Hello world!")


if __name__ == "__main__":
    main()