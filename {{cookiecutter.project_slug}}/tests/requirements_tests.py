import subprocess
from pathlib import Path

project_dir = Path(__file__).parent.parent
{% set type_hints = (cookiecutter.python_version|float) >= 3.5 %}

def test_requirements(){% if type_hints %} -> None{% endif %}:{% if not type_hints %}
    # type: () -> None{% endif %}
    """ requirements.txt must be up to date with Pipfile.lock """
    with (project_dir / 'requirements.txt').open('rb') as f:
        requirements = f.read()

    locked = subprocess.check_output(['pipenv', 'lock', '-r'])

    assert locked == requirements
