# Copied from: https://github.com/dfm/copier-simple-python
import warnings
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

from copier import run_copy
from copier.errors import DirtyLocalWarning
from plumbum import local

# Plumbum enables access to git shell comand as a function
git = local["git"]


@contextmanager
def generate_project(**data):
    data["project_name"] = data.get("project_name", "example_project")
    with TemporaryDirectory() as project:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DirtyLocalWarning)
            run_copy(".", project, data=data, defaults=True, vcs_ref="HEAD")
        with local.cwd(project):
            git("init", ".")
            git("add", ".")
            git(
                "commit",
                "--mesage=test",
                "--author=Test<test@test>",
                "--no-verify",
            )
            git("tag", "0.1.0")
            yield Path(project)
