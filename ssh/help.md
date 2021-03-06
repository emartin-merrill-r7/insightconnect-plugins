# Description

[Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network.
This plugin uses the [paramiko](http://www.paramiko.org/) to connect to a remote host via the library. The SSH plugin allows you to run commands on a remote host.

# Key Features

* Run remote commands with SSH

# Requirements

* Credentials for the target remote host
* Address and port for the target remote host

# Documentation

## Setup

This plugin requires the SSH host (IP address or domain), port, username, and either a password or SSH private key for authentication.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Remote host to connect to. Can be over-ridden in actions|None|
|key|credential_asymmetric_key|None|False|A base64 encoded SSH private key to use to authenticate to remote server. A newline is required after the beginning and before the end marker|None|
|password|credential_secret_key|None|False|Password authentication or password to decrypt provided private key. Either this or SSH private key is required|None|
|port|integer|22|True|Remote port to use|None|
|use_key|boolean|None|True|True to connect via key, false to connect via password|None|
|username|credential_secret_key|None|True|User to run command as|None|

The `key` field takes a base64 encoded RSA private key which must contain a newline character after the BEGIN marker and before the END marker:
E.g.

```

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7g4h53s=
...
-----END RSA PRIVATE KEY-----

```

You can easily encode a private key file and copy it to your clipboard on MacOS with the following command: `base64 < .ssh/id_rsa | pbcopy`.
This can then be pasted into the Connection's `key` input field.

## Technical Details

### Actions

#### Run Remote Command

This action is used to run remote command.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|command|string|None|True|Command to execute on remote host|None|
|host|string|None|False|Host to run remote commands. If not provided, the connection host will be used|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|results|True|Results|

Example output:

```
{
  "results": {
    "all_output": "total 57068\n\ndrwxrwxr-x. 2 rapid7 rapid7        6 Nov  4 20:15 test\n\n-rw-rw-r--. 1 rapid7 rapid7       13 Nov  4 20:15 test.txt\n\n-rw-r--r--. 1 rapid7 rapid7 58433536 Mar 26  2019 VBoxGuestAdditions.iso\n",
    "stderr": "",
    "stdout": "total 57068\n\ndrwxrwxr-x. 2 rapid7 rapid7        6 Nov  4 20:15 test\n\n-rw-rw-r--. 1 rapid7 rapid7       13 Nov  4 20:15 test.txt\n\n-rw-r--r--. 1 rapid7 rapid7 58433536 Mar 26  2019 VBoxGuestAdditions.iso\n"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Update Run action output to return 3 output fields i.e. `stderr`, `stdout`, and `all_output`
* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - Fixed issue where Run was excluded
* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Support web server mode | Update to new credential types | Rename "Run remote command" action to "Run Remote Command"
* 0.1.3 - SSL bug fix in SDK
* 0.1.2 - Strip extra newlines in key
* 0.1.1 - Connection SSH key input is now type bytes
* 0.1.0 - Initial plugin

# Links

## References

* [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)
* [OpenSSH](https://www.openssh.com/)
* [paramiko](http://www.paramiko.org/)

## Custom Output Types

### results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stderr|string|True|Stderr|
|stdout|string|True|Stdout|
|all_output|string|True|All output|
