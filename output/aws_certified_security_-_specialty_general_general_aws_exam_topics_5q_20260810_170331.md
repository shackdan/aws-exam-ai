# AWS AWS Certified Security – Specialty Practice Questions

**Generated:** 2026-08-10 17:03:31
**Certification:** AWS Certified Security – Specialty
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

# AWS AWS Certified Security – Specialty Practice Questions

**Generated:** 2026-08-10 17:02:38
**Certification:** AWS Certified Security – Specialty
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

## Batch 1 (Questions 1-5)

### AWS Certified Security – Specialty Practice Questions

**Question 1:**
You are implementing a new web application and need to ensure that all incoming traffic is filtered based on source IP address. Which two of the following AWS services would you use to achieve this requirement?

A) Configure an AWS WAF web ACL for an Application Load Balancer (ALB).

B) Set up Amazon Route 53 DNS records.

C) Use an AWS Shield Advanced protection plan.

D) Implement a custom security group on the EC2 instances.

**Correct Answer:** A, D

**Explanation:**
- **A) Configure an AWS WAF web ACL for an Application Load Balancer (ALB):** This is correct as AWS WAF provides web application firewall capabilities and can be used to filter incoming traffic based on various criteria.
- **D) Implement a custom security group on the EC2 instances:** This is also correct as security groups are network ACLs that control inbound and outbound traffic for your instances.

Why other answers are incorrect:
- **B) Set up Amazon Route 53 DNS records:** While Route 53 can manage DNS routing, it does not filter incoming traffic based on source IP addresses.
- **C) Use an AWS Shield Advanced protection plan:** Shield Advanced provides DDoS protection and traffic mitigation, but it does not directly filter traffic based on source IP addresses.

---

**Question 2:**
A company wants to ensure that its data is encrypted both at rest and in transit. Which three of the following AWS services would be most appropriate for this requirement?

A) Amazon S3 with Server-Side Encryption (SSE-S3)

B) Amazon RDS with encryption enabled

C) AWS Storage Gateway using KMIP

D) Amazon DynamoDB with on-demand backups

**Correct Answer:** A, B, C

**Explanation:**
- **A) Amazon S3 with Server-Side Encryption (SSE-S3):** This is correct as SSE-S3 automatically encrypts objects at rest.
- **B) Amazon RDS with encryption enabled:** This is also correct as you can enable encryption for data at rest and in transit using AWS KMS.
- **C) AWS Storage Gateway using KMIP:** This is correct as KMIP (Key Management Interoperability Protocol) allows you to manage keys from various key management services, including AWS KMS.

Why other answers are incorrect:
- **D) Amazon DynamoDB with on-demand backups:** On-demand backups do not affect data encryption. DynamoDB has its own encryption features but does not provide direct support for custom encryption.

---

**Question 3:**
A company needs to monitor and alert on any unauthorized access attempts to its AWS resources. Which two of the following AWS services would be most suitable for this requirement?

A) Amazon CloudTrail

B) Amazon GuardDuty

C) AWS Config

D) Amazon Inspector

**Correct Answer:** A, B

**Explanation:**
- **A) Amazon CloudTrail:** This is correct as it records API calls made by users and services, including attempts to access resources.
- **B) Amazon GuardDuty:** This is also correct as it continuously monitors AWS accounts for unusual activity that could indicate malicious or unauthorized behavior.

Why other answers are incorrect:
- **C) AWS Config:** While AWS Config helps you assess whether your AWS resources are configured according to your desired policies, it does not directly monitor access attempts.
- **D) Amazon Inspector:** This is a static application security testing tool and does not provide real-time monitoring or alerts for unauthorized access.

---

**Question 4:**
A company wants to ensure that all outbound traffic from its EC2 instances is filtered based on destination IP addresses. Which two of the following AWS services would be most appropriate for this requirement?

A) Configure an Application Load Balancer (ALB)

B) Set up a custom security group

C) Use an Amazon Route 53 DNS record

D) Implement an outbound rule in a network ACL

**Correct Answer:** B, D

**Explanation:**
- **B) Set up a custom security group:** This is correct as security groups control inbound and outbound traffic for your instances.
- **D) Implement an outbound rule in a network ACL:** This is also correct as network access control lists (ACLs) allow you to control traffic entering or leaving a subnet.

Why other answers are incorrect:
- **A) Configure an Application Load Balancer (ALB):** ALBs are designed for load balancing and do not have direct control over outbound traffic.
- **C) Use an Amazon Route 53 DNS record:** While Route 53 can manage DNS routing, it does not filter outgoing traffic based on destination IP addresses.

---

**Question 5:**
A company wants to ensure compliance with a specific regulatory standard (e.g., GDPR or HIPAA) by automating the validation of its AWS configurations. Which two of the following AWS services would be most suitable for this requirement?

A) Amazon Config

B) AWS Trusted Advisor

C) AWS Security Hub

D) AWS GuardDuty

**Correct Answer:** A, C

**Explanation:**
- **A) Amazon Config:** This is correct as it helps you assess whether your AWS resources are configured according to your desired policies and can be used to validate compliance.
- **C) AWS Security Hub:** This is also correct as it provides a unified view of security configurations across your AWS accounts and automatically identifies potential security issues.

Why other answers are incorrect:
- **B) AWS Trusted Advisor:** While Trusted Advisor provides recommendations for improving the security, performance, and efficiency of your AWS resources, it does not automate the validation process.
- **D) AWS GuardDuty:** This is a threat detection service that continuously monitors accounts and resources for malicious activity but does not directly validate compliance.

---

---

