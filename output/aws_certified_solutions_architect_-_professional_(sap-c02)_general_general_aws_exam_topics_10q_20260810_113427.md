# AWS AWS Certified Solutions Architect – Professional (SAP-C02) Practice Questions

**Generated:** 2026-08-10 11:34:27
**Certification:** AWS Certified Solutions Architect – Professional (SAP-C02)
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 10
**Model:** qwen2.5-coder:7b

---

# AWS AWS Certified Solutions Architect – Professional (SAP-C02) Practice Questions

**Generated:** 2026-08-10 11:32:54
**Certification:** AWS Certified Solutions Architect – Professional (SAP-C02)
**Domain:** General
**Topic:** General AWS exam topics
**Total Questions:** 10
**Model:** qwen2.5-coder:7b

---

## Batch 1 (Questions 1-5)

### Batch 1 (Questions 1-5)

**Question 1:**  
**Domain: Designing a Highly Available Architecture**  
You are tasked with designing a highly available web application using Amazon Web Services. The application needs to handle peak traffic and ensure minimal downtime in case of failures. Which two AWS services would you use to achieve this goal?  
A) **Amazon EC2 Auto Scaling Groups**  
B) **AWS Elastic Load Balancer**  
C) **Amazon RDS Multi-AZ Deployment**  
D) **Amazon S3 for static content hosting**  

**Correct Answer:** A and C  
**Explanation:**  
- **A) Amazon EC2 Auto Scaling Groups**: This service automatically scales the number of EC2 instances based on demand, ensuring that the application can handle varying loads efficiently.
- **C) Amazon RDS Multi-AZ Deployment**: This feature provides high availability by replicating your database across multiple Availability Zones, reducing the risk of downtime due to a single point of failure.

**Why B and D are wrong:**  
- **B) AWS Elastic Load Balancer**: While useful for distributing traffic across EC2 instances, it does not provide redundancy or disaster recovery capabilities on its own.
- **D) Amazon S3 for static content hosting**: This service is optimized for serving static files like images, videos, and web pages. It does not handle application logic, peak traffic, or disaster recovery.

---

**Question 2:**  
**Domain: Designing an Efficient Architecture**  
You need to design a web application that requires efficient data retrieval for high performance. Which three AWS services would you use to achieve this goal?  
A) **Amazon S3 for static content**  
B) **Amazon DynamoDB for real-time data access**  
C) **AWS ElastiCache for caching**  
D) **Amazon RDS for relational database management**  

**Correct Answer:** A, B, and C  
**Explanation:**  
- **A) Amazon S3 for static content**: Efficiently stores and serves static files with global reach.
- **B) Amazon DynamoDB for real-time data access**: Provides fast and predictable performance, ideal for handling real-time data.
- **C) AWS ElastiCache for caching**: Improves application performance by reducing database load.

**Why D is wrong:**  
- **D) Amazon RDS for relational database management**: While useful for managing relational databases, it does not provide the same level of efficiency in data retrieval and caching as DynamoDB and ElastiCache combined.

---

**Question 3:**  
**Domain: Designing a Secure Architecture**  
You are designing a secure web application that requires encryption both at rest and in transit. Which two AWS services would you use to achieve this goal?  
A) **AWS KMS for key management**  
B) **Amazon RDS**  
C) **AWS IAM**  
D) **Amazon EC2**  

**Correct Answer:** A and B  
**Explanation:**  
- **A) AWS KMS for key management**: Manages encryption keys securely, enabling encryption at rest.
- **B) Amazon RDS**: Supports encryption at rest through options like Storage Encryption and Transparent Data Encryption (TDE).

**Why C and D are wrong:**  
- **C) AWS IAM**: Provides identity and access management, but does not directly support encryption at rest or in transit.
- **D) Amazon EC2**: Does not provide built-in encryption for data at rest or in transit; this would typically be done using services like EBS Encryption (for instances) and SSL/TLS certificates.

---

**Question 4:**  
**Domain: Designing a Cost-Optimized Architecture**  
You need to design a cost-effective architecture that supports high availability and performance. Which two AWS services would you use to achieve this goal?  
A) **Amazon EC2 On-Demand Instances**  
B) **AWS Auto Scaling Groups**  
C) **Amazon RDS Reserved Instances**  
D) **Amazon S3 for static content hosting**  

**Correct Answer:** B and C  
**Explanation:**  
- **B) AWS Auto Scaling Groups**: Automatically scales the number of EC2 instances based on demand, helping to avoid over-provisioning and saving costs.
- **C) Amazon RDS Reserved Instances**: Provides significant cost savings by committing to a fixed term use of an instance, ensuring high availability without additional charges.

**Why A and D are wrong:**  
- **A) Amazon EC2 On-Demand Instances**: While providing flexibility, it does not automatically scale or provide long-term cost savings.
- **D) Amazon S3 for static content hosting**: Optimizes for storing and serving static files but does not directly support high availability or auto-scaling.

---

**Question 5:**  
**Domain: Designing a Scalable Architecture**  
You are designing a scalable web application that needs to handle increasing loads. Which two AWS services would you use to achieve this goal?  
A) **Amazon EC2 Auto Scaling Groups**  
B) **AWS Lambda**  
C) **Amazon RDS Multi-AZ Deployment**  
D) **Amazon S3 for static content hosting**  

**Correct Answer:** A and C  
**Explanation:**  
- **A) Amazon EC2 Auto Scaling Groups**: Automatically scales the number of EC2 instances based on demand, ensuring that the application can handle varying loads efficiently.
- **C) Amazon RDS Multi-AZ Deployment**: Provides high availability by replicating your database across multiple Availability Zones, reducing the risk of downtime due to a single point of failure.

