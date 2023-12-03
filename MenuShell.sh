#!/bin/bash
clear

end=0
while [ $end = 0]
do
		echo "M E N U   S H E L L S"
		echo "1) Numero de lineas encontradas en el archivo /etc/profile"
		echo "2) Buscar la palabra dada por el usuario en un archivo especifico."
		echo "3) Nombres de usuario y la descripcion de los mismos."
		echo "4) Revisar si hay intentos de acceso ilegales al usurario junto con la feca y hora de cada intento."
		echo "5) Salir."
		read numMenu
		
		case "$numMenu" in
				
				1)
						sh ./contarlineas1.sh
				;;
				2)
						echo "Escriba la palabra que quiera buscar."
						read word
						echo "Digite el directorio en el cual quiere buscar."
						read folder
						sh ./buscarpalabra2.sh $palabra $directorio
				;;
				3)
						sh ./extraerNombres3.sh
						echo ""
				;;
				4)
						echo "Digite el Archivo."
						read archivo
						echo "Digite los permisos."
						read permisos
						sh ./buscarArchivo4.sh $directorio $permisos
				;;
				5)
						end=1
				;;
				*)
				;;
		esac
done				