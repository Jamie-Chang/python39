from dataclasses import dataclass
import functools
from typing import Annotated, get_type_hints, get_args, get_origin


@dataclass
class ValueRange:
    range_from: int
    range_to: int

    def check(self, value: int):
        return self.range_from <= value < self.range_to


WheelCachedInt = Annotated[int, ValueRange(-5, 257)]


def _check(value, t) -> bool:
    origin = get_origin(t)  # Annotated
    if origin is None:
        return isinstance(value, t)

    args = get_args(t)  # int, ValueRange(-5, 257)

    if origin is not Annotated:
        raise Exception("Cannot support nested types")

    inner_t, *annos = args
    return _check(value, inner_t) and all(a.check(value) for a in annos)



def type_check(fn):
    type_hints = get_type_hints(fn, include_extras=True)
    @functools.wraps(fn)
    def overriden_fn(value):
        assert _check(value, type_hints["value"])
        fn(value)
    return overriden_fn



@type_check
def some_function(value: WheelCachedInt) -> None:
    print(value)
    ...
