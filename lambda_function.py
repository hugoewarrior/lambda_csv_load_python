import json
import boto3

# Initialize resources to use from AWS 
s3_cient = boto3.client('s3')
dynamo_db = boto3.resource('dynamodb')
table = dynamo_db.Table('locationsbucket') 

def lambda_handler(event, context):
    # Initialize necessary variables
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]
    resp = s3_cient.get_object(Bucket=bucket_name, Key=s3_file_name)
    
    #Read the file taken from the bucket
    data = resp['Body'].read().decode('utf-8')
    
    #Print on CloudWatch and Console
    locations = data.split("\n")
    headers = locations.pop(0).split(",")

    print(headers)
    print("*******************************************")
    print(data)

    for loc in locations:
        loc = loc.split(",")
        # Validation for record reading
        try:               
            table.put_item(
                Item = {
                    headers[0]: str(loc[0]),
                    headers[1]: str(loc[1]),
                    headers[2]: str(loc[2]), 
                    headers[3]: str(loc[3]), 
                    headers[4]: str(loc[4]), 
                    headers[5]: str(loc[5]), 
                    headers[6]: str(loc[6]), 
                    headers[7]: str(loc[7]), 
                    headers[8]: str(loc[8])
                })
        except Exception as err:
            print ("Warning on load: "+str(err))
    return {
        'statusCode': 200,
        'body': json.dumps('Cool! My Lambda is working!')
    }