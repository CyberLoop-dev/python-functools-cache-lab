from __future__ import annotations

import argparse
from functools import lru_cache


def run_demo(n: int, maxsize: int) -> dict[str, object]:
    @lru_cache(maxsize=maxsize)
    def fibonacci(value: int) -> int:
        if value < 2:
            return value
        return fibonacci(value - 1) + fibonacci(value - 2)

    result = fibonacci(n)
    first = fibonacci.cache_info()
    fibonacci(n)
    second = fibonacci.cache_info()
    fibonacci.cache_clear()
    after_clear = fibonacci.cache_info()

    @lru_cache(maxsize=None, typed=True)
    def kind(value: object) -> str:
        return type(value).__name__

    typed_values = [kind(1), kind(1.0)]
    return {
        "n": n, "fibonacci": result, "after_first_call": first._asdict(),
        "after_repeat": second._asdict(), "after_clear": after_clear._asdict(),
        "typed_keys": {"int_1": typed_values[0], "float_1_0": typed_values[1]},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Explore functools.lru_cache behavior.")
    parser.add_argument("--n", type=int, default=20, help="Fibonacci index (0..35)")
    parser.add_argument("--maxsize", type=int, default=4, help="LRU cache capacity")
    args = parser.parse_args()
    if not 0 <= args.n <= 35:
        parser.error("--n must be between 0 and 35")
    if args.maxsize < 1:
        parser.error("--maxsize must be at least 1")
    result = run_demo(args.n, args.maxsize)
    print(f"fib({result['n']}) = {result['fibonacci']}")
    print("Cache after first calculation:", result["after_first_call"])
    print("After repeating the same call:", result["after_repeat"])
    print("After cache_clear():", result["after_clear"])
    print("typed=True keys:", result["typed_keys"])

if __name__ == "__main__":
    main()
