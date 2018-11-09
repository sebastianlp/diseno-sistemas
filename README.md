# Diseño de sistemas - FantasyFootball

La aplicacion es un administrador de equipos de futbol.
En ella se crearon las siguientes entidades:
* Equipo: Es la entidad principal, en ella se guarda una coleccion de jugadores y una coleccion de usuarios, asi como tambien la informacion del equipo.
* Jugador: La entidad tiene la informacion del jugador. Se asocia N a 1 con los equipos.
* Estadio: Esta entidad guarda la informacion del estadio y esta relacionada con los equipos en N a 1, ya que un equipo puede tener varios usuarios.
* Partido: La entidad se creo para guardar informacion sobre partidos entre equipos pero no se desarrollo la funcionalidad.
* Perfil: Esta entidad tiene una relacion 1 a 1 con la entidad usuario provista por Django. Se utiliza para extender dicha entidad y darle la posibilidad de relacionar los usuarios con los equipos (de esta forma, un usuario puede administrar - agregar jugadores libres el equipo - el equipo.

## Levantar la aplicacion

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
	* `GRANT all ON SCHEMA public TO fantasy_football;`
	* Desconectarse del servidor psql y volver al usuario de vagrant
4. Ir al directorio del proyecto `cd /vagrant/TP`
5. Instalar las dependencias `pip3 install -r requirements.txt --user`
5. Ejecutar las migrations `python3 manage.py migrate`
6. Ejecutar el servidor `python3 manage.py runserver 0:5000`

## El admin
1. Crear un usuario superadmin `python3 manage.py createsuperuser`
2. Introducir los datos que va solicitando la consola
3. Ingresar a `http://0.0.0.0:5000/admin`
4. Logearse usando las credenciales creadas anteriormente
