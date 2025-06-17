# 🧪 Exercise 1: Hello Jenkins

**Goal:** Create and run your first Freestyle Jenkins job.

## Steps:
1. From Jenkins Dashboard, click **New Item**.
2. Name it `hello-job`, select **Freestyle project**, and click **OK**.
3. In the **Build** section, add a build step:  
   ```bash
   echo "Hello Jenkins!"
   ```
4. Click **Build Now** and observe the output in **Console Output**.

## Reflection:
- What does Jenkins actually execute behind the scenes?
- How could this scale for bigger tasks?
