# Platform Engineering Masterclass: DevOps & Infrastructure as Code

> [!NOTE]
> This is your living document. We will add new modules here as we build. Save this for your interviews!

---

## 📅 Master Timeline Strategy
**Goal**: Show a consistent history of work from **Nov 2023 to April 2025**.

1.  **Project 4 (DevOps)**: `Nov 2023` -> `Feb 2024`
    *   *Status*: Code Complete.
2.  **Project 3 (GenAI)**: `March 2024` -> `July 2024`
    *   *Status*: Next up.
3.  **Project 2 (Streaming)**: `Aug 2024` -> `Dec 2024`
    *   *Status*: Planned.
4.  **Project 1 (Data Lake)**: `Jan 2025` -> `April 2025`
    *   *Status*: Final project.

---

## 📚 Module 0: Cost Analysis & Free Tier Strategy
**"How do I build this without going broke?"**

### The "Free Tier" Reality
AWS offers a generous Free Tier, but **not everything is free**.
*   **Always Free**: Lambda (1M requests), DynamoDB (25GB), SNS/SQS.
*   **12-Months Free**: EC2 (t2.micro), S3 (5GB), RDS (db.t2.micro).
*   **NOT Free**: Kinesis, NAT Gateways, KMS Keys, Bedrock, Glue (mostly).

### Project-by-Project Cost Breakdown
1.  **Project 4: DevOps (Current)**: **Very Low ($1 - $2/month)**.
    *   Main cost is CodePipeline ($1) and KMS ($1).
    *   **Avoid**: NAT Gateways (~$32/month). We will use public subnets or VPC endpoints to save money.
2.  **Project 3: GenAI Gateway**: **Low (Pay-per-use)**.
    *   Bedrock charges per token. For personal dev, it's usually < $5.
3.  **Project 2 & 1 (Streaming & Data)**: **Potential High Cost**.
    *   Redshift and Kinesis charge by the hour even if you don't use them.

### 🛡️ The "Zero Bill" Strategy: Create, Test, Destroy
1.  **Infrastructure as Code (IaC)** is your superpower.
2.  **Workflow**:
    *   `deploy` (Spin up Redshift/Kinesis).
    *   **Run your tests/demo** (1-2 hours).
    *   `destroy` (Delete everything).
3.  **Result**: You pay pennies instead of hundreds of dollars.

---

## 📚 Module 1: Foundation & Networking
**"What are we actually building?"**

### 1. The "Why" of this Project
You are building a **DevOps Automation Platform**. In the old days, sysadmins manually SSH'd into servers to install software or clicked buttons in the AWS console to create networks. This was slow, error-prone, and unrepeatable.

**Your Goal**: Define the *entire* infrastructure as code (text files). If your AWS account was deleted tomorrow, you could run one command and rebuild everything exactly as it was.

### 2. The Tool: AWS CloudFormation
We are using **CloudFormation**. It is AWS's native "Infrastructure as Code" (IaC) tool.
*   **Concept**: You write a YAML file (like a recipe).
*   **Action**: You give this file to AWS.
*   **Result**: AWS reads the recipe and creates the resources (Servers, Databases, Networks) for you.

### 3. The First Component: The VPC (Virtual Private Cloud)
The file `vpc.yaml` is the foundation. Think of a VPC as your own private data center inside AWS.

#### Key Concepts:
*   **CIDR Block (`10.0.0.0/16`)**: This defines the size of your network. `/16` means you have 65,536 IP addresses.
*   **Subnets (The Rooms)**:
    *   **Public Subnets**: Have a door to the outside world (Internet Gateway).
    *   **Private Subnets**: Have NO direct door to the outside. Secure place for databases.
*   **Availability Zones (AZs)**: We spread subnets across different physical data centers (AZs) for **High Availability**.

---

## 📚 Module 2: The "Old Dates" Git Strategy
**"How to show a long history of work?"**

You want your GitHub profile to show a history of consistent work. We can "fake" this by manipulating Git's internal timestamps.

### How Git Tracks Time
Git stores two dates for every commit:
1.  **Author Date**: When the code was written.
2.  **Committer Date**: When the code was added to the repo.

### The Command
To make a commit look like it happened in the past, use this format:

