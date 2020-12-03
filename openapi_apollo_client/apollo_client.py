#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 18:52
# @Author  : Weiqiang.long
# @Site    : 
# @File    : apollo_client.py
# @Software: PyCharm
# @Description:
import requests

class RequestClient(object):
    def __init__(self, timeout=60, authorization=None):
        self._timeout = timeout
        self._authorization = authorization

    def _request_get(self, url, params=None):
        if self._authorization:
            return requests.get(
                url=url,
                params=params,
                timeout=self._timeout,
                headers={"Authorization": self._authorization}
            )
        else:
            return requests.get(url=url, params=params, timeout=self._timeout)

    def _request_put(self, url, json_data):
        if self._authorization:
            return requests.put(
                url=url,
                json=json_data,
                timeout=self._timeout,
                headers={"Authorization": self._authorization}
            )
        else:
            return requests.put(url=url, json=json_data, timeout=self._timeout)

    def _request_delete(self, url, params):
        if self._authorization:
            return requests.delete(
                url=url,
                params=params,
                timeout=self._timeout,
                headers={"Authorization": self._authorization}
            )
        else:
            return requests.delete(url=url, params=params, timeout=self._timeout)

    def _request_post(self, url, json_data):
        if self._authorization:
            return requests.post(
                url=url,
                json=json_data,
                timeout=self._timeout,
                headers={"Authorization": self._authorization}
            )
        else:
            return requests.post(url=url, json=json_data, timeout=self._timeout)


class PrivateApolloClient(RequestClient):
    def __init__(self, portal_address, app_id, env='QA', clusterName="default", timeout=60, authorization=None):
        '''
        :param portal_address: apollo接口地址
        :param app_id: 所管理的配置AppId
        :param env: 所管理的配置环境
        :param clusterName: 所管理的配置集群名， 一般情况下传入 default 即可。如果是特殊集群，传入相应集群的名称即可
        :param timeout:
        :param authorization: 鉴权参数
        '''
        RequestClient.__init__(self, timeout=timeout, authorization=authorization)
        self._portal_address = portal_address
        self._appid = app_id
        self._env = env
        self._clusterName = clusterName


    def get_namespace_items_key(self, key, namespaceName='application'):
        '''
        读取配置接口
        :param namespaceName: 所管理的Namespace的名称，如果是非properties格式，需要加上后缀名，如sample.yml
        :param key: 配置对应的key名称
        :return:
        '''
        __url = '{portal_address}/openapi/v1/envs/{env}/apps/{appId}/clusters/{clusterName}/namespaces/{namespaceName}/items/{key}'.format(
            portal_address=self._portal_address, env=self._env, appId=self._appid, clusterName=self._clusterName, namespaceName=namespaceName, key=key
        )
        try:
            return self._request_get(url=__url).json()
        except BaseException as e:
            return e

    def put_namespace_items_key(self, key, value, dataChangeLastModifiedBy, namespaceName='application', comment=None):
        '''
        修改配置接口
        :param namespaceName: 所管理的Namespace的名称，如果是非properties格式，需要加上后缀名，如sample.yml
        :param key: 配置的key，需和url中的key值一致。非properties格式，key固定为content
        :param value: 配置的value，长度不能超过20000个字符，非properties格式，value为文件全部内容
        :param comment: 配置的备注,长度不能超过1024个字符
        :param dataChangeLastModifiedBy: item的修改人，格式为域账号，也就是sso系统的User ID
        :return:
        '''
        __url = '{portal_address}/openapi/v1/envs/{env}/apps/{appId}/clusters/{clusterName}/namespaces/{namespaceName}/items/{key}'.format(
            portal_address=self._portal_address, env=self._env, appId=self._appid, clusterName=self._clusterName, namespaceName=namespaceName, key=key
        )
        __data = {
                "key":key,
                "value":value,
                "comment":comment,
                "dataChangeLastModifiedBy":dataChangeLastModifiedBy
            }
        try:
            return True if self._request_put(url=__url, json_data=__data).status_code is 200 else False
        except BaseException as e:
            return e

    def releases(self, releaseTitle, releaseComment, releasedBy, namespaceName='application'):
        '''
        发布配置接口
        :param releaseTitle: 此次发布的标题，长度不能超过64个字符
        :param releaseComment: 发布的备注，长度不能超过256个字符
        :param releasedBy: 发布人，域账号，注意：如果ApolloConfigDB.ServerConfig中的namespace.lock.switch设置为true的话（默认是false），那么该环境不允许发布人和编辑人为同一人。所以如果编辑人是zhanglea，发布人就不能再是zhanglea。
        :param namespaceName: 所管理的Namespace的名称，如果是非properties格式，需要加上后缀名，如sample.yml
        :return:
        '''
        __url = '{portal_address}/openapi/v1/envs/{env}/apps/{appId}/clusters/{clusterName}/namespaces/{namespaceName}/releases'.format(
            portal_address=self._portal_address, env=self._env, appId=self._appid, clusterName=self._clusterName, namespaceName=namespaceName)
        __data = {
                "releaseTitle":releaseTitle,
                "releaseComment":releaseComment,
                "releasedBy":releasedBy
            }
        try:
            return self._request_post(url=__url, json_data=__data).json()
        except BaseException as e:
            return e


if __name__ == '__main__':
    pass