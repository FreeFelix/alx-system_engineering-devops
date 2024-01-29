# Creates a custom HTTP header response
exec { 'command':
  command   => 'apt-get -y update;
# Update package list
                apt-get -y install nginx;
# Install nginx
                sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
# Add custom header to nginx configuration
                service nginx restart',
# Restart nginx service
  provider  => 'shell',
# Specify shell provider for execution
}
i
