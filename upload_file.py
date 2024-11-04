import boto3
import base64

def lambda_handler(event, context):
    # Input (JSON)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directory'] + '/'  # Ensure it ends with '/'
    objeto_key = nombre_directorio + event['body']['filename']
    file_content = base64.b64decode(event['body']['content'])  # Decoding the base64 content
    
    # Process
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=nombre_bucket, Key=objeto_key, Body=file_content)
        return {
            'statusCode': 200,
            'message': f'File {event["body"]["filename"]} uploaded to directory {nombre_directorio} in bucket {nombre_bucket} successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'error': str(e)
        }
