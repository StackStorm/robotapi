#!/bin/bash
### BEGIN INIT INFO
# Provides:    robotapi
# Required-Start: $local_fs $network $named $time $syslog
# Required-Stop:  $local_fs $network $named $time $syslog
# Default-Start:  2 3 4 5
# Default-Stop:   0 1 6
# Description:    robotapi Swagger API
### END INIT INFO

if [ "$1" == "start" ]; then
	source ~/robotapi/.venv/bin/activate
	nohup python3 -m swagger_server > ~/robotapi/server.log 2>&1 & echo $! > ~/robotapi/.server.pid &
	deactivate
	cd ~/robotarm
fi

if [ "$1" == "stop" ]; then
	server_pid=$(cat ~/robotapi/.server.pid)
	kill $server_pid
fi
