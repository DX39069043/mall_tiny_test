[toc]
# 1	环境变量

### 默认环境1
| 参数名 | 字段值 |
| ------ | ------ |
|baseUrl|http://localhost:8080|


# 2	mall-tiny项目骨架

##### 说明
> 



##### 联系方式
- **联系人：**macro
- **邮箱：**
- **网址：**//

##### 文档版本
```
1.0
```


# 3	UmsMenuController

## 3.1	添加后台菜单

> POST  /menu/create
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| createTime|string||false|创建时间|
| hidden|int32||false|前端隐藏|
| icon|string||false|前端图标|
| id|int32||false||
| level|int32||false|菜单级数|
| name|string||false|前端名称|
| parentId|int32||false|父级ID|
| sort|int32||false|菜单排序|
| title|string||false|菜单名称|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 3.2	根据ID删除后台菜单

> POST  /menu/delete/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 3.3	分页查询后台菜单

> GET  /menu/list/{parentId}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|parentId||parentId|
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|pageNum||pageNum|
|pageSize||pageSize|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
|⇥ list|array[object]||false||
|⇥⇥ createTime|string||false|创建时间|
|⇥⇥ hidden|int32||false|前端隐藏|
|⇥⇥ icon|string||false|前端图标|
|⇥⇥ id|int32||false||
|⇥⇥ level|int32||false|菜单级数|
|⇥⇥ name|string||false|前端名称|
|⇥⇥ parentId|int32||false|父级ID|
|⇥⇥ sort|int32||false|菜单排序|
|⇥⇥ title|string||false|菜单名称|
|⇥ pageNum|int32||false||
|⇥ pageSize|int32||false||
|⇥ total|int32||false||
|⇥ totalPage|int32||false||
| message|string||false||

##### 接口描述
> 




## 3.4	树形结构返回所有菜单列表

> GET  /menu/treeList
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ createTime|string||false|创建时间|
|⇥ hidden|int32||false|前端隐藏|
|⇥ icon|string||false|前端图标|
|⇥ id|int32||false||
|⇥ level|int32||false|菜单级数|
|⇥ name|string||false|前端名称|
|⇥ parentId|int32||false|父级ID|
|⇥ sort|int32||false|菜单排序|
|⇥ title|string||false|菜单名称|
| message|string||false||

##### 接口描述
> 




## 3.5	修改后台菜单

> POST  /menu/update/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| createTime|string||false|创建时间|
| hidden|int32||false|前端隐藏|
| icon|string||false|前端图标|
| id|int32||false||
| level|int32||false|菜单级数|
| name|string||false|前端名称|
| parentId|int32||false|父级ID|
| sort|int32||false|菜单排序|
| title|string||false|菜单名称|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 3.6	修改菜单显示状态

> POST  /menu/updateHidden/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|hidden||hidden|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 3.7	根据ID获取菜单详情

> GET  /menu/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false|后台菜单表|
|⇥ createTime|string||false|创建时间|
|⇥ hidden|int32||false|前端隐藏|
|⇥ icon|string||false|前端图标|
|⇥ id|int32||false||
|⇥ level|int32||false|菜单级数|
|⇥ name|string||false|前端名称|
|⇥ parentId|int32||false|父级ID|
|⇥ sort|int32||false|菜单排序|
|⇥ title|string||false|菜单名称|
| message|string||false||

##### 接口描述
> 




# 4	UmsResourceCategoryController

## 4.1	添加后台资源分类

> POST  /resourceCategory/create
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| createTime|string||false|创建时间|
| id|int32||false||
| name|string||false|分类名称|
| sort|int32||false|排序|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 4.2	根据ID删除后台资源

> POST  /resourceCategory/delete/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 4.3	查询所有后台资源分类

> GET  /resourceCategory/listAll
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ createTime|string||false|创建时间|
|⇥ id|int32||false||
|⇥ name|string||false|分类名称|
|⇥ sort|int32||false|排序|
| message|string||false||

##### 接口描述
> 




## 4.4	修改后台资源分类

> POST  /resourceCategory/update/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| createTime|string||false|创建时间|
| id|int32||false||
| name|string||false|分类名称|
| sort|int32||false|排序|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




# 5	UmsRoleController

## 5.1	给角色分配菜单

> POST  /role/allocMenu
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|menuIds||menuIds|
|roleId||roleId|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 5.2	给角色分配资源

> POST  /role/allocResource
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|resourceIds||resourceIds|
|roleId||roleId|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 5.3	添加角色

> POST  /role/create
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| adminCount|int32||false|后台用户数量|
| createTime|string||false|创建时间|
| description|string||false|描述|
| id|int32||false||
| name|string||false|名称|
| sort|int32||false||
| status|int32||false|启用状态：0->禁用；1->启用|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 5.4	批量删除角色

