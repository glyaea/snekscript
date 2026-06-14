
<h3 align="center">
	𓆩 𓂋 𓆪
	<br>
	HolyPython
</h3>

| `.hpy`                               |   | `.py`                        |
|--------------------------------------|---|------------------------------|
| ![HolyPython](images/holypython.png) | → | ![Python](images/python.png) |

## Syntax

### Summary

| Python         | HolyPython             | Notes                                  |
|----------------|------------------------|----------------------------------------|
| `a == b`       | `a = b`                |                                        |
| `a = b`        | `a <- b`               |                                        |
| `[a, ..., b]`  | `[a..b]`               | `a`, `b` are `int`, and `a` $\leq$ `b` |
| `def f(): ...` | `function f() { ... }` |                                        |
| `class C: ...` | `class C { ... }`      |                                        |

### Highlighting

**VSCode**

```sh
# Create extension
cd holypython/packages/vscode
npx --yes @vscode/vsce package

# Install extension
code --install-extension holypython-0.0.1.vsix
```

## Transpilation

### HolyPython-to-Python

```sh
cd holypython
python holypython.py foo.hpy
```
