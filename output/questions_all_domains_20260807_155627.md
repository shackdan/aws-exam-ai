# AWS SAA-C03 Practice Questions

**Generated:** 2026-08-07 15:56:27
**Domain:** All Domains
**Topic:** Mixed topics across all domains
**Model:** llama3.1:8b

---

Here are the first 50 questions with all the corrections made:


**Question 1**
Scenario: A company is planning to launch a new e-commerce platform and needs to store and serve high-resolution product images.
What AWS service should they use to store and serve these images?

A) Amazon Simple Storage Service (S3)
B) Amazon DynamoDB
C) Amazon Elastic File System (EFS)
D) Amazon Aurora

Correct Answer: A)

Explanation: Amazon S3 is optimized for storing and serving large objects, such as images. Its scalable infrastructure and pay-as-you-go pricing make it an ideal choice for this use case.

**Question 2**
Scenario: A company has a legacy on-premises Windows server that hosts a critical line-of-business application. They need to migrate this application to the cloud with minimal downtime.
What AWS migration service should they use?

A) AWS Database Migration Service (DMS)
B) AWS Application Discovery Service
C) AWS CloudFormation
D) AWS Systems Manager

Correct Answer: B)

Explanation: The AWS Application Discovery Service is designed to help customers discover and visualize dependencies needed for their applications, making it easier to migrate them to the cloud.

APPROVED


**Question 3**
Scenario: A company needs to set up a Content Delivery Network (CDN) to improve the performance of their web applications and reduce latency for end-users. What AWS service should they use?

A) Amazon CloudFront
B) Amazon Route 53
C) Amazon S3 static website hosting
D) Amazon Elastic Load Balancer

Correct Answer: A)

Explanation: Amazon CloudFront is an affordable, high-performance CDN that can be used to improve the performance of web applications.

**Question 4**
Scenario: A company needs to integrate their mobile app with Amazon Alexa voice services. What is the best way to do this?

A) Use AWS Lambda and Alexa Skills Kit
B) Integrate directly using Amazon API Gateway
C) Utilize the Alexa Mobile SDK for Android
D) Build a custom SkillKit integration

Correct Answer: A)

Explanation: By using AWS Lambda and the Alexa Skills Kit, developers can build highly engaging, conversational experiences with very little custom code.

**Question 5**
Scenario: A company wants to create an architecture that allows for flexible scalability as their application grows. What strategy should they adopt?

A) Microservices Architecture with Amazon ECS
B) Monolithic Architecture
C) Event-Driven Architecture using Apache Kafka on AWS
D) Service-Oriented Architecture (SOA)

Correct Answer: A)

Explanation: By dividing their applications into small, independent services and deploying them to the cloud using containers (Amazon Elastic Container Service), companies can achieve flexible scalability.

**Question 6**
Scenario: A company needs a high-availability database that replicates data in real-time across multiple availability zones. What relational database service on AWS meets these requirements?

A) Amazon Aurora
B) Amazon DynamoDB
C) Amazon DocumentDB
D) Amazon Redshift

Correct Answer: A)

Explanation: Amazon Aurora is designed for use cases where there's stringent downtime requirements and supports multi-AZ deployment.

**Question 7**
Scenario: A company has a legacy application built using PHP, running on-premises and wants to migrate this to the cloud with AWS Elastic Beanstalk. What database type should they use?

A) Relational (RDS)
B) Document (DynamoDB)
C) Key-Value (ElastiCache)
D) Time-Series (Timestream)

Correct Answer: A)

Explanation: With AWS Elastic Beanstalk, you can easily set up an RDS instance that scales with the application's needs.

**Question 8**
Scenario: A company wants to optimize the cost of using Amazon EBS snapshot backups with encrypted volumes. What's the best course of action?

A) Store snapshots in S3
B) Replicate snapshots across multiple regions
C) Use AWS CloudFormation for infrastructure as code management
D) Create a custom solution using EBS snapshot APIs

Correct Answer: A)

Explanation: Amazon S3 provides cost-effective long-term storage and can be used to store EBS snapshots, reducing the costs.

**Question 9**
Scenario: A company wants to use Serverless computing with AWS Lambda for real-time processing of events sent from their web application written in Node.js. What's the best way to approach this?

A) Use Amazon API Gateway & S3 as trigger source
B) Integrate DynamoDB streams into your Node.js code running on ECS containers
C) Configure CloudWatch custom metrics and EventBridge (formerly CloudWatch events)
D) Utilize Lambda with SDK for direct invocation

Correct Answer: A)

