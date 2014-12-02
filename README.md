AWSnapshots
===========

Simple tool to manage AWS Volume Snapshots using the AWS API

## Install

    #$ pip install awsnapshots

## Configure

Create a configuration file named **awsnapshots.yaml** in either the current working directory, or use `--config path/to/config.yaml` if you want to run this script from a different environment.

```yaml
AWS_ACCESS_KEY: access_key
AWS_ACCESS_KEY: secret_key
```

## Usage

    usage: awsnapshots [-h] [--config CONFIG] region volume keep [description]

    Simple tool to manage AWS Volume Snapshots using the AWS API.

    positional arguments:
      region           The ID of the AWS region where your volumes are. (e.g., us-
                       west-1)
      volume           The ID of the volume you want to take the snapshot from.
                       (e.g., vol-abcd1234)
      keep             Number of snapshots to keep. (i.e., if 3, the last 3
                       snapshots will be kept. When the fourth one is taken, the
                       oldest will be automatically deleted.
      description      Snapshot description

    optional arguments:
      -h, --help       show this help message and exit
      --config CONFIG  YAML formatted configuration file to be used. Default is
                       ./awsnapshots.yaml

Example:

    #$ awsnapshots us-west-1 vol-abcd1234 3 "Test snapshots"

The above example will create a snapshot of the volume **vol-abcd1234** located at **us-west-1**, named **Test snapshots**, each time it's called. If you run it four or more times, only the latest 3 snapshots will be kept. The older ones will be deleted.