> POST  /role/delete
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|ids||ids|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 5.5	根据角色名称分页获取角色列表

> GET  /role/list
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|keyword||keyword|
|pageNum||pageNum|
|pageSize||pageSize|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
|⇥ list|array[object]||false||
|⇥⇥ adminCount|int32||false|后台用户数量|
|⇥⇥ createTime|string||false|创建时间|
|⇥⇥ description|string||false|描述|
|⇥⇥ id|int32||false||
|⇥⇥ name|string||false|名称|
|⇥⇥ sort|int32||false||
|⇥⇥ status|int32||false|启用状态：0->禁用；1->启用|
|⇥ pageNum|int32||false||
|⇥ pageSize|int32||false||
|⇥ total|int32||false||
|⇥ totalPage|int32||false||
| message|string||false||

##### 接口描述
> 




## 5.6	获取所有角色

> GET  /role/listAll
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ adminCount|int32||false|后台用户数量|
|⇥ createTime|string||false|创建时间|
|⇥ description|string||false|描述|
|⇥ id|int32||false||
|⇥ name|string||false|名称|
|⇥ sort|int32||false||
|⇥ status|int32||false|启用状态：0->禁用；1->启用|
| message|string||false||

##### 接口描述
> 




## 5.7	获取角色相关菜单

> GET  /role/listMenu/{roleId}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|roleId||roleId|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ createTime|string||false|创建时间|
|⇥ hidden|int32||false|前端隐藏|
|⇥ icon|string||false|前端图标|
|⇥ id|int32||false||
|⇥ level|int32||false|菜单级数|
|⇥ name|string||false|前端名称|
|⇥ parentId|int32||false|父级ID|
|⇥ sort|int32||false|菜单排序|
|⇥ title|string||false|菜单名称|
| message|string||false||

##### 接口描述
> 




## 5.8	获取角色相关资源

> GET  /role/listResource/{roleId}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|roleId||roleId|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ categoryId|int32||false|资源分类ID|
|⇥ createTime|string||false|创建时间|
|⇥ description|string||false|描述|
|⇥ id|int32||false||
|⇥ name|string||false|资源名称|
|⇥ url|string||false|资源URL|
| message|string||false||

##### 接口描述
> 




## 5.9	修改角色

> POST  /role/update/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| adminCount|int32||false|后台用户数量|
| createTime|string||false|创建时间|
| description|string||false|描述|
| id|int32||false||
| name|string||false|名称|
| sort|int32||false||
| status|int32||false|启用状态：0->禁用；1->启用|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 5.10	修改角色状态

> POST  /role/updateStatus/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|status||status|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




# 6	UmsResourceController

## 6.1	添加后台资源

> POST  /resource/create
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| categoryId|int32||false|资源分类ID|
| createTime|string||false|创建时间|
| description|string||false|描述|
| id|int32||false||
| name|string||false|资源名称|
| url|string||false|资源URL|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 6.2	根据ID删除后台资源

> POST  /resource/delete/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 6.3	分页模糊查询后台资源

> GET  /resource/list
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|categoryId||categoryId|
|nameKeyword||nameKeyword|
|pageNum||pageNum|
|pageSize||pageSize|
|urlKeyword||urlKeyword|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
|⇥ list|array[object]||false||
|⇥⇥ categoryId|int32||false|资源分类ID|
|⇥⇥ createTime|string||false|创建时间|
|⇥⇥ description|string||false|描述|
|⇥⇥ id|int32||false||
|⇥⇥ name|string||false|资源名称|
|⇥⇥ url|string||false|资源URL|
|⇥ pageNum|int32||false||
|⇥ pageSize|int32||false||
|⇥ total|int32||false||
|⇥ totalPage|int32||false||
| message|string||false||

##### 接口描述
> 




## 6.4	查询所有后台资源

> GET  /resource/listAll
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ categoryId|int32||false|资源分类ID|
|⇥ createTime|string||false|创建时间|
|⇥ description|string||false|描述|
|⇥ id|int32||false||
|⇥ name|string||false|资源名称|
|⇥ url|string||false|资源URL|
| message|string||false||

##### 接口描述
> 




## 6.5	修改后台资源

> POST  /resource/update/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| categoryId|int32||false|资源分类ID|
| createTime|string||false|创建时间|
| description|string||false|描述|
| id|int32||false||
| name|string||false|资源名称|
| url|string||false|资源URL|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

##### 接口描述
> 




## 6.6	根据ID获取资源详情

> GET  /resource/{id}
### 地址参数（Path Variable）
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false|后台资源表|
|⇥ categoryId|int32||false|资源分类ID|
|⇥ createTime|string||false|创建时间|
|⇥ description|string||false|描述|
|⇥ id|int32||false||
|⇥ name|string||false|资源名称|
|⇥ url|string||false|资源URL|
| message|string||false||

