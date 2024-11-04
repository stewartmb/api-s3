import boto3

def lambda_handler(event, context):
    # Input (JSON)
    nombre_bucket = event['body']['bucket']
    nombre_directorio = event['body']['directory'] + '/'  # Ensuring it ends with '/'
    
    # Process
    s3 = boto3.client('s3')
    try:
        # Create an empty object with a key ending in '/'
        s3.put_object(Bucket=nombre_bucket, Key=nombre_directorio)
        return {
            'statusCode': 200,
            'message': f'Directory {nombre_directorio} created in bucket {nombre_bucket} successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'error': str(e)
        }
