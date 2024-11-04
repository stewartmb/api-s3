import boto3

def lambda_handler(event, context):
    # Input (JSON)
    nombre_bucket = event['body']['bucket']
    
    # Process
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=nombre_bucket)
        return {
            'statusCode': 200,
            'message': f'Bucket {nombre_bucket} deleted successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'error': str(e)
        }
