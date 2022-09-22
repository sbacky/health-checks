# health-checks

This repo will be populated with checks to verify a computers health and
status and display vital information.

Currently has two scripts: all_checks.py and display_vitals.py

To run, first clone or fork repo and cd into health-checks, then follow the below steps:

1.) Setup virtual environemnt and install requirements

```sh
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

2.) Run script: (all_checks.py, display_vitals.py)

```sh
python3 all_checks.py
```

## All Checks

This script will print "Everything ok" if all checks pass,
or the corresponding error message if some checks fail.

## Display Vitals

This script will display average CPU usage over 15 minutes in percentage,
RAM usage in percentage and used, free and total memory in percentage and GB.

## FAQ's

### **1. Permission Denied**

Check file permissions and make sure script is exucutable. All files should be executable, however if not,
try using "sudo chmod 777 <path/to/file>" to change permissions on a file and allow it to be executable by
everyone.

If this does not work, try looking at the parent folders permissions and make sure they allow files to
be executed. Folder permissions should look like the following at a minimum: drwxr-xr-x.
