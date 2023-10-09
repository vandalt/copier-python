# Copied from: https://github.com/dfm/copier-simple-python
from helpers import generate_project
from plumbum import local


def test_pre_commit():
    with generate_project():
        local["pre-commit"]("run", "--all-files")
