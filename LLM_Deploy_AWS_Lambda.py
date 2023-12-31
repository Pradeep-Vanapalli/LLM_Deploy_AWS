# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import json
import boto3

ENDPOINT = 'XXXXXX XXX'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
  query_params = event['queryStringParameters']
  query = query_params.get('query')
  payload = {
    'inputs':prompt,
    'parameters':{
        'do_sample':True,
        'top_p':0.7,
        'temperature':0.3,
        'top_k':50,
        'max_new_tokens':512,
        'repetition_penalty':1.03}}

  response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='application/json', Body=json.dumps(payload))
  prediction = json.loads(response['Body'].read().decode('utf-8'))
  final_result = prediction[0]['generated_text']

  return {
      'statusCode':200,
      'body':json.dumps(final_result)
  }

Even Json

{
    'httpMethod':'GET',
    'path':'/example',
    'queryStringParameters':{
        'query': "Write a short article on blockchain"
    }
}