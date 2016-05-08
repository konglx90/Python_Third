学习一些Python组件
celery
supervisord
essay



Celery

Celery是一个用Python写的分布式任务队列系统。

介绍Celery最简单的应用，包括：

 - 选择并安装消息代理（broker）
	+ Redis、RabbitMQ
 - 安装Celery并创建任务
 - 运行worker并调用任务
 - 跟踪任务执行状态，检查任务返回值

我使用的代理容器是redis, 先在ubuntu上安装好redis

安装celery
`pip install celery`

helloworld
