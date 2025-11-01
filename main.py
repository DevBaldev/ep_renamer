import argparse


def main() -> None:
    print(yazi_bulk_renamer(*args_ep()) if args_ep_check(*args_ep()) else "Try again.")


def args_ep() -> tuple[int, int, str]:
    parser = argparse.ArgumentParser(description="Get start, end or type")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start of ep.")
    parser.add_argument("-e", "--end", type=int, default=10, help="End of ep.")
    parser.add_argument("-t", "--type_ep", type=str, default="mp4", help="Type of eps.")
    args = parser.parse_args()
    return args.start, args.end, args.type_ep.lower()


def args_ep_check(start: int, end: int, type_ep: str) -> bool:
    if not 0 <= start <= end and 0 <= end:
        return False
    if type_ep not in {"mp4", "mkv", "webm"}:
        return False
    return True


def yazi_bulk_renamer(start: int, end: int, type_ep: str) -> str:
    result: str = str()
    checker: set = set()
    for i in range(start, end + 1):
        if i not in checker:
            checker.add(i)
            result += f"{i:02}.{type_ep}\n"
            for j in list(
                ep
                for ep in range(i * 10, (i + 1) * 10)
                if ep in set(range(start, end + 1))
            ):
                if j not in checker:
                    checker.add(j)
                    result += f"{j:02}.{type_ep}\n"
    return result


if __name__ == "__main__":
    main()
