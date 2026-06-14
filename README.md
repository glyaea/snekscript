🙏
**HolyPython.**
*Python as God intended.*

## Usage

### Programming

| Notion              | Python              | HolyPython     | Remark                                 |
|---------------------|---------------------|----------------|----------------------------------------|
| Equality checking   | `a == b`            | `a = b`        |                                        |
| Variable assignment | `a = b`             | `a <- b`       |                                        |
| Function definition | `def`               | `function`     |                                        |
| Integer interval    | `[-1, ..., 1]`      | `[-1..1]`      |                                        |
| Integer interval    | `[f(a), ..., g(b)]` | `[f(a)..g(b)]` | `f(a)`, `g(b)` non-decreasing integers |

### Transpilation

| Standard | `uv` |
|-|-|
| `python holypython.py foo.hpy` | `uv run python holypython.py foo.hpy` |

## Testing

| Standard | `uv` |
|-|-|
| `pytest` | `uv run pytest` |
