
examples: list[list[str]] = [
    [
        """
printf 'Hello, world!'
			""",
        """
printf("Hello, world!");
			"""
    ],
    [
        """
printf 'Hello, world!'
return 0
			""",
        """
printf("Hello, world!");
return 0;
			"""
    ],
    ["""
""",
     """
"""
     ],
]
