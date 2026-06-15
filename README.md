# 𓆩 H𓂋lyPython 𓆪

## Compilation

```sh
# Compile HolyPython file to Python file
cd holypython
python holypython.py foo.hpy
```

## Syntax

| Idea                | Python   | HolyPython |
|---------------------|----------|------------|
| Equality check      | `a == b` | `a = b`    |
| Variable assignment | `a = b`  | `a <- b`   |
| Function definition | `def`    | `function` |

### Examples

```holypython
class TwoSumII:
	function __init__(self, nums, target):
		self.nums <- nums
		self.target <- target

	function search(self):
		l <- 0
		r <- len(self.nums) - 1
		while l < r:
			current <- self.nums[l] + self.nums[r]
			if current = self.target:
				return [l + 1, r + 1]
			if current < self.target:
				l <- l + 1
			if current > self.target:
				r <- r - 1
```

### Highlighting

**VSCode**

```sh
# Build extension
cd holypython/packages/vscode
npx @vscode/vsce package --out holypython.vsix

# Install extension
code --install-extension holypython.vsix
```
