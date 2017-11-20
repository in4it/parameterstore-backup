# Parameterstore-backup
Python script to backup the AWS parameter store in S3.

## Configuration
You can set the following environment variables:

* S3\_BUCKET: name of S3 bucket to backup to
* AWS\_REGION: AWS Region of the S3 bucket
* ENCRYPTION\_KEY\_ARN: Encryption key (ARN of KMS) to use to create the backup

# Deployment
This script can be deployed as a scheduled container in AWS ECS. See examples/iam.json for an example IAM task role.

## License
Copyright 2017 in4it BVBA

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

