#Puppet script in ruby that creates an SSH config file

file { 'etc/ssh/ssh_config':
	ensure => 'present',
content => "
	#SSH Client configuration
	Host *
	    IdentityFile ~/.ssh/school
	    PasswordAuthentication no
	   ", 
}
