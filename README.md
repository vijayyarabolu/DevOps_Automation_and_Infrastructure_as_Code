# DevOps Automation & Infrastructure as Code

![AWS](https://img.shields.io/badge/AWS-CloudFormation-orange) ![CI/CD](https://img.shields.io/badge/CI%2FCD-CodePipeline-blue) ![Security](https://img.shields.io/badge/Security-KMS%20%26%20IAM-red)

## 🚀 Project Overview
This project implements a fully automated **DevOps Platform** using **Infrastructure as Code (IaC)**. It provisions a secure, Multi-AZ VPC, sets up a continuous deployment pipeline using AWS CodePipeline, and enforces security best practices with KMS encryption and IAM least privilege.

**Key Features:**
*   **Infrastructure as Code**: All resources defined in AWS CloudFormation (`vpc.yaml`, `cicd.yaml`, `monitoring.yaml`).
*   **Secure Networking**: Custom VPC with public/private subnets and strict Security Groups.
*   **VPN-Only Access**: (Optional) Configuration to restrict access to Corporate VPN CIDRs only.
*   **Automated CI/CD**: Zero-touch deployment from CodeCommit to Lambda/EC2.
*   **Observability**: Integrated CloudWatch Alarms and SNS notifications for 5xx errors.

## 🏗️ Architecture
1.  **Network**: VPC (`10.0.0.0/16`) spanning 2 Availability Zones.
2.  **Pipeline**: CodeCommit -> CodeBuild (Test/Package) -> CodePipeline -> Deploy.
3.  **Security**: KMS Customer Managed Keys (CMK) for artifact encryption.

## 🛠️ Tech Stack
*   **Cloud**: AWS (VPC, EC2, Lambda, S3, KMS, CloudWatch)
*   **IaC**: AWS CloudFormation
*   **CI/CD**: AWS CodePipeline, CodeBuild
*   **Language**: Python 3.9 (Application Code)

## 📂 Repository Structure
```
├── infrastructure/      # CloudFormation Templates
│   ├── vpc.yaml        # Network & Networking
│   ├── cicd.yaml       # Pipeline Definitions
│   └── monitoring.yaml # Alarms & Dashboards
├── app/                # Application Source Code
├── buildspec.yml       # CI/CD Build Instructions
└── DevOps_Project_Guide.md # Detailed Documentation
```

## 🔒 Security & Compliance
*   **Encryption**: All data at rest encrypted via AWS KMS.
*   **Access Control**: Resources are isolated in private subnets where possible.
*   **Audit**: CloudTrail enabled for all API calls.

## 🚀 Deployment
To deploy this stack:
```bash
aws cloudformation deploy --template-file infrastructure/vpc.yaml --stack-name DevOps-VPC
aws cloudformation deploy --template-file infrastructure/cicd.yaml --stack-name DevOps-Pipeline --capabilities CAPABILITY_NAMED_IAM
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
