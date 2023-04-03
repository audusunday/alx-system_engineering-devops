WEB SERVER

This project encompases the following learning objective;

General

What is the main role of a web server?

What is a child process?

Why web servers usually have a parent process and child processes?

What are the main HTTP requests?

Below were the files creatwed and their expected output;

0-transfer_file - Writes a Bash script that transfers a file from our client to a server:

1-install_nginx_web_server - Writes a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself).

2-setup_a_domain_name - Setup a domain name.

3-redirection - Configures a Nginx server so that /redirect_me is redirecting to another page.

4-not_found_page_404 - Configures a Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

7-puppet_install_nginx_web_server.pp - Configures a server using a Puppet. To save time and effort, resources are included in the manifest to perform a 301 redirect when querying /redirect_me.
