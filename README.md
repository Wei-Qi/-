## 地摊货二手商品交易平台

----

#### 依赖的包

```text
flask_mail
werkzeug
flask_sqlalchemy
flask_migrate
flask_login
flask_wtf
email-validator
pymysql
```

----

#### 数据库更改的方法

```text
flask db init
flask db migrate
flask db upgrade
```

初始化创建表时，先删除`migrations`文件夹，执行
```text
flask db init
flask db migrate
flask db upgrade
```
当表发生变化时，执行
```text
flask db migrate
flask db upgrade
```


#### 任务
前端：添加一个顶部的导航栏，用于显示用户的登陆状态，用户基本信息。以及要改很多的网页链接<a href=""