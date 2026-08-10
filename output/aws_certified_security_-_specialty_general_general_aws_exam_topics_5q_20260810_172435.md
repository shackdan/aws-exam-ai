# AWS AWS Certified Security – Specialty Practice Questions

**Generated:** 2026-08-10 17:24:35
**Certification:** AWS Certified Security – Specialty
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

# AWS AWS Certified Security – Specialty Practice Questions

**Generated:** 2026-08-10 17:23:49
**Certification:** AWS Certified Security – Specialty
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 5
**Model:** qwen2.5-coder:7b

---

## Batch 1 (Questions 1-5)

### AWS Certified Security – Specialty Practice Questions

**Question 1:**
**Domain:** Data Protection
**Scenario:** A healthcare organization needs to ensure compliance with HIPAA regulations for storing patient data on AWS. Which of the following would be the most appropriate actions to take?

A) Encrypt data at rest using AWS KMS and enable encryption in transit using SSL/TLS.

B) Use S3 Bucket Policies to restrict access only to authorized users within the organization.

C) Configure VPC Flow Logs to monitor network traffic but not store any sensitive data.

D) Implement an AWS Security Hub with a custom security configuration tailored to HIPAA requirements.

**Correct Answer:** A, B, D

**Explanation:**
- **A)** Encrypts data at rest and in transit, which is crucial for compliance with HIPAA.
- **B)** Limits access to authorized users, ensuring that only those who need it can view the data.
- **D)** Uses AWS Security Hub to ensure that all security configurations are aligned with HIPAA guidelines.

**Why B and C are incorrect:**
- **C)** VPC Flow Logs do not encrypt the data; they just log network traffic. This does not meet the encryption requirements for HIPAA compliance.
- **B)** While restricting access is good practice, it alone does not meet the encryption requirements for HIPAA compliance.

---

**Question 2:**
**Domain:** Incident Response
**Scenario:** A company discovers that a critical application has been compromised and data is being exfiltrated. Which of the following actions should be taken immediately?

A) Immediately terminate all EC2 instances to prevent further damage.

B) Run an automated script to update security groups to restrict access to the compromised instance.

C) Contact AWS Support and provide them with logs and screenshots of the incident for investigation.

D) Use AWS CloudTrail to identify which user made unauthorized changes to the application.

**Correct Answer:** B, C, D

**Explanation:**
- **B)** Restricting access immediately can help prevent further damage.
- **C)** Contacting AWS Support is essential for an official investigation and guidance on how to proceed.
- **D)** AWS CloudTrail provides logs that can help identify the source of the compromise.

**Why A is incorrect:**
- **A)** Terminating all EC2 instances could cause significant disruptions to other applications and services. It should only be done as a last resort.

---

**Question 3:**
**Domain:** Compliance
**Scenario:** A financial services firm needs to ensure that its AWS environment complies with PCI DSS standards for storing credit card data. Which of the following actions is NOT required?

A) Encrypt all data at rest using AWS KMS.

B) Set up an S3 bucket and enable server-side encryption (SSE).

C) Use AWS Key Management Service (KMS) Customer Master Keys (CMKs) to manage encryption keys.

D) Implement AWS Config rules to monitor for compliance with PCI DSS standards.

**Correct Answer:** B

**Explanation:**
- **A)** Encrypting data at rest is required.
- **B)** While setting up an S3 bucket and enabling SSE is good practice, it alone does not meet all PCI DSS requirements. Additional measures such as network segmentation are also necessary.
- **C)** Using AWS KMS CMKs for encryption is required to meet PCI DSS standards.
- **D)** Implementing AWS Config rules helps monitor compliance with various security and compliance standards.

**Why A, C, and D are correct:**
- **A), C, and D)** These actions directly contribute to meeting PCI DSS requirements.

---

**Question 4:**
**Domain:** Security Controls
**Scenario:** An organization needs to implement multi-factor authentication (MFA) for accessing its AWS Management Console. Which of the following methods can be used to achieve this?

A) Configure MFA using a hardware token provided by Google Authenticator.

B) Enable MFA using an SMS-based verification code from an external service.

C) Implement MFA using Amazon Cognito Multi-Factor Authentication (MFA).

D) Set up MFA using an email-based verification code sent to a registered email address.

**Correct Answer:** A, C

**Explanation:**
- **A)** Using Google Authenticator is a valid method for implementing MFA.
- **C)** AWS Cognito provides built-in support for MFA, including hardware tokens and software tokens like Google Authenticator.

**Why B and D are incorrect:**
- **B)** SMS-based verification code from an external service does not meet the requirement of using an authenticator that is directly integrated with AWS services.
- **D)** Email-based verification code is not considered a strong factor in MFA, as it can be intercepted or guessed.

---

**Question 5:**
**Domain:** Data Protection
**Scenario:** A company wants to ensure that data stored on AWS S3 is protected against accidental deletion. Which of the following actions should be taken?

A) Enable versioning for the S3 bucket.

B) Set up lifecycle rules to automatically delete old objects after a certain period.

C) Create an SNS topic and configure it to send notifications when objects are deleted.

D) Implement AWS Key Management Service (KMS) encryption for the S3 objects.

**Correct Answer:** A, C

**Explanation:**
- **A)** Enabling versioning ensures that all versions of an object are retained, preventing accidental deletion.
- **C)** Setting up SNS notifications can help in monitoring and responding to deletions, although it does not prevent them.

**Why B and D are incorrect:**
- **B)** While lifecycle rules are useful for managing storage costs, they do not directly protect against accidental deletion.
- **D)** Implementing KMS encryption is important for protecting data at rest but does not address the issue of accidental deletion.

---

