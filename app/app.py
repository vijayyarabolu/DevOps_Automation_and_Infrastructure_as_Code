import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Sample Lambda function for DevOps Project.
    This function simulates a backend API response.
    """
    logger.info("Received event: %s", json.dumps(event))
    
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from the DevOps Pipeline!",
            "status": "healthy",
            "version": "1.0.0"
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    
    return response
