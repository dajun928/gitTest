MySQL 
一、快速重装MySQL
sudo apt-get autoremove mysql-client 
sudo apt-get autoremove mysql-server 
sudo apt-get autoremove mysql-common

清除残留数据和配置信息 
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P 

sudo apt-get install mysql-server mysql-client 安装MySQL。 

sudo service mysql start/stop/restart 命令可启动/停止/重启mysql服务
mysql -uXXX -pxxx 连接mysql
二、一些常见错误
（1）mysql-python安装时EnvironmentError: mysql_config not found
解决方法：
sudo apt-get install libmysqlclient-dev
三、创建utf-8数据库
CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; 
四、数据的导进导出
mysql导出数据库所有表结构以及数据
mysqldump -uroot -p -d dbname >db.sql;
mysql导出数据库某个表结构以及数据
mysqldump -uroot -p dbname tablename > db.sql

导入数据：source info.sql；
或：mysql -uroot -p world < info.sql

语法：mysqldump -h[hosname] -u[user_name] -p[password] --default-character-set=[char_set_name] [db_name] [save_path]
五、mysql定时备份（解决警告：Warning: Using a password on the command line interface can be insecure）
(1) 首先在mysql配置文件里添加用户信息:
[client]
user = root
password = root
(2) 使用mysqldump:(建立定时备份文件schedule_backup.sh)
mysqldump --defaults-extra-file=/etc/mysql/mysql.conf.d/mysqld.cnf world info > info.sql
(3) 添加定时任务(crontab)

六、mysql设置允许远程链接
（1）进入mysql
（2）use mysql
（3）设置所有用户可以远程链接mysql
grant all privileges on *.* to 'root'@'%' identified by 'password-here' with grant option;
flush privileges;

