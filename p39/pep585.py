# import less
tuple[int, str]
list[int]
set[int]
dict[int, list[str]]
frozenset[int]
type[object]
...

assert not isinstance([1, "2", (3,)], list[int])  # TypeError
