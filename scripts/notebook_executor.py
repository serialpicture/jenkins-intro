!conda install --yes papermill
import papermill as pm
pm.execute_notebook("analysis.ipynb", "executed.ipynb")
print("Notebook executed.")
