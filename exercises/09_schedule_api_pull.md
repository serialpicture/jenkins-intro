# 🧪 Exercise 9: Scheduled Data Pull from API

**Goal:** Schedule a Python script that pulls data from a public API.

**Instructions:**
1. Add `scripts/pull_api_data.py` to Jenkins.
2. Create a Freestyle job.
3. Under **Build Triggers**, enable **Build periodically** and set: `H */6 * * *`
4. Add a **Build Step**:
   ```bash
   python3 scripts/pull_api_data.py
   ```
5. Confirm the `api_data.json` file is created.
