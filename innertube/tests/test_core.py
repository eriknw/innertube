from pytest import raises
from innertube import Tube


def test_simple_pipeline():
    tube = Tube(
        "a",
        b=lambda: a + 1,
        c=lambda: a + b,
    )
    assert tube(a=1) == {"a": 1, "b": 2, "c": 3}
    with raises(TypeError):
        tube()
