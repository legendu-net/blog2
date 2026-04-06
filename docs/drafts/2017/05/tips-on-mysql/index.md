---
title: Tips on MySQL
created: 2017-05-22 14:45:18
date: 2026-04-05 19:42:38.084636
authors:
- bendu
label: tips-on-mysql
license: CC-BY-4.0
tags:
- Database
- programming
- tips
- MySQL
- Python
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

```bash
sudo service mysql restart
```


```sh
mysqladmin -u root -p variables | grep port
```

`mysqladmin --help` list the locations of `my.cnf`.
```sh
mysqladmin --help
```

## Python Packages 

1. peewee

2. PyMySQL

3. MySQLdb

## References 

- [MySQL Cheat Sheet](http://cse.unl.edu/~sscott/ShowFiles/SQL/CheatSheet/SQLCheatSheet.html)
- [MySQL Tutorial](http://zetcode.com/databases/mysqltutorial/)  
- [MySQL Tutorial on ClockWatch](http://www.clockwatchers.com/mysql_databases.html)