import holypython

def test_edit_equality():
	source = holypython.EqualityCheckEditor("if a = b:\n\tpass\n").edit_source()
	assert source == "if a == b:\n\tpass\n"

def test_keep_keyword_argument():
	source = holypython.EqualityCheckEditor("print(\"hi\", end=\"\")").edit_source()
	assert source == "print(\"hi\", end=\"\")"
