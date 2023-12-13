# python-snippets

## Env Setup

- install venv if not installed (ubuntu: `sudo apt install python3.8-venv`)
- create python virtual env(venv)
    - create venv `python3 -m venv ./venv`
    - verify created venv: `dir ./venv`

- Activate venv
  - On Unix or MacOS, run: `source venv/bin/activate`

- To verify the venv is activated:
  - on unix run: `which pip` (output should show path to `<project_path>/venv/bin/pip`)

- Install deps
  - run `pip install -r requirements.txt`
