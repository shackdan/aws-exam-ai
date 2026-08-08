# Answer Key - AWS SAA-C03 Practice Questions

**Generated:** 2026-08-07 17:42:56
**Domain:** All Domains
**Topic:** Mixed topics across all domains

---

*Review the main question file for full explanations.*

### Batch 1

---
QUESTION 1:
Domain: Application Development
Topic: Serverless Computing

A large e-commerce company wants to build a scalable and secure infrastructure to handle a high volume of web traffic. The company has decided to use Amazon Elastic Beanstalk to deploy its web application, but it also needs a content delivery network (CDN) to distribute static assets across the globe.

A) **Amazon CloudFront**
B) Amazon Route 53
C) Amazon S3
D) Amazon EC2

Correct Answer: A)

Ex Explanation:
Amazon CloudFront is a highly distributed content delivery network that can help distribute static assets across the globe, reducing latency and improving user experience.

Why other options are incorrect:
- B) Amazon Route 53 - This service is primarily used for DNS management, not as a CDN.
- C) Amazon S3 - While S3 can store files, it's not optimized for delivering dynamic content and caching.
- D) Amazon EC2 - This service is a virtual machine instance and doesn't support scaling or SSL/TLS.

AWS Services Covered: 
- Amazon CloudFront
---

---
QUESTION 2:
Domain: Data Management
Topic: Event Processing

A startup needs to process large amounts of real-time data from IoT sensors. The company wants to use an event-driven architecture with Apache Kafka on AWS, but it also needs to store the processed data in a database for analytics purposes.

A) Amazon EMR + Amazon DynamoDB + Amazon S3
B) **Amazon Kinesis Data Firehose + Amazon Redshift + Amazon S3**
C) Apache Kafka on AWS (using EC2 + Flink) + Amazon Aurora + Amazon EBS
D) Amazon CloudWatch + Amazon QuickSight + Amazon DynamoDB

Correct Answer: B)

Explanation:
Kinesis Data Firehose can collect and process the real-time data from IoT sensors, while Redshift can store the processed data in a database for analytics purposes. S3 can be used to store raw logs.

Why other options are incorrect:
- A) While EMR + DynamoDB + S3 is a possible architecture, it doesn't handle data processing or analytics.
- C) Using EC2 with Flink and Aurora may require more management effort than necessary for this scenario.
- D) CloudWatch is a monitoring service and QuickSight is a business intelligence tool, not designed for storing raw logs.

AWS Services Covered: 
- Amazon Kinesis Data Firehose
- Amazon Redshift
- Amazon S3
---

---
QUESTION 3:
Domain: Security and Compliance
Topic: Identity Management

An online course company needs to provide secure authentication and authorization for its users and grant them role-based access to courses, but it also wants to integrate with its existing Active Directory (AD) environment on-premises.

A) **Amazon Cognito**
B) AWS IAM Identity Center
C) AWS Organizations
D) Amazon Redshift

Correct Answer: A)

Explanation:
Amazon Cognito allows the company to provide secure authentication and authorization services directly through its application, while using custom SAML 2.0 applications can integrate with existing AD.

Why other options are incorrect:
- B) While IAM Identity Center supports identity management, it's more suitable for enterprise environments with multiple AWS accounts.
- C) AWS Organizations is an account-level service that manages AWS credentials, not users.
- D) Amazon Redshift is a data warehousing service and has nothing to do with authentication.

AWS Services Covered: 
- Amazon Cognito
---

---
QUESTION 4:
Domain: Development Tools
Topic: Continuous Integration/Continuous Deployment

A DevOps team wants to deploy microservices on AWS using Kubernetes on EKS but also needs to automate code builds for continuous integration.

A) **Amazon CodePipeline**
B) AWS CodeBuild
C) AWS CloudFormation + AWS Elastic Container Service for Kubernetes (EKS)
D) AWS Systems Manager

Correct Answer: A)

Explanation:
Amazon CodePipeline can trigger automated builds, tests, and deployments in multiple services to implement Continuous Integration/Continuous Deployment (CI/CD).

Why other options are incorrect:
- B) While CodeBuild automates code builds, it doesn't provide full CI/CD functionality.
- C) CloudFormation + EKS helps manage infrastructure but doesn't handle code automation.
- D) AWS Systems Manager provides a single location for inventory control and configuration management and isn't intended to automate build processes.

AWS Services Covered: 
- Amazon CodePipeline
---

---
QUESTION 5:
Domain: Data Management
Topic: Analytics

A retail company wants to collect and analyze large amounts of event logs by using Amazon S3 buckets as event hubs. However, it also requires the ability to filter these logs in real-time based on various rules without disrupting existing processing flows.

A) Kinesis Data Firehose
B) **Analytics Runtime**
C) Amazon Kinesis Video Streams + AWS Lake Formation
D) AWS Step Functions

Correct Answer: B)

Explanation:
Analytics Runtime allows real-time analytics against S3 event logs by using custom SQL queries to filter data, eliminating the need for additional processing steps or data replication.

Why other options are incorrect:
- A) While Data Firehose can collect and deliver logs, it's also meant for ELK (Elasticsearch + Logstash - Kibana) based data processing.
- C) Using Video Streams would only make sense if there are video streams to be processed in addition to event logs.
- D) Step Functions manage state-machines and workflows across multiple services but isn't designed to create a real-time analytics pipeline.

AWS Services Covered: 
- Analytics Runtime
---

