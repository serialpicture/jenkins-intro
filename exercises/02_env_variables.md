# 🧪 Exercise 2: environment variables

**Goal:** Call env vraibles in a Jenkins job.

## Steps:
1. From Jenkins Dashboard, click **New Item**.
2. Name it `env-variables`, select **Freestyle project**, and click **OK**.
3. In the **Build** section, add a build step:  
   ```bash
   echo "Hello Variables!"
   ```
4. Click **Build Now** and observe the output in **Console Output**.
5. Go back to the **Build** section and try to display the env variables **BUILD_ID** and **BUILD_URL**

## Reflection:
- What kind of info can you get with env variables? 