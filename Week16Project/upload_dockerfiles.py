#!/usr/bin/env python3
from pathlib import Path
import boto3
s3 = boto3.resource('s3')

rootdir ='/home/omar'

for path in Path(rootdir).rglob('Dockerfile'):
        s3.put_object(
            Bucket="mydockerfiles2022",
        )