#!/bin/bash

function linstall.nfsc.usage(){
    cat << EOF
Description
Syntax: linstall.nfsc
EOF
}

function linstall.nfsc(){
    if [ "$1" == "-h" ]; then
        linstall.nfss.usage
        return 0
    fi
    local dist="$(lsb_release -d)"
    case "$dist" in
        *Debian* )
            wajig install nfs-common rpcbind
            return 0;;
        *LMDE* )
            wajig install nfs-common rpcbind
            return 0;;
        *Ubuntu* )
            wajig install nfs-common rpcbind
            return 0;;
        * )
            echo "This script does not support ${dist:13}."
            return 1;;
    esac
}

if [ "$0" == ${BASH_SOURCE[0]} ]; then
    linstall.nfsc $@
fi
