# **🙏 HolyPython.** *Python as God intended.*

import io
import itertools
import pathlib
import re
import sys
import token
import tokenize

def get_path():
	arg = sys.argv[1]
	path = pathlib.Path(arg).resolve()
	return path

def get_source(path):
	with tokenize.open(path) as source_file:
		source = source_file.read()
	return source

def get_tokens(source):
	text = io.StringIO(source)
	reader = text.readline
	iterator = tokenize.generate_tokens(reader)
	tokens = list(iterator)
	return tokens

class AssignmentEditor:
	def __init__(self, source):
		self.tokens = get_tokens(source)

	def edit_source(self):
		edited = []
		i = 0
		while i < len(self.tokens):
			t = self.tokens[i]
			if i + 1 < len(self.tokens):
				next_t = self.tokens[i + 1]
				if t.string == "<" and next_t.string == "-" and t.end == next_t.start:
					edited.append(t._replace(string="="))
					i += 2
					continue
			edited.append(t)
			i += 1
		source = tokenize.untokenize(edited)
		return source

class DefEditor:
	def __init__(self, source):
		self.tokens = get_tokens(source)

	def edit_source(self):
		edited = []
		for t in self.tokens:
			if t.type == token.NAME and t.string == "function":
				edited.append(t._replace(string="def"))
				continue
			edited.append(t)
		source = tokenize.untokenize(edited)
		return source

class RangeEditor:
	def __init__(self, source):
		self.source = source
		self.tokens = get_tokens(source)
		self.columns = [match.start() for match in re.finditer(r"(?m)^", self.source)]

	def edit_source(self):
		edited = []
		source_offset = 0
		i = 0
		while i < len(self.tokens):
			t = self.tokens[i]
			if t.string != "[":
				i += 1
				continue
			result = self.find_split(i)
			if result is None:
				i += 1
				continue
			j, split = result
			start_offset = self.get_offset(t.start)
			end_offset = self.get_offset(self.tokens[j].end)
			left_source = self.edit_endpoint_source(t.end, split[0])
			right_source = self.edit_endpoint_source(split[1], self.tokens[j].start)
			edited.append(self.source[source_offset:start_offset])
			edited.append(f"list(range(({left_source}), ({right_source}) + 1))")
			source_offset = end_offset
			i = j + 1
		edited.append(self.source[source_offset:])
		source = "".join(edited)
		return source

	def edit_endpoint_source(self, start, end):
		source = self.source[self.get_offset(start):self.get_offset(end)]
		source = RangeEditor(source).edit_source()
		return source

	def find_split(self, start_index):
		brace_depth = 0
		bracket_depth = 1
		paren_depth = 0
		split = None
		for j in range(start_index + 1, len(self.tokens)):
			t = self.tokens[j]
			if t.string == "[":
				bracket_depth += 1
			elif t.string == "]":
				bracket_depth -= 1
				if bracket_depth == 0:
					if split is None:
						return None
					return j, split
			elif bracket_depth == 1:
				if t.string == "(":
					paren_depth += 1
				elif t.string == ")":
					paren_depth -= 1
				elif t.string == "{":
					brace_depth += 1
				elif t.string == "}":
					brace_depth -= 1
				elif split is None:
					if brace_depth == 0 and paren_depth == 0:
						if j + 1 < len(self.tokens):
							split = self.get_split(t, self.tokens[j + 1])
		return None

	def get_offset(self, position):
		row, column = position
		offset = self.columns[row - 1] + column
		return offset

	def get_split(self, left_token, right_token):
		if left_token.string == ".":
			left_dot = left_token.start
		elif left_token.type == token.NUMBER and left_token.string.endswith("."):
			left_dot = (left_token.end[0], left_token.end[1] - 1)
		else:
			return None
		if right_token.string == ".":
			right_dot = right_token.end
		elif right_token.type == token.NUMBER and right_token.string.startswith("."):
			right_dot = (right_token.start[0], right_token.start[1] + 1)
		else:
			return None
		return left_dot, right_dot

def run_script(source, path):
	sys.path.insert(0, str(path.parent))
	namespace = {
		"__file__": str(path),
		"__name__": "__main__",
		"__package__": None
	}
	exec(compile(source, str(path), "exec"), namespace)

if __name__ == "__main__":
	path = get_path()
	source = get_source(path)
	source = AssignmentEditor(source).edit_source()
	source = RangeEditor(source).edit_source()
	source = DefEditor(source).edit_source()
	run_script(source, path)
