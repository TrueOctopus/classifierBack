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
|           /users/confirm           |                {'email'}                |                     {'code', 'message'}                      | 发送验证邮件; 0:用户不存在; 1:验证邮件已发送; 2:用户已完成验证 |
| /users/confirm/{{email}}/{{token}} |                  None                   |                     {'code', 'message'}                      | 邮箱验证; 0:链接是无效的或已经超时; 1:验证完成; 2:用户已完成验证; -1:用户不存在 |
|       /users/changePassword        | {'email', 'oldPassword', 'newPassword'} |                     {'code', 'message'}                      | 修改密码; 0:用户不存在 1: 密码修改成功; -1: 修改失败; -2: 原密码错误 |
|       /users/forgetPassword        |                {'email'}                |                     {'code', 'message'}                      |           发送修改邮件; 0:用户不存在; 1:邮件已发送           |
|    /users/deleteUserById/{{id}}    |              Authorization              |                     {'code', 'message'}                      | 通过id删除用户; 0:删除失败; -2:权限不足; -3:-token失效请重新登录; -4:你不能删除你自己; -1:用户不存在; 1:删除成功 |
| /users/deleteUserByEmail/{{email}} |              Authorization              |                     {'code', 'message'}                      | 通过邮箱删除用户; 0:删除失败; -1:用户不存在; -2:权限不足; -3:token失效请重新登录; -4:你不能删除你自己; 1:删除成功 |
|      /users/changePermission       |     Authorization {'email', 'perm'}     |                     {'code', 'message'}                      | 修改用户权限; 1:修改成功; 0:权限不足; -1:用户不存在; -2:添加至数据库失败; -3:你不能修改管理员的权限; -4:token失效请重新登录 |
|        /users/confirmToken         |              Authorization              |                     {'code', 'message'}                      |   验证token是否有效; 0:token失效请重新登录; 1:token未失效    |

**gets**

|              api               |    request    |                           response                           |       description       |
| :----------------------------: | :-----------: | :----------------------------------------------------------: | :---------------------: |
|      /gets/getById/{{id}}      | Authorization | {'id', 'username', 'name', 'profile_photo', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'email', 'about_me', 'confirmed'} |   通过id查看用户信息    |
|         /gets/getList          | Authorization | {'id', 'username', 'name', 'profile_photo', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'email', 'about_me', 'confirmed'} |    查看所用用户信息     |
|   /gets/getImgs/{{imgName}}    |     None      |                             file                             |   通过图片名获取图片    |
|      /gets/getAllArtList       |     None      | {'id', 'art_type', 'title', ’image‘, 'body', 'timestamp', 'filename'} |    获取所有文章信息     |
|     /gets/getNoticeArtList     |     None      | {'id', 'art_type', 'title', ’image‘, 'body', 'timestamp', 'filename'} |    获取所用公告信息     |
|    /gets/getActivityArtList    |     None      | {'id', 'art_type', 'title', ’image‘, 'body', 'timestamp', 'filename'} |    获取所用活动信息     |
|    /gets/getArtById/{{id}}     |     None      | {'id', 'art_type', 'title', ’image‘, 'body', 'timestamp', 'filename'} |     通过id获取信息      |
|     /gets/getNoBodyArtList     |     None      | {'id', 'art_type', 'title', ’image‘, 'timestamp', 'filename'} | 获取所有文章信息 无正文 |
|  /gets/getNoBodyNoticeArtList  |     None      | {'id', 'art_type', 'title', ’image‘, 'timestamp', 'filename'} | 获取所用公告信息 无正文 |
| /gets/getNoBodyActivityArtList |     None      | {'id', 'art_type', 'title', ’image‘, 'timestamp', 'filename'} | 获取所用活动信息 无正文 |
| /gets/getNoBodyArtById/{{id}}  |     None      | {'id', 'art_type', 'title', ’image‘, 'timestamp', 'filename'} |  通过id获取信息 无正文  |
|  /gets/getArtImgs/{{imgName}}  |     None      |                             file                             | 通过图片名获取文章图片  |

**posts**

|         api          |                           request                            |                           response                           |                         description                          |
| :------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| /posts/uploadProfile | {'email', 'username', 'name', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'about_me', 'profile_photo'} |                     {'code', 'message'}                      |     更新用户资料; 0:用户不存在; 1:更新成功; -1:添加失败;     |
|    /posts/addUser    |              {'email', 'username', 'password'}               | {'code', 'message', 'id', 'username', 'name', 'profile_photo', 'sex', 'college', 'major', 'grade', 'student_num', 'phone_num', 'email', 'about_me', 'confirmed'} | 添加用户,默认邮箱验证完成; 0:添加失败; 1:添加成功,返回信息; -1:添加失败，信息不全 |
|   /posts/uploadImg   |                             None                             |                     {'code', 'message'}                      |       上传图片；0:图片已存在; 1:上传成功; -1:类型错误        |
