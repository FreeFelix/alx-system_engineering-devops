# Setup New Ubuntu server with Nginx

# Update the system
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
  require => Exec['update system'],
}

# Create a simple Hello World index file
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Set up a redirection rule for /redirect_me to a YouTube video
exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
