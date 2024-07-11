import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

def test_render_variable_with_none():
    env = Environment()
    result = render_variable(env, None, {})
    assert result is None

def test_render_variable_with_bool():
    env = Environment()
    result = render_variable(env, True, {})
    assert result is True

def test_render_variable_with_dict():
    env = Environment()
    raw = {"key": "{{ cookiecutter.project_name }}"}
    cookiecutter_dict = {"project_name": "SampleProject"}
    expected = {"key": "SampleProject"}
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected

def test_render_variable_with_list():
    env = Environment()
    raw = ["{{ cookiecutter.project_name }}", "static_value"]
    cookiecutter_dict = {"project_name": "SampleProject"}
    expected = ["SampleProject", "static_value"]
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected

def test_render_variable_with_string():
    env = Environment()
    raw = "{{ cookiecutter.project_name.replace(' ', '_') }}"
    cookiecutter_dict = {"project_name": "Sample Project"}
    expected = "Sample_Project"
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected

def test_render_variable_with_non_string():
    env = Environment()
    raw = 12345
    cookiecutter_dict = {}
    expected = "12345"
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected
