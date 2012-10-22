SnipFlow
---------------------

+ SnipFlow 瀑布流布局
+ PasteBin Syntax Highlight
+ DB Adapter

技术实现
---------------------

+ 瀑布流 Jquery Masonry

  代码作为瀑布流元素的时候限制宽度影响代码美观，所以需要重新制定瀑布排版算法。暂时先转移到中文短文上。
  
  *QAQ*

  + 瀑布流布局不合理.

+ Backend API Flask

  暂时用 SQLAlchemy ORM 来控制 Model.
  
      CREATE DATABASE `test` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
