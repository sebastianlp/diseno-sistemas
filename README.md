## Levantar la aplicacion
1. Levantar la maquina virtual `vagrant up`
2. Conectarse a ssh `vagrant ssh`
  1. Crear la base de datos con el usuario y darle permisos siguiendo los pasos de la guia.
    1. `sudo su - postgres`
    2. `psql`
    3. `CREATE USER fantasy_football WITH PASSWORD 'claveresegura';`
    4. `ALTER USER fantasy_football CREATEDB;`
    5. `CREATE DATABASE fantasy_footballdb WITH OWNER fantasy_football;`
    6. `\c fantasy_footballdb`
    7. `REVOKE ALL ON SCHEMA public FROM public;`
    8. `GRANT ALL ON SCHEMA public to fantasy_football`
  2. Ir al directorio del proyecto `cd /vagrant/TP`
  3. Ejecutar las migrations `python3 manage.py migrate`
  4. Ejecutar el servidor `python3 manage.py runserver 0:5000`

## Administracion
1. Ingresar a `http://0.0.0.0:5000/admin
2. Logearse usando las credenciales
```
user: admin
password: admin321
```