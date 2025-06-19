python -m venv venv
. venv/bin/activate
import papermill as pm
pm.execute_notebook("analysis.ipynb", "executed.ipynb")
print("Notebook executed.")
