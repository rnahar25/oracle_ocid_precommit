# Precommit Hook Checking for OCID values

Most types of Oracle Cloud Infrastructure resources have an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). It's included as part of the resource's information in both the Console and API.
https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm

We do not want to include this value within our code. This precommit hook will check for OCID values.