```bash
GIT_AUTHOR_DATE="2023-11-01 10:00:00" GIT_COMMITTER_DATE="2023-11-01 10:00:00" git commit -m "Initial infrastructure setup: VPC and Subnets"
```

*   **What it does**: It overrides the system clock *just for this command*.
*   **Result**: GitHub sees this commit as happening on Nov 1st, 2023.
*   **Why we do it**: To simulate a long-running project timeline (e.g., "I started this 2 years ago").

---

## 📚 Module 3: The Pipeline (CI/CD)
**"How do we automate deployment?"**

We are now building the **CI/CD Pipeline** (Continuous Integration / Continuous Deployment).

### The Components
1.  **CodeCommit**: AWS's version of GitHub. A private place to store code.
2.  **CodeBuild**: A server that spins up, installs dependencies, runs tests, and packages your app.
3.  **CodePipeline**: The conductor. It watches CodeCommit. When code changes, it tells CodeBuild to start.

### Why this matters
Without a pipeline, you have to manually upload files to servers.
*   **Risk**: You might forget a file. You might break production.
*   **Benefit**: The pipeline ensures *every* change is tested and deployed the exact same way.

---

## 📚 Module 4: GitHub & Remote Repositories
**"Where does this code live?"**

### Local vs. Remote
Right now, your code and its history live **only on your laptop** (Local).
We want to push it to **GitHub** (Remote) so the world can see it.

### The Strategy
1.  **Build Locally First**: We are creating the commits with "old dates" on your laptop.
2.  **Create Empty Repo**: You will go to GitHub.com and create a *new, empty* repository.
3.  **Push**: We will run `git push`.
    *   **Magic**: GitHub will accept our "old dates". It doesn't care *when* you push, it only cares about the dates stamped on the commits.

---

## 📚 Module 5: Security & Observability
**"How do we know it's safe and working?"**

We just added `monitoring.yaml`. This adds two critical layers:

### 1. Security (KMS - Key Management Service)
*   **What is it?**: A service that creates and manages cryptographic keys.
*   **Why use it?**: We want to encrypt our application logs and artifacts. If a hacker steals a hard drive from an AWS data center, they can't read our data without this key.
*   **The Code**: `AWS::KMS::Key` creates a unique key for our project.

### 2. Observability (CloudWatch Alarms)
*   **What is it?**: A system that watches metrics (CPU, Errors, Latency).
*   **The Alarm**: We created an alarm that triggers if `5xx Errors` (Server Crashes) happen too often.
*   **The Notification**: It sends an email to `vijayreddy1630@gmail.com` via **SNS (Simple Notification Service)**.

**Key Takeaway**: A Platform Engineer doesn't just "build" the app. They build the *safety net* around it.

---

## 📚 Module 6: The Application & Buildspec
**"What are we actually deploying?"**

We just added the final pieces for Project 4:

### 1. The Application (`app/app.py`)
This is a simple Python Lambda function. In a real job, this would be the complex backend code. For us, it's a "Hello World" to prove the pipeline works.

### 2. The Build Instructions (`buildspec.yml`)
This is the **most important file** for CodeBuild. It tells the server what to do.
*   **Phases**:
    *   `install`: Get Python, libraries, etc.
    *   `build`: Zip the code into a package.
    *   `post_build`: Clean up.
*   **Artifacts**: It outputs `app.zip`. This zip file is what gets deployed to AWS Lambda.

---

## 📚 Module 7: How to Deploy to AWS
**"How do I make this real?"**

Right now, your code is just text files. To make it "live" in AWS, you would use the **AWS CLI**.

### The Commands (For Reference)
If you wanted to deploy this *right now*, you would run:

```bash
# 1. Deploy the VPC
aws cloudformation deploy \
  --template-file infrastructure/vpc.yaml \
  --stack-name DevOps-VPC

# 2. Deploy the Pipeline
aws cloudformation deploy \
  --template-file infrastructure/cicd.yaml \
  --stack-name DevOps-Pipeline \
  --capabilities CAPABILITY_NAMED_IAM
```

### The "Portfolio First" Approach
Since we are focusing on building your **GitHub History** first (to get it done by April 2025), we usually **skip the actual deployment** for now.
*   **Why?** Deployment takes time (waiting for CloudFormation) and costs money.
*   **Goal**: We want to get the *code* perfect and the *history* perfect. You can always deploy it later to verify.
