python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install jupyterlab
pip3 install duckdb graphviz
pip3 install jupyterlab-code-formatter
pip3 install black isort
pip3 install -e /Volumes/GitHub/techminer2 --force-reinstall