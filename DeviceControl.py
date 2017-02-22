#!/bin/env python
# -*- coding: utf-8 -*-

""" ATENCIÓN: Este script sólo funciona con dispositivos listados por el comando "xinput",
intercambiando su estado de "enable" a "disable" y viceversa.
Es recomendable asignar su ejecución a una combinación de teclas específica.

Importante: Al iniciar el sistema se debe crear el archivo /tmp/device_status, el cual debe 
contener un 1 o un 0, dependiendo del estado inicial del dispositivo a controlar.
El método recomendado es utilizar el archivo ~/.profile, conteniendo lo siguiente.

- Si el dispositivo arranca ENCENDIDO:
	echo "1" > /tmp/device_status

- Si el dispositivo arranca APAGADO:
	echo "0" > /tmp/device_status

"""


from os import system
from subprocess import check_output

## String del dispositivo a controlar, tal y como se muestra a la salida de "xinput"
device = "SYNAPTICS Synaptics Large Touch Screen"

cmd = "xinput --list --id-only"
disable_cmd = "xinput disable "
enable_cmd = "xinput enable "
status_cmd = "cat /tmp/device_status"
status_cmd = status_cmd.split(' ')

cmd = cmd.split(' ')
cmd.append(device)

## Detecto ID
out = check_output(cmd)
out = str(out)

out = out.split("'")
out = out[1].split('\\n')
out = out[0]

print ('ID: '+out)


## Formo los comandos para Activar/Desactivar el dispositivo
disable_dev = disable_cmd+out
disable_dev = disable_dev

enable_dev = enable_cmd+out
enable_dev = enable_dev

## Verifico estado actual
status = str(check_output(status_cmd))
status = status.split('\\n')[0].split("'")[-1]



if (status == "1"):
	try:
		system(disable_dev)
		print('Desactivando...')
		cmdDev = 'notify-send -i checkbox-mixed-symbolic "Disposivo Desactivado" "'+device+' ha sido desactivado"'
		system(cmdDev)
		system('echo "0" > /tmp/device_status')
	except:
		system('notify-send -i checkbox-mixed-symbolic "Error al Desactivar" "Se produjo un error al intentar desactivar el dispositivo"')

if (status == "0"):
	try:
		system(enable_dev)
		print('Activando...')
		cmdDev = 'notify-send -i checkbox-checked-symbolic "Disposivo Activado" "'+device+' ha sido activado"'
		system(cmdDev)
		system('echo "1" > /tmp/device_status')
	except:
		system('notify-send -i checkbox-checked-symbolic "Error al Activar" "Se produjo un error al intentar activar el dispositivo"')