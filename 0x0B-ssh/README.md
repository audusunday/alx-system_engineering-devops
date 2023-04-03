0x0B. SSH
SSH

Learning Objectives;

General What is a server.

Where servers usually live.

What is SSH.

How to create an SSH RSA key pair.

How to connect to a remote host using an SSH RSA key pair.

The advantage of using #!/usr/bin/env bash instead of /bin/bash.

Below were the files created and their respective output;

0-use_a_private_key - Writes a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

1-create_ssh_key_pair - Writes a Bash script that creates an RSA key pair.

2-ssh_config - Configures my SSH files for the local SSH client in a way it can connect to a server without typing in a password.

100-puppet_ssh_config.pp - Puppet to make changes to our configuration file.

