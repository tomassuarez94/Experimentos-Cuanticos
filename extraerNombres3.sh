#!/bin/sh

awk -F: '{ print $1 print $5}' /etc/passwd
