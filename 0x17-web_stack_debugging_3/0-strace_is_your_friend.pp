# A puppet manuscript to replace a line in a file on a server
# replace line containing "phpp" with "php" on the php script
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
  path    => ['/bin','/usr/bin']
}
