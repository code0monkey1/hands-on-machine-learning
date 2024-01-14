## Poetry

Poetry is used (among other things) for dependency management, below you will find instructions for starting a new project using Poetry, and how to use an existing Poetry project.

- Install Poetry using pip:
```bash
pip install poetry
```

- Initialize the Poetry project and install dependencies:
```bash
poetry init
```
> Alternatively, the command `poetry new project-name` can be used.

- When cloning an existing Poetry project use the following command to install the dependencies:
```bash
poetry install
```
> The command `poetry install --no-root` should be used if you do not have a sub folder for the project.

- Remove the existing virtual environment (if present) and change the Poetry configuration to use the virtual environment in the project (not global):
```bash
rm -rf .venv && poetry env remove --all && poetry config virtualenvs.in-project true
```

- Display information about the virtual environment:
```bash
poetry env info
```

- List available virtual environments:
```bash
poetry env list
```

- Activate the virtual environment:
```bash
poetry shell
```
> To exit the Poetry shell you can simply use `exit`.

- To add a dependency use the following command:
```bash
poetry add requests
```

- To add a development dependency use the following command:
```bash
poetry add -D mypy
```

- To remove a dependency use the following command:
```bash
poetry remove requests
```
