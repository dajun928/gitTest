MySQL 
һ��������װMySQL
sudo apt-get autoremove mysql-client 
sudo apt-get autoremove mysql-server 
sudo apt-get autoremove mysql-common

����������ݺ�������Ϣ 
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P 

sudo apt-get install mysql-server mysql-client ��װMySQL�� 

sudo service mysql start/stop/restart ���������/ֹͣ/����mysql����
mysql -uXXX -pxxx ����mysql
����һЩ��������
��1��mysql-python��װʱEnvironmentError: mysql_config not found
���������
sudo apt-get install libmysqlclient-dev
��������utf-8���ݿ�
CREATE DATABASE `test2` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; 
�ġ����ݵĵ�������
mysql�������ݿ����б�ṹ�Լ�����
mysqldump -uroot -p -d dbname >db.sql;
mysql�������ݿ�ĳ����ṹ�Լ�����
mysqldump -uroot -p dbname tablename > db.sql

�������ݣ�source info.sql��
��mysql -uroot -p world < info.sql

�﷨��mysqldump -h[hosname] -u[user_name] -p[password] --default-character-set=[char_set_name] [db_name] [save_path]
�塢mysql��ʱ���ݣ�������棺Warning: Using a password on the command line interface can be insecure��
(1) ������mysql�����ļ�������û���Ϣ:
[client]
user = root
password = root
(2) ʹ��mysqldump:(������ʱ�����ļ�schedule_backup.sh)
mysqldump --defaults-extra-file=/etc/mysql/mysql.conf.d/mysqld.cnf world info > info.sql
(3) ��Ӷ�ʱ����(crontab)

����mysql��������Զ������
��1������mysql
��2��use mysql
��3�����������û�����Զ������mysql
grant all privileges on *.* to 'root'@'%' identified by 'password-here' with grant option;
flush privileges;

