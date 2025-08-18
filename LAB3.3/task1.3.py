import sys
from typing import Optional


def compute_factorial(n: int) -> int:

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def parse_int(value: str) -> int:
    try:
        return int(value)
    except ValueError as error:
        raise ValueError(f"Invalid integer: {value}") from error


def main(argv: Optional[list[str]] = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)

    try:
        if argv:
            n = parse_int(argv[0])
        else:
            raw = input("Enter a non-negative integer: ")
            n = parse_int(raw)

        result = compute_factorial(n)
        print(f"{n}! = {result}")
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


