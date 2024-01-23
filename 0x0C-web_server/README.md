0. Transfer a file to your server
mandatory
Write a Bash script that transfers a file from our client to a server:

Requirements:

Accepts 4 parameters
The path to the file to be transferred
The IP of the server we want to transfer the file to
The username scp connects with
The path to the SSH private key that scp uses
Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
scp must transfer the file to the user home directory ~/
Strict host key checking must be disabled when using scp

In this example, I:

remotely execute the ls ~/ command via ssh to see what ~/ contains
create a file named some_page.html
execute my 0-transfer_file script
remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred
That is one way of publishing your website pages to your server.i

Readme:

-y on apt-get command
Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

Install nginx on your web-01
server
Nginx should be listening on port 80
When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
You can’t use systemctl for restarting nginx


In this example 34.198.248.145 is the IP of my web-01 server. If you want to query the Nginx that is locally installed on your server, you can use curl 127.0.0.1.

If things are not going as expected, make sure to check out Nginx logs, they can be found in /var/log/.

Maarten’s PRO-tip: When you use sudo su on your web-01 you can become root like this to test your file

2. Setup a domain name
mandatory
.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

YOU can have a free .tech domain for 1 year by following these steps:

Access the tools space
Unlock the GitHub student pack: WARNING - this invitation link is unique to you and can’t be reclaimed! If you have any issue, please contact GitHub education support


The cost of the domain should be now at $0
You can finalize it by creating an account in .Tech domains
And manage your domain there!
Provide the domain name in your answer file.

Requirement:

provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
go to your profile and enter your domain in the Project website url field


3. Redirection
mandatory
Readme:

Replace a line with multiple lines with sed
Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

The redirection must be a “301 Moved Permanently”
You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task

4. Not found page 404
mandatory
Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

Requirements:

The page must return an HTTP 404 error code
The page must contain the string Ceci n'est pas une page
Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task

5. Install Nginx web server (w/ Puppet)
#advanced
Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

Requirements:

Nginx should be listening on port 80
When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
The redirection must be a “301 Moved Permanently”
Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
