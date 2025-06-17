# 🧪 Exercise 3: Simulate and Fix a Job Failure

**Goal:** Understand how Jenkins handles errors and how to debug failed jobs.

## Steps:
1. Duplicate your `hello-job` and name it `failing-job`.
2. Modify the shell step:
   ```bash
   echo "Simulating failure..."
   exit 1
   ```
3. Run it and observe the **Console Output**.

## Reflection:
- How is failure indicated?
- What logs or info help identify the problem?
