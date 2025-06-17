# 🧪 Exercise 5: Git Repository Integration

**Goal:** Pull source code from a Git repository and execute a basic job.

## Steps:
1. Create a new Freestyle or Pipeline job.
2. In **Source Code Management**, select **Git** and add a public repo URL.
3. In the **Build** step:
   ```bash
   ls -l
   cat README.md
   ```

## Reflection:
- What happens if the repo URL is wrong?
- How can credentials be handled securely for private repos?
