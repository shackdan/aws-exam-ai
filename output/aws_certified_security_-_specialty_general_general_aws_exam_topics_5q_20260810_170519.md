# AWS AWS Certified Security – Specialty Practice Questions

**Generated:** 2026-08-10 17:05:19
**Certification:** AWS Certified Security – Specialty
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

# AWS AWS Certified Security – Specialty Practice Questions

**Generated:** 2026-08-10 17:04:31
**Certification:** AWS Certified Security – Specialty
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

## Batch 1 (Questions 1-5)

### AWS Certified Security – Specialty Practice Questions

---

#### Domain: General AWS exam topics

**Question 1:**
You are tasked with securing a web application running on Amazon EC2 instances. Which two of the following would be essential steps to ensure the application is secure?

A) Implementing an Application Load Balancer (ALB) for load balancing and HTTPS termination  
B) Enabling AWS Shield Advanced for DDoS protection  
C) Configuring security groups to restrict access to the EC2 instances  
D) Encrypting data at rest using Amazon EBS encryption

**Correct Answer:** A, C  

**Explanation:**  
- **A) Implementing an ALB**: An ALB can help distribute traffic across multiple EC2 instances and terminate HTTPS, reducing the attack surface.  
- **C) Configuring security groups**: Security groups are essential for restricting access to your EC2 instances based on IP addresses, ports, and protocols.

**Why Each Wrong Answer is Wrong:**  
- **B) Enabling AWS Shield Advanced**: While AWS Shield Advanced can protect against DDoS attacks, it does not directly secure the application itself. It provides DDoS mitigation services.  
- **D) Encrypting data at rest using Amazon EBS encryption**: Encryption at rest is important for securing data but is not a direct measure to secure the web application itself.

---

**Question 2:**
You need to implement network segmentation in your AWS environment to improve security. Which two of the following would be effective strategies?

A) Creating VPCs with private subnets and public subnets  
B) Enabling transit gateways for inter-VPC communication  
C) Configuring route tables to direct traffic between subnets  
D) Implementing NAT instances in each public subnet

**Correct Answer:** A, B  

**Explanation:**  
- **A) Creating VPCs with private subnets and public subnets**: This allows you to segment your network into trusted and untrusted zones, enhancing security.  
- **B) Enabling transit gateways for inter-VPC communication**: Transit gateways enable efficient routing between multiple VPCs without requiring NAT instances.

**Why Each Wrong Answer is Wrong:**  
- **C) Configuring route tables to direct traffic between subnets**: While route tables are essential for directing traffic, they do not provide the segmentation benefits of private and public subnets.  
- **D) Implementing NAT instances in each public subnet**: NAT instances are useful for allowing outbound internet access but do not provide the necessary segmentation.

---

**Question 3:**
You are designing a secure data backup strategy for your AWS environment. Which two of the following would be critical steps to ensure compliance and security?

A) Using Amazon S3 for storing backups  
B) Implementing AWS Key Management Service (KMS) encryption for the backups  
C) Enabling versioning and lifecycle policies on S3 buckets  
D) Performing regular audits and monitoring backup activities

**Correct Answer:** B, C  

**Explanation:**  
- **B) Implementing AWS KMS encryption**: Encrypting backups ensures that even if the data is compromised, it remains unreadable without the correct decryption keys.  
- **C) Enabling versioning and lifecycle policies on S3 buckets**: Versioning allows you to keep multiple versions of a backup, while lifecycle policies help manage storage costs by automatically transitioning or expiring old backups.

**Why Each Wrong Answer is Wrong:**  
- **A) Using Amazon S3 for storing backups**: While S3 is a suitable storage solution for backups, it does not provide encryption out-of-the-box.  
- **D) Performing regular audits and monitoring backup activities**: This is important for compliance and security but does not directly address the technical aspects of securing backups.

---

**Question 4:**
You need to implement a secure incident response plan in your AWS environment. Which two of the following would be essential components of such a plan?

A) Having a dedicated security team available 24/7  
B) Implementing Amazon GuardDuty for threat detection and response  
C) Configuring Amazon CloudTrail to log API calls  
D) Having access to forensic analysis tools

**Correct Answer:** A, B  

**Explanation:**  
- **A) Having a dedicated security team available 24/7**: A dedicated security team ensures that incidents are handled promptly and effectively.  
- **B) Implementing Amazon GuardDuty for threat detection and response**: GuardDuty helps detect and respond to threats by continuously monitoring AWS accounts and services.

**Why Each Wrong Answer is Wrong:**  
- **C) Configuring Amazon CloudTrail to log API calls**: While CloudTrail logs are important for auditing and compliance, they do not directly address incident response.  
- **D) Having access to forensic analysis tools**: Access to forensic analysis tools is useful but does not cover the proactive detection and response aspects of an incident response plan.

---

**Question 5:**
You need to ensure that your AWS environment complies with regulatory requirements for data protection. Which two of the following would be critical measures to take?

A) Implementing AWS Config to monitor and evaluate your resources  
B) Enabling AWS CloudTrail to log API calls  
C) Using AWS Key Management Service (KMS) encryption for sensitive data  
D) Conducting regular penetration testing

**Correct Answer:** C, D  

**Explanation:**  
- **C) Using AWS Key Management Service (KMS) encryption for sensitive data**: Encryption ensures that sensitive data remains secure even if it is compromised.  
- **D) Conducting regular penetration testing**: Penetration testing helps identify vulnerabilities and weaknesses in your environment before they can be exploited.

**Why Each Wrong Answer is Wrong:**  
- **A) Implementing AWS Config to monitor and evaluate your resources**: While AWS Config is useful for compliance monitoring, it does not directly address data protection.  
- **B) Enabling AWS CloudTrail to log API calls**: Logging API calls helps with auditing and compliance but does not address the technical aspects of data protection.

---

These questions are designed to test your understanding of general AWS security practices and principles, as covered in the AWS Certified Security – Specialty exam blueprint.

---

