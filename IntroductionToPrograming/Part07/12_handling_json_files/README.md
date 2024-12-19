
# handling JSON files

Let's have a look at a JSON file, which contains some information about students in the following format:

```json
[
    {
        "name": "Peter Pythons",
        "age": 27,
        "hobbies": [
            "coding",
            "knitting"
        ]
    },
    {
        "name": "Jean Javanese",
        "age": 24,
        "hobbies": [
            "coding",
            "rock climbing",
            "reading"
        ]
    }
]
```

Please write a function named print_persons(filename: str), which reads a JSON file in the above format, and prints the contents as shown below. The file may contain any number of entries.

```markdown
Peter Pythons 27 years (coding, knitting)
Jean Javanese 24 years (coding, rock climbing, reading)
```

The hobbies should be listed in the same order as they appear in the JSON file.
