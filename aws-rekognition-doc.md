# AWS Serverless Image Analysis Pipeline

A fully automated serverless pipeline that analyzes uploaded images using AWS Rekognition and stores the results in DynamoDB for easy retrieval.

---

## The Challenge
Ever tried organizing thousands of photos on your phone? You know the struggle.  
You've got pictures of your dog, your coffee, random screenshots, and vacation photos all mixed together. Finding anything takes forever.

Now imagine you're a business that gets hundreds of images uploaded daily - product photos, user content, documents. Someone has to manually look at each one and figure out what's inside.

That's exactly what I wanted to solve:
- **Stop the manual work** - No more humans staring at images all day
- **Get instant answers** - What's actually in this image?
- **Make it searchable** - Find all images with "cars" or "people" in seconds
- **Never worry about scale** - Whether it's 10 images or 10,000, it should just work
 
---

## My Steps

**1. Setting Up the Storage Layer**  
I created an S3 bucket to store incoming images and a DynamoDB table to hold analysis results.
- S3 handles the image storage and triggers
- DynamoDB stores structured analysis data with `ImageName` as the primary key

![S3 Bucket Creation](images/s3-creation.png)

---

**2. Building the Lambda Function**  
The core logic lives in a Python Lambda function that:
- **Listens** for S3 upload events
- **Calls** Amazon Rekognition to analyze the image  
- **Stores** the detected labels and confidence scores in DynamoDB

![Lambda Function](images/lambda-function-success.png)  
[View full Lambda code](rekognition_lambda.py)

---

**3. Configuring the Event Trigger**  
I set up S3 to automatically trigger the Lambda function whenever a new image gets uploaded.

![Lambda Trigger Setup](images/lambda-trigger.png)

---

**4. Setting Up IAM Permissions**  
The Lambda function needs specific permissions to:
- **Read** from the S3 bucket
- **Analyze** images with Rekognition  
- **Write** results to DynamoDB
For this project I added permissions for full access DynampDB, Rekognition and read on;y permissions for S3

![Permission Policy](images/permission-policy-lambda.png)

---

**5. Testing the Pipeline**  
When I upload an image:
- The trigger fires automatically
- Rekognition detects objects like "Person", "Car", "Building"
- Results get stored in DynamoDB with confidence scores

![Analysis Results](images/result.png)

---
**Tech Stack:**
- **AWS Lambda** (Python 3.12) - Serverless compute
- **Amazon S3** - Image storage and event source
- **Amazon Rekognition** - AI image analysis
- **Amazon DynamoDB** - NoSQL database for results

---

## Performance Optimizations

**Current Setup:**
- Lambda timeout: 30 seconds (sufficient for most images)
- Max labels per image: 10 (configurable)

**Possible Architecture Improvements:**
- Separate Lambda function for DynamoDB writes to improve speed
- Add image resizing for faster processing
- Implement batch processing for multiple images

---

## What I Learned
- How to build **event-driven serverless architectures** on AWS
- How to use **Amazon Rekognition** for automatic image analysis
- Why **proper IAM permissions** are crucial for Lambda functions
- That **serverless scaling** happens automatically without configuration

---

**Personal Links:**
[LinkedIn](https://www.linkedin.com/in/nazariy-buryak-778433350/) | [GitHub](https://github.com/K0NGR3SS)
