"""
Проверьте, есть ли среди данных N чисел нули.
"""

import sys

print(
    any(
        map(
            lambda n: n == 0,
            map(
                int,
                sys.stdin.readlines()[1:]
            )
        )
    )
)
