#!/bin/sh

PATH=.:$PATH
cat << EOF >> "${nsjail_cfg}"
mount {
	src: "/dev"
	dst: "/dev"
	is_bind: true
	rw: true
}
mount {
	src: "/dev/shm"
	dst: "/dev/shm"
	is_bind: true
	rw: true
	options: "size=20m"
	nodev: true
	nosuid: true
	noexec: true
}
EOF