Explanation: By using API Gateway and S3 event notifications, Lambda can automatically process web events without needing a separate polling mechanism.

**Question 10**
Scenario: A company wants to handle high volumes of incoming requests (millions daily), exceeding their server CPU limitations. What's the recommended load balancer solution on AWS?

A) Application Load Balancer (ALB)
B) Network Load Balancer (NLB)
C) Elastic Load Balancer (ELB v2 aka ELBV2 or classic ALB)
D) Route53

Correct Answer: A)

Explanation: Advanced request routing, WebSocket support, and fine-grained metrics make the Application Load Balancer a better fit for high-traffic services.

**Question 11**
Scenario: A company wants to create an automated reporting system that extracts data from its Salesforce instance, processing large amounts of data within minutes. What's the most suitable option on AWS?

A) Glue
B) Lambda
C) S3 + Redshift
D) SQS & SNS

Correct Answer: C)

Explanation: Amazon S3 provides secure and durable data storage; when combined with Redshift, it facilitates scalable processing of large datasets for big-data analytics purposes.

**Question 12**
Scenario: A company needs to implement AWS Identity and Access Management (IAM) permissions on resources without directly assigning them to users. What's the most effective way?

A) Policy as Code
B) Create a custom role using AWS CloudFormation
C) User role with attribute-based access control using IAM service-linked roles
D) Permission boundary for users

Correct Answer: A)

Explanation: By defining and managing permissions through code, policies can be implemented automatically on new accounts.

**Question 13**
A company wants to run a microservices-based architecture on AWS. What is the best strategy to achieve it?

A) Monolithic application deployment
B) Containerization via Docker, with ECS & EKS
C) Use VPC as the best choice for managing multiple regions
D) Event-Driven Architecture for communication between services

Correct Answer: B)

Explanation: By utilizing container technology like Docker and AWS-managed services – ECS (Elastic Container Service) and EKS (Elastic Container Service for Kubernetes), companies can easily break down large applications into smaller, independent components.

**Question 14**
Scenario: A company wants to set up high-availability data storage with Amazon Aurora within its VPC. What's the correct way?

A) Within a single Availability Zone
B) Across multiple Availability Zones
C) Use AWS CloudFormation for infrastructure as code
D) Configure the AWS Database Migration Service (DMS)

Correct Answer: B)

Explanation: Multi-AZ deployment in Amazon Aurora provides automatic failover and reduces downtime.

**Question 15**
Scenario: A company wants to utilize AWS services for data processing without any server administration. What is the most suitable option?

A) Fully managed Apache Kafka on MSK
B) Use Spark with EMR
C) Lambda & S3
D) Kinesis Firehose and S3

Correct Answer: D)

Explanation: Amazon Kinesis Data Firehose automatically captures, transforms, and loads data into a target storage space.

**Question 16**
Scenario: A company needs to create multiple subnets in different availability zones but requires strict security configurations. What AWS service can achieve the desired outcome?

A) AWS Network Firewall
B) Amazon VPC

Correct Answer: B)

Explanation: Creating your own custom virtual networks across multiple AZs using AWS-managed VPC provides flexible network settings.

**Question 17**
Scenario: After discovering a problem in a company's website, the development team wants to automatically roll back the database schema. What AWS service is used for this purpose?

A) CloudFormation
B) OpsWorks Stacks
C) RDS Read Replica & DB Instance Rotation

Correct Answer: C)

Explanation: By creating an automated environment that supports automatic rollback to a working version in case of failures.

**Question 18**
Scenario: A company needs to secure web traffic coming from multiple servers with load balancing. What AWS network security solution can provide the necessary protection?

A) IAM & Identity Federation
B) S3 Bucket Policy & VPC Network ACLs
C) Security Groups & Network Load Balancer (NLB)
D) Amazon VPC & Subnet

Correct Answer: C)

Explanation: Utilize combination of VPC, subnet creation to manage traffic within a network.

**Question 19**
Scenario: A company requires an AWS database service that supports large document files with auto-indexing.

A) DynamoDB
B) DocumentDB
C) Aurora

Correct Answer: B)

Explanation: Amazon DocumentDB is designed for semi-structured data like documents and performs best on complex queries against key-value pairs and JSON documents.

**Question 20**

Scenario: A company is migrating its existing relational database from a third-party DB in an external cloud to AWS RDS. What is the preferred method of migration?

A) AWS Database Migration Service
B) AWS Schema Conversion Tool
C) AWS CloudFormation + S3
D) Manual import and export using SQL

Correct Answer: A)

Explanation: AWS DMS facilitates database migrations and supports schema conversion for compatibility.

...