#!/usr/bin/env bash
#manifest file that changes our configuration file
file { '/etc/ssh/ssh_config':
ensure => present
}

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}
