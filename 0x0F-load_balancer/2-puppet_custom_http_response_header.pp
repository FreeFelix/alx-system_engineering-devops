# Use Puppet to automate the task of creating a custom HTTP header response

# Execute 'apt-get update' before installing nginx
exec {'update':
  command => '/usr/bin/apt-get update',
}
# Ensure nginx is present
-> package {'nginx':
  ensure => 'present',
}
# Add a custom HTTP header in the nginx configuration
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
# Restart nginx after updating the configuration
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
