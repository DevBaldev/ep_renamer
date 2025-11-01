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
