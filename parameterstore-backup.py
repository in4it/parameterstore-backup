#!/usr/bin/env python

from io import StringIO

import boto3
import botocore
import time
import os
import json
import math

# static variables
S3_BUCKET = os.getenv('S3_BUCKET')
AWS_REGION = os.getenv('AWS_REGION')
ENCRYPTION_KEY_ARN = os.getenv('ENCRYPTION_KEY_ARN')
TODAY = time.strftime("%Y/%m/%d")

# param variables
params = []
params_names = []
params_values = {}
str_params = ''

# boto
s3 = boto3.client('s3', region_name=AWS_REGION)
ssm = boto3.client('ssm', region_name=AWS_REGION)

# describe parameters (without values)
ssm_paginator = ssm.get_paginator('describe_parameters')

page_iterator = ssm_paginator.paginate()

for page in page_iterator:
  for item in page['Parameters']:
    params.append(item)
    params_names.append(item['Name'])

# get values
params_names_loop = math.ceil(len(params_names) / 10) + 1

for x in range(1, params_names_loop):
  response = ssm.get_parameters(Names=params_names[((x-1)*10):(x*10)], WithDecryption=True)
  
  for item in response['Parameters']:
    params_values[item['Name']] = item['Value']

# add values to parameters
for param in params:
  param['Value'] = params_values[param['Name']]
  str_params += json.dumps(param, default=str)+"\n"

# write to s3 bucket
fake_handle = StringIO(str_params)
s3.put_object(Bucket=S3_BUCKET, Key="paramstore-backups/"+TODAY+"/paramstore.csv", Body=fake_handle.read(), ServerSideEncryption='aws:kms', SSEKMSKeyId=ENCRYPTION_KEY_ARN)

