#pull and run mysql by docker
#
docker pull mysql
docker run --name huy-mysql -e MYSQL_ROOT_PASSWORD=12345678 -e MYSQL_USER=huysql -e MYSQL_PASSWORD=11111111 -d -p 3306:3306 mysql

#enter password
#create schema
run schema.sql