##### 接口描述
> 




# 7	UmsAdminController

## 7.1	删除指定用户信息

> POST  /admin/delete/{id}
**地址参数（Path Variable）**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.2	获取当前登录用户信息

> GET  /admin/info
**请求参数(Query Param)**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|name|||
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.3	根据用户名或姓名分页获取用户列表

> GET  /admin/list
**请求参数(Query Param)**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|keyword||keyword|
|pageNum||pageNum|
|pageSize||pageSize|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
|⇥ list|array[object]||false||
|⇥⇥ createTime|string||false|创建时间|
|⇥⇥ email|string||false|邮箱|
|⇥⇥ icon|string||false|头像|
|⇥⇥ id|int32||false||
|⇥⇥ loginTime|string||false|最后登录时间|
|⇥⇥ nickName|string||false|昵称|
|⇥⇥ note|string||false|备注信息|
|⇥⇥ password|string||false||
|⇥⇥ status|int32||false|帐号启用状态：0->禁用；1->启用|
|⇥⇥ username|string||false||
|⇥ pageNum|int32||false||
|⇥ pageSize|int32||false||
|⇥ total|int32||false||
|⇥ totalPage|int32||false||
| message|string||false||

**接口描述**

> 




## 7.4	登录以后返回token

> POST  /admin/login
注：username和password只能由数字或字母构成，长度不能超过20且不能为空

**请求体(Request Body)**

| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| password|string||true|密码|
| username|string||true|用户名|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.5	登出功能

> POST  /admin/logout
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.6	刷新token

> GET  /admin/refreshToken
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.7	用户注册

> POST  /admin/register
**请求体(Request Body)**

注：username和password只能由数字或字母构成，长度不能超过20且不能为空

| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| email|string||false|邮箱|
| icon|string||false|用户头像|
| nickName|string||false|用户昵称|
| note|string||false|备注|
| password|string||true|密码|
| username|string||true|用户名|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false|后台用户表|
|⇥ createTime|string||false|创建时间|
|⇥ email|string||false|邮箱|
|⇥ icon|string||false|头像|
|⇥ id|int32||false||
|⇥ loginTime|string||false|最后登录时间|
|⇥ nickName|string||false|昵称|
|⇥ note|string||false|备注信息|
|⇥ password|string||false||
|⇥ status|int32||false|帐号启用状态：0->禁用；1->启用|
|⇥ username|string||false||
| message|string||false||

**接口描述**

> 




## 7.8	给用户分配角色

> POST  /admin/role/update
**请求参数(Query Param)**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|adminId||adminId|
|roleIds||roleIds|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.9	获取指定用户的角色

> GET  /admin/role/{adminId}
**地址参数（Path Variable）**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|adminId||adminId|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|array[object]||false||
|⇥ adminCount|int32||false|后台用户数量|
|⇥ createTime|string||false|创建时间|
|⇥ description|string||false|描述|
|⇥ id|int32||false||
|⇥ name|string||false|名称|
|⇥ sort|int32||false||
|⇥ status|int32||false|启用状态：0->禁用；1->启用|
| message|string||false||

**接口描述**

> 




## 7.10	修改指定用户信息

> POST  /admin/update/{id}
**地址参数（Path Variable）**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
**请求体(Request Body)**

| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| createTime|string||false|创建时间|
| email|string||false|邮箱|
| icon|string||false|头像|
| id|int32||false||
| loginTime|string||false|最后登录时间|
| nickName|string||false|昵称|
| note|string||false|备注信息|
| password|string||false||
| status|int32||false|帐号启用状态：0->禁用；1->启用|
| username|string||false||
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.11	修改指定用户密码

> POST  /admin/updatePassword
**请求体(Request Body)**

| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| newPassword|string||true|新密码|
| oldPassword|string||true|旧密码|
| username|string||true|用户名|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.12	修改帐号状态

> POST  /admin/updateStatus/{id}
**地址参数（Path Variable）**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
**请求参数(Query Param)**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|status||status|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false||
| message|string||false||

**接口描述**

> 




## 7.13	获取指定用户信息

> GET  /admin/{id}
**地址参数（Path Variable）**

| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|id||id|
**响应体**

● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false||
| data|object||false|后台用户表|
|⇥ createTime|string||false|创建时间|
|⇥ email|string||false|邮箱|
|⇥ icon|string||false|头像|
|⇥ id|int32||false||
|⇥ loginTime|string||false|最后登录时间|
|⇥ nickName|string||false|昵称|
|⇥ note|string||false|备注信息|
|⇥ password|string||false||
|⇥ status|int32||false|帐号启用状态：0->禁用；1->启用|
|⇥ username|string||false||
| message|string||false||

**接口描述**

> 



 
