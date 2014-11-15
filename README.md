AWSnapshots
===========

Simple tool to manage AWS Volume Snapshots using the AWS API

## Install

    #$ pip install awsnapshots

## Configure

Create a configuration file named **awsnapshots.yaml** in either the current working directory, or at `/etc/` if you want to run this script from a different environment.

```yaml
AWS_ACCESS_KEY: access_key
AWS_ACCESS_KEY: secret_key
```

## Usage

    #$ awsnapshots **region-id volume-id snapshots-to-keep [description]**

Example:

    #$ awsnapshots us-west-1 vol-abcd1234 3 "Test snapshots"

The above example will create a snapshot of the volume **vol-abcd1234** located at **us-west-1**, named **Test snapshots**, each time it's called. If you run it four or more times, only the latest 3 snapshots will be kept. The older ones will be deleted.
