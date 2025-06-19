apt-get install python-jenkins
pip install
import papermill as pm
pm.execute_notebook("analysis.ipynb", "executed.ipynb")
print("Notebook executed.")
