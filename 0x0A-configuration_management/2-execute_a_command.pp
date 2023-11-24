#manifest file kills process 'killmenow'
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow', onlyif => '/usr/bin/pgrep killmenow'
}
