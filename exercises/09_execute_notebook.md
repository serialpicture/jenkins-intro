# 🧪 Exercise 9: Execute a Notebook

**Goal:** Automatically run a Jupyter notebook and log the output.

**Instructions:**
1. Add `scripts/notebook_executor.py` and `analysis.ipynb` (already in the script bash).
2. Create a Freestyle job with:
   ```bash
   cat <<EOF > analysis.ipynb
      {
      "cells": [
      {
         "cell_type": "markdown",
         "metadata": {},
         "source": [
         "# Analyse de base"
         ]
      },
      {
         "cell_type": "code",
         "execution_count": null,
         "metadata": {},
         "outputs": [],
         "source": [
         "print(\"Hello from the notebook!\")"
         ]
      },
      {
         "cell_type": "code",
         "execution_count": null,
         "metadata": {},
         "outputs": [],
         "source": [
         "data = [1, 2, 3, 4, 5]\\n",
         "average = sum(data) / len(data)\\n",
         "print(\"Moyenne:\", average)"
         ]
      }
      ],
      "metadata": {
      "kernelspec": {
         "display_name": "Python 3",
         "language": "python",
         "name": "python3"
      },
      "language_info": {
         "name": "python",
         "version": "3.12"
      }
      },
      "nbformat": 4,
      "nbformat_minor": 5
      }
   EOF

   python3 scripts/notebook_executor.py
   ```
3. Check the console output and verify `executed.ipynb` exists.
