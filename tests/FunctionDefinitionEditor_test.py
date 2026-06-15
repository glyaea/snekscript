import holypython
import utils

def test_edit_function():
	source = """
function add(a, b):
	return a + b

result = add(2, 3)
"""
	namespace = utils.run_source(holypython.FunctionDefinitionEditor, source)
	assert namespace["result"] == 5
