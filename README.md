# classifier
### 数据表结构

**User**

|     User      |         definition          |      description       |
| :-----------: | :-------------------------: | :--------------------: |
|      id       | Integer, primary_key, index |          主键          |
|   username    |     String(12), unique      |         用户名         | 
|     email     |  String(64), unique, index  |        邮箱地址        |
|      sex      |           Integer           |  性别（1为男 0为女）   |
|   phone_num   |     String(11), unique      |          电话          |
| password_hash |         String(128)         |          密码          |
|   address     |         String(128)         |          地址          |
|   unit        |         String(128)         |          单位          |
|   permission    |       Integer         |         用户权限          |

### API定义

#### api v1

{{baseUrl}} = http://localhost/api/v1

**users**

|                api                 |                 request                 |                           response                           |                         description                          |
| :--------------------------------: | :-------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|            /users/login            |          {'email', 'password'}          | {'code', 'message', 'id', 'username', 'name', 'profile_photo', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'email', 'about_me', 'confirmed'} |       用户登录; 0:用户不存在; 1:登录成功; -1:密码错误        |
|          /users/register           |    {'email', 'password', 'username'}    |                     {'code', 'message'}                      |      用户注册; 0:用户已存在; 1:注册成功,验证邮件已发送       |
|       /users/changePassword        | {'email', 'oldPassword', 'newPassword'} |                     {'code', 'message'}                      | 修改密码; 0:用户不存在 1: 密码修改成功; -1: 修改失败; -2: 原密码错误 |
|       /users/forgetPassword        |                {'email'}                |                     {'code', 'message'}                      |           发送修改邮件; 0:用户不存在; 1:邮件已发送           |
|    /users/deleteUserById/{{id}}    |              Authorization              |                     {'code', 'message'}                      | 通过id删除用户; 0:删除失败; -2:权限不足; -3:-token失效请重新登录; -4:你不能删除你自己; -1:用户不存在; 1:删除成功 |
| /users/deleteUserByEmail/{{email}} |              Authorization              |                     {'code', 'message'}                      | 通过邮箱删除用户; 0:删除失败; -1:用户不存在; -2:权限不足; -3:token失效请重新登录; -4:你不能删除你自己; 1:删除成功 |

**gets**

|              api               |    request    |                           response                           |       description       |
| :----------------------------: | :-----------: | :----------------------------------------------------------: | :---------------------: |
|      /gets/getById/{{id}}      | Authorization | {'id', 'username', 'name', 'profile_photo', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'email', 'about_me', 'confirmed'} |   通过id查看用户信息    |
|         /gets/getList          | Authorization | {'id', 'username', 'name', 'profile_photo', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'email', 'about_me', 'confirmed'} |    查看所用用户信息     |

**posts**

|         api          |                           request                            |                           response                           |                         description                          |
| :------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| /posts/classifier | {'keywords', 'keyPhrases', 'category', 'code', 'message'} |                     {'code', 'message'}                      |     文献分类; 0:分类失败; 1:分类成功; 2:非铁道文献;     |
