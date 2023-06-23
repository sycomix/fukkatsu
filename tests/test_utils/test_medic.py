from unittest.mock import patch

import pytest

from fukkatsu.utils.medic import defibrillate, enhance, stalker, twin


def test_defibrillate_with_mock():
    inputs = "example input"
    faulty_function = "def foo(x): return x + 1"
    error_trace = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    llm = {"primary": "gpt"}
    temperature = {"primary": 0.5}

    expected_corrected_function = "def foo(x):\n    return str(x) + '1'"

    with patch(
        "fukkatsu.utils.medic.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": expected_corrected_function}}]
        }

        corrected_function = defibrillate(
            inputs, faulty_function, error_trace, llm["primary"], temperature["primary"]
        )

        assert corrected_function == expected_corrected_function


def test_enhance_with_mock():
    inputs = "example input"
    target_function = "def foo(x): return x + 1"
    request = "Enahnce the function"
    llm = {"primary": "gpt"}
    temperature = {"primary": 0.5}

    expected_enhanced_function = "def foo(x):\n    return str(x) + '1'"

    with patch(
        "fukkatsu.utils.medic.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": expected_enhanced_function}}]
        }

        corrected_function = enhance(
            inputs, target_function, request, llm["primary"], temperature["primary"]
        )

        assert corrected_function == expected_enhanced_function


def test_twin_with_mock():
    inputs = "example input"
    target_function = "def foo(x): return x + 1"
    llm = {"primary": "gpt"}
    temperature = {"primary": 0.5}

    expected_enhanced_function = "def foo(x):\n    return str(x) + '1'"

    with patch(
        "fukkatsu.utils.medic.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": expected_enhanced_function}}]
        }

        corrected_function = twin(
            inputs, target_function, llm["primary"], temperature["primary"]
        )

        assert corrected_function == expected_enhanced_function


def test_stalker_with_mock_no_additional_rquest():
    inputs = "example input"
    target_function = "def foo(x): return x + 1"
    additonal_request = ""
    llm = {"primary": "gpt"}
    temperature = {"primary": 0.5}

    expected_enhanced_function = "def foo(x):\n    return str(x) + '1'"

    with patch(
        "fukkatsu.utils.medic.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": expected_enhanced_function}}]
        }

        corrected_function = stalker(
            inputs=inputs,
            function=target_function,
            model=llm["primary"],
            temperature=temperature["primary"],
            additional_req=additonal_request,
        )

        assert corrected_function == expected_enhanced_function


def test_stalker_with_mock_additional_rquest():
    inputs = "example input"
    target_function = "def foo(x): return x + 1"
    additonal_request = "Enhance the function"
    llm = {"primary": "gpt"}
    temperature = {"primary": 0.5}

    expected_enhanced_function = "def foo(x):\n    return str(x) + '1'"

    with patch(
        "fukkatsu.utils.medic.openai.ChatCompletion.create"
    ) as mock_completion_create:
        mock_completion_create.return_value = {
            "choices": [{"message": {"content": expected_enhanced_function}}]
        }

        corrected_function = stalker(
            inputs=inputs,
            function=target_function,
            model=llm["primary"],
            temperature=temperature["primary"],
            additional_req=additonal_request,
        )

        assert corrected_function == expected_enhanced_function
