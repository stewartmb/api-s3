import boto3

def lambda_handler(event, context):
    # Input (JSON)
    nombre_bucket = event['body']['bucket']
    objeto_key = event['body']['key']
    
    # Process
    s3 = boto3.client('s3')
    try:
        s3.delete_object(Bucket=nombre_bucket, Key=objeto_key)
        return {
            'statusCode': 200,
            'message': f'Object {objeto_key} deleted from bucket {nombre_bucket} successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'error': str(e)
        }
