# AWS SAA-C03 Practice Questions

**Generated:** 2026-08-07 14:06:49
**Domain:** All Domains
**Topic:** Mixed topics across all domains
**Model:** llama3.1:8b

---

---
QUESTION 1:
Domain: [Compute]
Topic: [Load Balancing]

A e-commerce company is planning to launch a new product globally. The architecture team wants to ensure high availability and scalability for their web application. They have decided to use AWS services to achieve this goal. Which service can be used as the load balancer to distribute incoming traffic across multiple instances of the web application?

A. Elastic Load Balancing (ELB)
B. Amazon Route 53
C. Auto Scaling Group (ASG)
D. IAM Identity Center

Correct Answer: A

Explanation:
ELBs include Application and Network Load Balanced to distribute incoming traffic across multiple instances of the web application.

Why other options are incorrect:
- B: Amazon Route 53 is a DNS resolution service, not a load balancer.
- C: Auto Scaling Group (ASG) handles instance scaling but doesn't directly handle traffic distribution.
- D: IAM Identity Center manages identities and access rights across AWS accounts but does not distribute incoming traffic.

AWS Services Covered: [Elastic Load Balancing (ELB), Amazon Route 53, Auto Scaling Group (ASG), IAM Identity Center]
---

---
QUESTION 2:
Domain: [Database]
Topic: [NoSQL Database]

A financial services company needs to process a high volume of transactions per second. The existing database system is experiencing performance issues, leading the team to consider migrating to AWS. Which AWS service would be best suited for this use case?

A. Amazon DynamoDB
B. Amazon Aurora Serverless
C. Amazon Elasticsearch Service
D. Amazon DocumentDB

Correct Answer: A

Explanation:
Amazon DynamoDB is well-suited for handling high-transactional data due to its performance specifications, including high levels of throughput.

Why other options are incorrect:
- B: Amazon Aurora Serverless serves various business needs but not high-throughput transaction handling.
- C: Amazon Elasticsearch Service focuses on text search and query capabilities in a document-based database.
- D: Amazon DocumentDB does not handle massive transactions per second as efficiently as DynamoDB.

AWS Services Covered: [Amazon DynamoDB, Amazon Aurora Serverless, Amazon Elasticsearch Service, Amazon DocumentDB]
---

---
QUESTION 3:
Domain: [Security and Identity]
Topic: [Authentication]

A company has an existing on-premises application relying heavily on Kerberos authentication. They are moving parts of the system to AWS and have a critical requirement to maintain current authentication methods with minimal changes. However, they do not want to require users to log in twice when accessing some applications within the AWS cloud environment.

Which service should the company use to achieve this seamless integration?

A. IAM Identity Center
B. Amazon Cognito
C. Amazon EKS (Elastic Container Service for Kubernetes)
D. AWS_DIRECTORY_SERVICE

Correct Answer: D

Explanation:
AWS Directory Service allows specifying Federation with Active Directory, enabling companies to integrate Kerberos authentication in AWS with minimal disruption.

Why other options are incorrect:
- A: IAM Identity Center manages identities and access rights across AWS accounts but does not integrate with on-premises applications.
- B: Amazon Cognito requires users to have two sessions logged in, which defeats the company's objective of seamless integration.
- C: Amazon EKS is used for containerized workloads, not authentication services.

AWS Services Covered: [IAM Identity Center, Amazon Cognito, Amazon EKS (Elastic Container Service for Kubernetes), AWS_DIRECTORY_SERVICE]
---

---
QUESTION 4:
Domain: [Monitoring and Performance]
Topic: [Real-Time Monitoring]

An e-learning company delivers massive amounts of educational content over the web and has a requirement to monitor the performance of their application in real-time across different metrics, such as latency, error rates, and throughput.

Which AWS service can be used for collecting and reporting on this data?

A. CloudWatch
B. CloudFormation template
C. Inspector (AWS)
D. X-Ray

Correct Answer: A

Explanation:
CloudWatch provides detailed visibility into performance and operations-related metrics of real-time web applications, making it the best fit for the company's needs.

Why other options are incorrect:
- B: CloudFormation template is used to manage and provision AWS resources within a stack.
- C: Inspector serves evaluating vulnerability in instances but doesn't directly address monitoring performance in real time.
- D: X-Ray provides tracing individual requests, which does not align with the requirement for real-time metric collection.

AWS Services Covered: [CloudWatch, CloudFormation template, Inspector (AWS), X-Ray]
---

---
QUESTION 5:
Domain: [Security and Identity]
Topic: [Conditional Access]

A global organization wants to provide access to a protected API to certain users based on their identity. The API is secured via an AWS Managed Active Directory but does not have any specific Identity Provider connected as of now.

Which service will you choose for integrating IAM with the Active Directory to establish trust and enable conditional access control within your application?

A. AWS Identity Store
B. Amazon Cognito
C. AWS SSO (AWS Single Sign-On)
D. AWS WAF

Correct Answer: B is incorrect, Correct Service: C) AWS SSO (AWS Single Sign-On)

Explanation:
To achieve seamless integration between IAM and Active Directory for users accessing a protected API based on their identity, the service chosen should facilitate conditional access within applications using federation.

Why other options are incorrect:
- A: AWS Identity Store hosts an identity store but isn't suited for this use case of enabling conditional access control through IAM.
- B: Amazon Cognito causes issues with two sessions logged in and is not ideal for this requirement as well.
- D: AWS WAF - Web Application Firewall does not integrate IAM directly into Active Directory.

AWS Services Covered: [AWS Identity Store, Amazon Cognito, AWS SSO (AWS Single Sign-On), AWS WAF]
---