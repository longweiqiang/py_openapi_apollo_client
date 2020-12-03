# py_openapi_apollo_client
python-apollo客户端封装

### 支持的python版本
python3.x

### 功能点
1. 获取apollo中指定namespaceName下的配置数据
2. 修改apollo中指定namespaceName下的配置数据

### 说明
支持鉴权token的传入

### 安装
```shell script
pip install py_openapi_apollo_client
```

### 二次开发
继承PrivateApolloClient类后，增加自己的方法即可

### 使用
```python
from py_openapi_apollo_client.openapi_apollo_client import PrivateApolloClient

client = PrivateApolloClient(app_id='test', portal_address='http://test.com', authorization='xxx')
print(client.get_namespace_items_key(key='test.switch'))
```
