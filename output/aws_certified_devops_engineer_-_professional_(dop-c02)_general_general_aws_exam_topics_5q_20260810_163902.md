# AWS AWS Certified DevOps Engineer – Professional (DOP-C02) Practice Questions

**Generated:** 2026-08-10 16:39:02
**Certification:** AWS Certified DevOps Engineer – Professional (DOP-C02)
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

# AWS AWS Certified DevOps Engineer – Professional (DOP-C02) Practice Questions

**Generated:** 2026-08-10 16:38:26
**Certification:** AWS Certified DevOps Engineer – Professional (DOP-C02)
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

## Batch 1 (Questions 1-5)

### AWS Certified DevOps Engineer – Professional (DOP-C02) Practice Questions

---

**Question 1:**
You are working on a CI/CD pipeline for a web application. Which two of the following actions can be configured in an AWS CodePipeline to trigger pipeline execution?

A) Creating a new code commit in Amazon S3  
B) Pushing code changes to an Amazon EC2 instance  
C) Detecting changes in the repository's main branch  
D) Starting an EC2 instance using AWS Systems Manager

**Correct Answer:** C, D  

**Explanation:**
- **C) Detecting changes in the repository’s main branch**: This can be done by configuring a webhook or an event in the source provider (like CodeCommit or GitHub) to trigger pipeline execution.
- **D) Starting an EC2 instance using AWS Systems Manager**: AWS Systems Manager Patch Manager can be configured to restart instances, but it doesn't directly trigger pipeline execution.

**Why A and B are incorrect:**
- **A) Creating a new code commit in Amazon S3**: S3 does not have built-in triggers for CodePipeline.
- **B) Pushing code changes to an Amazon EC2 instance**: EC2 does not trigger pipelines; it is used for running applications or services.

---

**Question 2:**
To ensure high availability and failover capabilities, which three of the following AWS services would you deploy your application across?

A) Amazon RDS Multi-AZ  
B) Amazon Route 53  
C) Amazon CloudFront  
D) Amazon DynamoDB Global Table  

**Correct Answer:** A, B, D  

**Explanation:**
- **A) Amazon RDS Multi-AZ**: Provides database replication across multiple Availability Zones.
- **B) Amazon Route 53**: Manages DNS records and provides failover routing policies.
- **D) Amazon DynamoDB Global Table**: Ensures data is replicated across regions for high availability.

**Why C is incorrect:**
- **C) Amazon CloudFront**: Delivers content from edge locations but does not provide failover capabilities. It can be used with Route 53 to optimize delivery and improve reliability.

---

**Question 3:**
Which two of the following AWS services would you use to manage encryption for data at rest?

A) Amazon S3  
B) AWS Secrets Manager  
C) Amazon RDS Multi-AZ  
D) AWS Key Management Service (KMS)

**Correct Answer:** A, D  

**Explanation:**
- **A) Amazon S3**: Provides default and custom server-side encryption using AES-256 or AWS-KMS.
- **D) AWS Key Management Service (KMS)**: Manages encryption keys for data stored in services like S3, RDS, and others.

**Why B and C are incorrect:**
- **B) AWS Secrets Manager**: Stores and manages secrets for applications. It does not handle data at rest encryption.
- **C) Amazon RDS Multi-AZ**: Provides high availability but does not encrypt data at rest.

---

**Question 4:**
To perform a blue/green deployment using AWS services, which two of the following would you configure?

A) Amazon Route 53 with a weighted routing policy  
B) Amazon EC2 instances behind an Application Load Balancer (ALB)  
C) Amazon RDS Multi-AZ setup  
D) AWS Lambda functions  

**Correct Answer:** A, B  

**Explanation:**
- **A) Amazon Route 53 with a weighted routing policy**: Allows you to gradually shift traffic between two environments.
- **B) Amazon EC2 instances behind an Application Load Balancer (ALB)**: Used for load balancing and managing blue/green deployments.

**Why C is incorrect:**
- **C) Amazon RDS Multi-AZ setup**: Provides high availability by replicating the database, but it does not directly support blue/green deployments.

---

**Question 5:**
Which two of the following AWS services would you use to implement a monitoring and alerting system for your application?

A) Amazon CloudWatch  
B) Amazon S3  
C) Amazon Route 53  
D) Amazon DynamoDB  

**Correct Answer:** A, C  

**Explanation:**
- **A) Amazon CloudWatch**: Provides detailed monitoring and observability for AWS resources.
- **C) Amazon Route 53**: Can be used to monitor DNS health checks.

**Why B, D are incorrect:**
- **B) Amazon S3**: Stores objects for long-term archiving or backup. It does not provide monitoring capabilities.
- **D) Amazon DynamoDB**: Manages NoSQL databases and provides query capabilities but does not directly support monitoring.

---

---

