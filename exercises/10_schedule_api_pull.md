# 🧪 Exercise 10: Scheduled Data Pull from API

**Goal:** Schedule a Python script that pulls data from a public API.

**Instructions:**
1. Add `scripts/pull_api_data.py` to Jenkins.
2. Create a Freestyle job.
3. Add you github repo
4. Under **Build Triggers**, enable **Build periodically** and set: `* * * * *`
5. Add a **Build Step**:
   ```bash
   python3 scripts/pull_api_data.py
   ```
6. Confirm the `api_data.json` file is created.
7. Change the **Build periodically** to be executed every hour.
8. Change the **Build periodically** to be executed every 6 hours.

## Reflection:
- What `* * * * *` does it mean? Do you see any change in your builds?
