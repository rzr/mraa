#
# Regular cron jobs for the mraa package
#
0 4	* * *	root	[ -x /usr/bin/mraa_maintenance ] && /usr/bin/mraa_maintenance
