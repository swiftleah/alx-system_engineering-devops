package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80;
      root /var/www/html;
      index index.html;
      
      location / {
        try_files $uri $uri/ =404;
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
