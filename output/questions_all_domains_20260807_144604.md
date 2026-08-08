# AWS SAA-C03 Practice Questions

**Generated:** 2026-08-07 14:46:04
**Domain:** All Domains
**Topic:** Mixed topics across all domains
**Model:** llama3.1:8b

---

---

**Final Exam Questions for SAA-C03**

**Question 1:** 

 DOMAIN: Designing the Compute Environment
TOPIC: Elastic Beanstalk and Auto Scaling

A large e-commerce company wants to build an application using microservices architecture. They need a service that can manage network policies and security groups at scale.

A) Use AWS CloudFormation to create a stack with all necessary network components.
B) Utilize the Network Load Balancer (NLB) to handle high traffic and apply network policies.
C) Implement an Application Load Balancer (ALB) and use Target Groups to manage instances' security.
D) Employ AWS IAM roles to grant permissions for network configuration.

**Correct Answer:** B
**Explanation:** The correct answer is the Network Load Balancer (NLB), which allows fine-grained control of network traffic at scale.

**Distractors Analysis:**
- A) CloudFormation is excellent for provisioning infrastructure, but it's not ideal for managing network policies.
- C) ALB is suited for application-layer load balancing and doesn't support managing instances' security directly.
- D) IAM roles are used to grant permissions at the service level, not specifically for network configuration.

---

**Question 2:** 

DOMAIN: Designing Storage and Data Management
TOPIC: Data Lakes with S3

A video streaming company experiences periodic failures with its static website hosting.

A) The use of AWS S3's Standard-IA storage class will resolve these issues by optimizing performance and reducing costs.
B) Implement an Auto Scaling policy to scale out the EC2 instances hosting the site, handling increased traffic better.
C) Migrate all assets to Amazon CloudFront for faster content delivery across edge locations worldwide.
D) Upgrade the Static Website Hosting bucket's replication configuration within a specific region.

**Correct Answer:** C
**Explanation:** The use of Amazon CloudFront allows the video streaming company to benefit from its extensive network of edge locations, providing faster content delivery and handling increased traffic better.

---

**Question 3:** 

DOMAIN: Designing Storage and Data Management
TOPIC: Database Management with RDS

A business needs a service that will automatically backup their MySQL database, with a disaster recovery strategy using continuous backups and automated snapshots.

A) Use AWS Database Migration Service to regularly transfer the data to an optimized target environment.
B) Establish automatic backing up of the RDS instance with continuous backup enabled.
C) Implement Amazon S3 bucket versioning with lifecycle policies for regular snapshot rotation.
D) Configure a Data Pipeline using Amazon Redshift as the destination and Amazon Kinesis stream as the source.

**Correct Answer:** B
**Explanation:** The correct answer is enabling automatic backups of the RDS instance, ensuring data recoverability.

---

**Question 4:** 

DOMAIN: Securing Applications and Environments
TOPIC: Server-Side Encryption (SSE)

A global financial platform requires high security for sensitive customer and company data. They want to encrypt all AWS S3 bucket objects, both at rest and in transit.

A) Set up Server-Side Encryption (SSE-S3) to manage encryption on the client-side within Amazon S3 buckets.
B) Implement Client-Side Encryption (CSE), with users encrypting files before uploading them for added security.
C) Configure AWS KMS encryption keys within an IAM role granting permissions to use these keys across services.
D) Use Amazon CloudWatch's integration with AWS Organizations for access management.

**Correct Answer:** A
**Explanation:** The correct answer involves selecting Server-Side Encryption (SSE-S3), which encrypts data stored in the bucket on service side without any action required from users, providing comprehensive security for sensitive customer and company information.

---

**Question 5:** 

DOMAIN: Designing Storage and Data Management
TOPIC: S3 Intelligent-Tiering

A media firm needs a cost-effective storage solution that can support their video content in high definition (HD), while also providing automatic transfer of uploaded files to other stores for disaster recovery purposes.

A) Set up Amazon Simple Storage Service (S3) using S3 Intelligent-Tiering, utilizing it with auto-archive and lifecycle policies.
B) Implement Object Lambda Access Points, offering on-fly data transformations which improve the user experience through optimized content delivery.
C) Choose between standard storage options in Amazon Glacier or Tape for long-term storage based on specific regional compliance requirements and performance needs.
D) Utilize Automatic Bucket Policies to apply default settings across buckets with common permissions.

**Correct Answer:** A
**Explanation:** S3 Intelligent-Tiering uses automatic tier changes based on file access frequency, supporting HD content while reducing costs through lifecycle policies for archival transfers.

---

**Question 6:** 

DOMAIN: Designing the Compute Environment
TOPIC: Elastic Beanstalk and Auto Scaling

A developer is planning out new cloud architecture services that will integrate using multiple microservices and third-party libraries. They desire high availability, scalability for handling rapid traffic spikes at no operational extra cost compared to current solutions used previously within the enterprise organization.

A) Apply an Elastic Beanstalk environment, adding Auto Scaling features with its integrated load balancing.
B) Implement a solution by integrating with AWS Lambda functions and an Amazon Cognito-based database system optimized behind a serverless VPC.
C) Use only services supported by FIPS to ensure compliance, configuring AWS Certificate Manager for secure communication and using RDS for DB access in EC2 servers without any automation features necessary from other cloud platforms that aren't on demand resources.
D) Implement Iam Roles with appropriate least privilege permissions that also provide access logs of system actions taken within the infrastructure under management by the DevOps team at this company.

