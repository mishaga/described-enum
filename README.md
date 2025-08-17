# described-enum

Python Enums with description property


## Install

With pip:

```bash
pip install described-enum
```

With uv:

```bash
uv add described-enum
```

With poetry:

```bash
poetry add described-enum
```


## Classes

* `DescribedEnum` – child class of `enum.Enum`
* `DescribedIntEnum` – child class of `enum.IntEnum`
* `DescribedStrEnum` – child class of `enum.StrEnum`


## Usage examples

```python
from described_enum import DescribedIntEnum, DescribedStrEnum


class TaskStatus(DescribedIntEnum):
    PENDING = 1, 'Task was created / enqueued'
    RUNNING = 2, 'Working on the task'
    DONE = 3, 'Success'
    FAILED = 4, 'Task failed'


print(TaskStatus.RUNNING.name)  # will print str 'RUNNING'
print(TaskStatus.RUNNING.value)  # will print int 2
print(TaskStatus.RUNNING.description)  # will print str 'Working on the task'


class Format(DescribedStrEnum):
    XML = 'xml', 'Extensible Markup Language'
    JSON = 'json', 'JavaScript Object Notation'
    TOML = 'toml', "Tom's Obvious, Minimal Language"
    YAML = 'yml', "YAML Ain't Markup Language"


print(Format.YAML.name)  # will print str 'YAML'
print(Format.YAML.value)  # will print str 'yml'
print(Format.YAML.description)  # will print str "YAML Ain't Markup Language"
```