**Why B and D are wrong:**  
- **B) AWS Lambda**: Ideal for serverless computing and handling small requests, but not for managing large scale-out architectures.
- **D) Amazon S3 for static content hosting**: Optimizes for serving static files like images, videos, and web pages. It does not handle application logic or scale out efficiently.

---

---

## Batch 2 (Questions 6-10)

### Batch 1 (Questions 1-5)

---

**Question 1:**  
**Domain:** Designing a Highly Available Architecture  
You are tasked with designing a highly available web application using Amazon Web Services. The application needs to handle peak traffic and ensure minimal downtime in case of failures. Which two AWS services would you use to achieve this goal?  
A) **Amazon EC2 Auto Scaling Groups**  
B) **AWS Elastic Beanstalk**  
C) **Amazon RDS Multi-AZ Deployment**  
D) **Amazon S3 for static content hosting**  

**Correct Answer: A and C**  
**Explanation:**  
- **A) Amazon EC2 Auto Scaling Groups**: This service automatically adjusts the number of EC2 instances based on demand, ensuring high availability.
- **C) Amazon RDS Multi-AZ Deployment**: This feature replicates your database across multiple Availability Zones, providing redundancy and minimal downtime.

**Why B is incorrect:**  
- **B) AWS Elastic Beanstalk**: While this simplifies deployment and scaling, it does not provide the same level of manual control over redundancy and disaster recovery as EC2 Auto Scaling Groups and RDS Multi-AZ Deployment.

**Why D is incorrect:**  
- **D) Amazon S3 for static content hosting**: This service is used for storing and serving static website content, not for handling dynamic application traffic.

---

**Question 2:**  
**Domain: Designing an Efficient Architecture**  
You need to design a web application that requires efficient data retrieval for high performance. Which three AWS services would you use to achieve this goal?  
A) **Amazon S3 for static content**  
B) **Amazon DynamoDB for real-time data access**  
C) **AWS ElastiCache for caching**  
D) **Amazon RDS for relational database management**  

**Correct Answer: B, C, and D**  
**Explanation:**  
- **B) Amazon DynamoDB**: This NoSQL database service provides fast and predictable performance with fully managed storage and scaling.
- **C) AWS ElastiCache**: This in-memory data store accelerates application performance by caching frequently accessed data.
- **D) Amazon RDS for relational database management**: This managed service allows you to easily set up, operate, and scale a relational database.

**Why A is incorrect:**  
- **A) Amazon S3 for static content hosting**: While useful for serving static assets, it is not suitable for handling dynamic data retrieval required by the application.

---

**Question 3:**  
**Domain: Designing a Secure Architecture**  
You are designing a secure web application that requires encryption both at rest and in transit. Which two AWS services would you use to achieve this goal?  
A) **AWS KMS for key management**  
B) **Amazon RDS**  
C) **AWS IAM**  
D) **Amazon EC2**  

**Correct Answer: A and B**  
**Explanation:**  
- **A) AWS KMS**: This service provides a secure way to encrypt and manage keys for data at rest.
- **B) Amazon RDS**: This managed database service offers encryption at rest through AWS-managed CMKs.

**Why C is incorrect:**  
- **C) AWS IAM**: While essential for access control, it does not handle encryption directly. It manages permissions and roles that users and applications can assume.

**Why D is incorrect:**  
- **D) Amazon EC2**: This service provides instances to run applications but does not inherently encrypt data at rest or in transit without additional configurations (like using EBS volumes with encrypted snapshots).

---

**Question 4:**  
**Domain: Designing a Cost-Optimized Architecture**  
You need to design a cost-effective architecture that supports high availability and performance. Which two AWS services would you use to achieve this goal?  
A) **Amazon EC2 On-Demand Instances**  
B) **AWS Auto Scaling Groups**  
C) **Amazon RDS Reserved Instances**  
D) **Amazon S3 for static content hosting**  

**Correct Answer: B and C**  
**Explanation:**  
- **B) AWS Auto Scaling Groups**: This service allows you to automatically scale out your application based on demand, optimizing resource usage.
- **C) Amazon RDS Reserved Instances**: These provide significant cost savings by committing to a fixed term of use.

**Why A is incorrect:**  
- **A) Amazon EC2 On-Demand Instances**: While useful for running applications, they can be costly if not used efficiently. Auto Scaling Groups are more cost-effective when scaling out.

**Why D is incorrect:**  
- **D) Amazon S3 for static content hosting**: This service is primarily for static assets and does not directly impact the cost of high availability or performance.

---

**Question 5:**  
**Domain: Designing a Scalable Architecture**  
You are designing a scalable web application that needs to handle increasing loads. Which two AWS services would you use to achieve this goal?  
A) **Amazon EC2 Auto Scaling Groups**  
B) **AWS Lambda**  
C) **Amazon RDS Multi-AZ Deployment**  
D) **Amazon S3 for static content hosting**  

**Correct Answer: A and C**  
**Explanation:**  
- **A) Amazon EC2 Auto Scaling Groups**: This service automatically adjusts the number of EC2 instances based on demand, enabling horizontal scaling.
- **C) Amazon RDS Multi-AZ Deployment**: By replicating your database across multiple Availability Zones, this ensures high availability and can handle increased load.

**Why B is incorrect:**  
- **B) AWS Lambda**: While useful for serverless computing and reducing infrastructure costs, it does not directly support horizontal scaling of applications.

**Why D is incorrect:**  
- **D) Amazon S3 for static content hosting**: This service is used for serving static assets and does not inherently impact the scalability of your application.

---

