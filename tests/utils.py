def run_source(editor, source):
	edited_source = editor(source).edit_source()
	namespace = {}
	exec(compile(edited_source, "<test>", "exec"), namespace)
	return namespace
