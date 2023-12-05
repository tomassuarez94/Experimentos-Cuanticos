#!/bin/bash
clear
nlineas=(Get-Content /etc/profile).lenght
echo "El numero de lineas del archivo /etc/profile es:" $nlineas
