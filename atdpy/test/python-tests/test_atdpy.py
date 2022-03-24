"""
Test suite for all Python code, some of which is generated by atdpy.

Each function starting with 'test_' is executed as a test by pytest.
"""

import manual_sample
import everything as e


def test_sample() -> None:
    a_obj = manual_sample.Root(id="hello", await_=True, items=[[1, 2], [3]])
    a_str = a_obj.to_json_string()

    b_str = '{"id": "hello", "await": true, "items": [[1, 2], [3]]}'
    b_obj = manual_sample.Root.from_json_string(a_str)
    b_str2 = b_obj.to_json_string()

    assert b_str == b_str2  # depends on json formatting (whitespace...)
    assert b_str2 == a_str


def test_sample_missing_field() -> None:
    try:
        manual_sample.Root.from_json_string('{}')
        assert False
    except ValueError:
        pass


def test_sample_wrong_type() -> None:
    try:
        manual_sample.Root.from_json_string('["hello"]')
        assert False
    except ValueError:
        pass


# mypy correctly rejects this.
# TODO: move to its own file and expect mypy to fail.
# def test_require_field() -> None:
#     try:
#         # Should fail because the 'req' field is required.
#         e.RequireField()
#         assert False
#     except ValueError:
#         pass


def test_everything_to_json() -> None:
    a_obj = e.Root(
        id="abc",
        await_=True,
        x___init__=1.5,
        items=[[], [1, 2]],
        extras=[17, 53],
        answer=42,
        aliased=e.Alias([8, 9, 10]),
        point=(3.3, -77.22),
        kinds=[
            e.Kind(e.WOW()),
            e.Kind(e.Thing(99)),
            e.Kind(e.Amaze(["a", "b"])),
            e.Kind(e.Root_())
        ],
        assoc1=[
            (1.1, 1),
            (2.2, 2),
        ],
        assoc2=[
            ("c", 3),
            ("d", 4),
        ],
        assoc3={
            5.5: 5,
            6.6: 6,
        },
        assoc4={
            "g": 7,
            "h": 8,
        },
    )
    a_str = a_obj.to_json_string(indent=2)
    print(a_str)

    # expected output copy-pasted from the output of the failing test
    b_str = \
        """{
  "ID": "abc",
  "await": true,
  "__init__": 1.5,
  "items": [
    [],
    [
      1,
      2
    ]
  ],
  "extras": [
    17,
    53
  ],
  "aliased": [
    8,
    9,
    10
  ],
  "point": [
    3.3,
    -77.22
  ],
  "kinds": [
    "wow",
    [
      "Thing",
      99
    ],
    [
      "!!!",
      [
        "a",
        "b"
      ]
    ],
    "Root"
  ],
  "assoc1": [
    [
      1.1,
      1
    ],
    [
      2.2,
      2
    ]
  ],
  "assoc2": {
    "c": 3,
    "d": 4
  },
  "assoc3": [
    [
      5.5,
      5
    ],
    [
      6.6,
      6
    ]
  ],
  "assoc4": {
    "g": 7,
    "h": 8
  },
  "answer": 42
}"""
    b_obj = e.Root.from_json_string(a_str)
    b_str2 = b_obj.to_json_string(indent=2)

    assert b_str == b_str2  # depends on json formatting (whitespace...)
    assert b_str2 == a_str


def test_kind() -> None:
    x = e.Kind(e.WOW())
    assert x.kind == x.value.kind
    assert x.kind == 'WOW'


def test_pair() -> None:
    try:
        e.Pair.from_json_string('[1,2,3]')
        assert False
    except ValueError as exn:
        print(f"Exception: {exn}")
        assert str(exn) == (
                "incompatible JSON value where type "
                "'array of length 2' was expected: '[1, 2, 3]'"
            )


# print updated json
test_everything_to_json()