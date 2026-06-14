
<h3 align="center">
	𓆩 𓂋 𓆪
	<br>
	HolyPython
</h3>

<table>
	<tr>
		<td><img src="images/holypython.png" width="480px"></td>
		<td><img src="images/python.png" width="480px"></td>
	</tr>
</table>

## Syntax

| Python         | HolyPython             | Note                          |
|----------------|------------------------|-------------------------------|
| `a == b`       | `a = b`                |                               |
| `a = b`        | `a <- b`               |                               |
| `[a, ..., b]`  | `[a..b]`               | `a`, `b` non-decreasing `int` |
| `def f(): ...` | `function f() { ... }` |                               |
| `class C: ...` | `class C { ... }`      |                               |

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