**Correct Answer:** A
**Explanation:** Using Elastic Beanstalk to develop, host, and operate web applications helps simplify service deployments while aligning well with business demands regarding scalability and cost savings.

---

**Question 7:** 

DOMAIN: Designing Security and Compliance
TOPIC: AWS Organizations

A company wants to automate and centralize management of its AWS resources, including permissions, access controls, and cost allocation across multiple departments.

A) Utilize the AWS Organizations service for centralized account management.
B) Centralize control through IAM policies that govern role-based access across all services within different regions.
C) Implement resource tagging using tags in S3 buckets to track related data usage by users across different organization units.
D) Adopt an approach combining serverless computing with EventBridge, targeting real-time analytics and stream processing capabilities for better cost governance.

**Correct Answer:** A
**Explanation:** AWS Organizations enables centralized management of multiple accounts via a master account from which policies and configuration can be applied uniformly across associated workloads under an umbrella.

---

**Question 8:** 

DOMAIN: Designing Storage and Data Management
TOPIC: Data Lakes with S3

An application developer requires the ability to handle large volumes of data being streamed into a database within their AWS services. They chose Amazon Kinesis and then need help figuring out what’s best for storing such processed information efficiently.

A) Migrate all historical data from batch processing to DynamoDB using its global table option optimized at lower tier storage pricing.
B) Stream the raw but unprocessed aggregated events first into an in-memory column type NoSQL solution, RDS before pushing it off with Lambda job for archival needs post data reduction via Kinesis Data Analytics API.
C) Transfer processed and aggregated events to S3 where files can auto-generate CSV at an hourly or even real-time schedule basis depending on user request frequency - after which files become part of automated tiering for cost savings purposes.
D) Deploy the entire workflow including event collection, processing & delivery within a single serverless container via Kinesis Data Flow and AWS Lambda using custom IAM roles.

**Correct Answer:** C
**Explanation:** Storing processed events in S3 enables archived files from being part of lifetime tier for cost-effective discounts via lifecycle features.

---

**Question 9 (Replaced)** 

 DOMAIN: Designing the Compute Environment
TOPIC: Elastic Beanstalk and Auto Scaling

Due to an increased workload, more instances need to be provisioned with a focus on high availability while minimizing cost. They choose Amazon EC2 Spot Instances.

A) Establish alarm conditions that detect sudden increases in server count or unexpected load spikes which can initiate corrective actions.
B) Implement metric filters within each IAM role's policies so as to prevent unauthorized access based on user group membership.
C) Track changes towards desired capacity through customized rate thresholds with a threshold multiplier set higher than normal high use values expected per app in cloud.
D) Create an Auto Scaling Group policy using Spot and on-Demand instance types, scaling dynamically with resource utilization detected.

**Correct Answer:** D
**Explanation:** Using both Spot and On-Demand instance types with auto-scaling helps meet workload needs while saving considerable money.

---

**Question 10 (Replaced)** 

 DOMAIN: Designing Storage and Data Management
TOPIC: AWS S3

An organization requires its existing data lake architecture built upon S3 to remain compliant with GDPR regulations by providing easy deletion process via automatic metadata updates & also being able to perform data retention within time windows depending on customer preferences.

A) Design an automated deletion process with Athena's usage metrics in conjunction S3’s batch processing jobs triggering upon defined triggers & schedule.
B) Implement a new solution focusing entirely on centralizing compliance through Amazon Cloud Directory where policies set within this environment get inherited by objects below the hierarchy automatically once they’re attached - enabling shared visibility among departments including external partners if granted appropriate privileges after configuration completion by designated teams who worked hard ensuring alignment requirements were covered appropriately according proper standards established throughout whole lifecycle from analysis through implementation without compromising integrity any time since there are multiple competing interests needing balance protection while minimizing operational burden whenever possible according their individual priorities regarding current state operations.
C) Integrate AWS Lake Formation with S3, utilizing a data catalog to manage metadata for tracking storage & retention needs across all regions automatically, providing fine-grained access controls that support the separation of duties model while enabling more streamlined auditing capabilities based upon relevant policies put in place previously via configuration management activities performed earlier stage prior launching current iteration where several changes occurred following extensive review analysis discussions held amongst participants involved contributing different perspectives shared within context related topic being addressed here today!
D) Enact multi-region AWS CloudHSM that stores encryption keys & managed securely using AWS Secrets Manager which is connected directly into the source systems like EMR cluster etc via API for accessing sensitive data at rest during query operations – taking advantage advantages multi-factor authentication ensures complete control even access permission revocation after setup allowing removal process easier due better centralized resource control compared legacy environments previously used pre-AWS adoption times requiring constant monitoring maintenance henceforth due reduced overhead thanks simplicity features designed reduce administrative burden introduced automation tasks running smoothly without interruptions.

  **Correct Answer:** C
 **Explanation:** AWS Lake Formation provides a data catalog for managing metadata across regions automatically, making it easy to track changes in the data lake.