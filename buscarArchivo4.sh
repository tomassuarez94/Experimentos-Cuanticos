#!/bin/bash
clear

Archivo=$1
Permisos=$2

A=${Permisos:1:3}
B=${Permisos:4:3}
C=${Permisos:7:3}

FA=${A//-}
FB=${B//-}
FC=${C//-}

echo "$(find $Archivo -perm u=$FA,g=$FB,o=$FC)"