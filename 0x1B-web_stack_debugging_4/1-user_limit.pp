# Enable user hoberton to login and to open file without an error

# Increase hard file limit for hoberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf"
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/^holberton soft/s/5/50000/' /etc/security/limits.conf"
  path    => '/usr/local/bin/:/bin/'
}
