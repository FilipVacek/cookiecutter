import pytest
from cookiecutter.generate import is_copy_only_path

def test_is_copy_only_path_true():
    context = {
        'cookiecutter': {
            '_copy_without_render': ['*.txt', 'docs/*']
        }
    }
    assert is_copy_only_path('readme.txt', context) == True
    assert is_copy_only_path('docs/index.html', context) == True

def test_is_copy_only_path_false():
    context = {
        'cookiecutter': {
            '_copy_without_render': ['*.txt', 'docs/*']
        }
    }
    assert is_copy_only_path('main.py', context) == False
    assert is_copy_only_path('src/docs/index.html', context) == False

def test_is_copy_only_path_no_key():
    context = {
        'cookiecutter': {}
    }
    assert is_copy_only_path('readme.txt', context) == False
