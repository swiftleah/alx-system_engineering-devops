# puppet file - fixes issue - Apache returning 500 error
exec { 'fixed-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
}
