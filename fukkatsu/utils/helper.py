import ast
import importlib
import inspect
import logging
import re
import subprocess
import sys


def remove_trace_lines(trace_error: str) -> str:
    pattern = r"\b\w*line\s\d+\w*\b"
    output_str = re.sub(pattern, "", trace_error)
    return output_str


def remove_wrapper_name(source_code: str) -> str:
    start_index = source_code.index("def")
    source_code = source_code[start_index:]
    return source_code


def standardize_delimiters(code_block: str) -> str:
    pattern = r"\|*\s*(?:python):?\|*"
    return re.sub(pattern, "|||", code_block)


def extract_text_between_backticks(message: str) -> str:
    message = standardize_delimiters(message)
    start_idx = message.find("|||") + 3
    end_idx = message.rfind("|||")
    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        return ""
    return message[start_idx:end_idx].strip()


def return_source_code(func: callable) -> str:
    source = inspect.getsource(func)
    return source


def return_input_arguments(func: callable, *args, **kwargs) -> dict:
    signature = inspect.signature(func)
    bound_args = signature.bind(*args, **kwargs)
    input_args = {k: bound_args.arguments[k] for k in signature.parameters.keys()}
    return input_args


def extract_imports(code_block: str) -> str:
    """Extract all import statements from a code block."""
    parsed_code = ast.parse(code_block)
    import_statements = []
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Import):
            import_names = [
                f"import {name.name}"
                if name.asname is None
                else f"import {name.name} as {name.asname}"
                for name in node.names
            ]
            import_statements.extend(import_names)
        elif isinstance(node, ast.ImportFrom):
            module_name = (
                node.module if node.level == 0 else "." * node.level + node.module
            )
            import_names = [
                f"from {module_name} import {name.name}"
                if name.asname is None
                else f"from {module_name} import {name.name} as {name.asname}"
                for name in node.names
            ]
            import_statements.extend(import_names)

    import_block = "\n".join(["    " + statement for statement in import_statements])
    return import_block


def insert_string_after_colon(function_string: str, string_to_insert: str) -> str:
    pattern = r"def.*\(.*\).*:"
    match = re.search(pattern, function_string)
    if not match:
        return function_string

    pattern_index = match.end()
    return (
        function_string[:pattern_index]
        + "\n"
        + string_to_insert
        + function_string[pattern_index:]
    )


def check_and_install_libraries(import_statements: str) -> None:
    missing_libraries = []

    for line in import_statements.split("\n"):
        line = line.strip()
        if line.startswith("import"):
            statement = line.split(" ")[1]
        elif line.startswith("from"):
            statement = line.split(" ")[1].split(".")[0]
        else:
            continue

        try:
            importlib.import_module(statement)
        except ImportError:
            missing_libraries.append(statement)

    if missing_libraries:
        logging.warning(f"Missing libraries: {', '.join(missing_libraries)}\n")
        install_libraries(missing_libraries)


def install_libraries(libraries: str) -> None:
    for library in libraries:
        logging.warning(f"Installing library {library}\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

    logging.warning(f"Libraries installed successfully\n")
