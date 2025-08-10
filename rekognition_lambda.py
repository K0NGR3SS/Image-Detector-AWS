import boto3
import json

def lambda_handler(event, context):

    #Initializing all the clients
    s3_client = boto3.client('s3')
    rekognition_client = boto3.client('rekognition')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ImageAnalysisResult')

    #Get the S3 bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    #Call Amazon Rekognition to detect labels in the image
    response = rekognition_client.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': object_key}},
        MaxLabels=10
    )

    #Store the labels detected in DynamoDB
    labels = [{'Confidence': label['Confidence'], 'Name': label['Name']} for label in response['Labels']]
    table.put_item(
        Item={
            'ImageName': object_key,
            'Labels': json.dumps(labels)
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully!')
    }