# Levantar la aplicacion

1. Levantar la maquina virtual `vagrant up`
2. Conectarse a ssh `vagrant ssh`
3. Crear la base de datos con el usuario y darle permisos siguiendo los pasos de la guia.
	* `sudo su - postgres`
	* `psql`
	* `CREATE USER fantasy_football WITH PASSWORD 'claveresegura';`
	* `ALTER USER fantasy_football CREATEDB;`
	* `CREATE DATABASE fantasy_footballdb WITH OWNER fantasy_football;`
	* `\c fantasy_footballdb`
	* `REVOKE ALL ON SCHEMA public FROM public;`
	* `GRANT ALL ON SCHEMA public to fantasy_football`
4. Ir al directorio del proyecto `cd /vagrant/TP`
5. Ejecutar las migrations `python3 manage.py migrate`
6. Ejecutar el servidor `python3 manage.py runserver 0:5000`

## El admin
1. Ingresar a `http://0.0.0.0:5000/admin
2. Logearse usando las credenciales
```
user: admin
password: admin321
```
