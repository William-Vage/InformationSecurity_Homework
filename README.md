# InformationSecurity_Homework

Jiaxing Qiu branch

## 代码

```
src/
 - datafilter.py: czy的数据预处理脚本，我稍微改了一下，让它能读多个dataset
 - parseflag.py: 从批量HTML数据中解析出第四题flag的自动化脚本
```

## Overleaf

[Here](https://cn.overleaf.com/1281747996zntnkfyxtgcj)

## 下面是攻击溯源的一些临时记录

## 11

只有一条流量数据，来自`Apr 22, 2023 22:13:04.804663000 中国标准时间`，无法分析

## 12

从`Apr 23, 2023 21:10:44.348292000 中国标准时间`持续到了`Apr 23, 2023 21:13:58.911153000 中国标准时间`，攻击者大量访问了web服务经常会泄露信息的路径，如`/.admin`、`/.access`、`/.AppleDB`、`/.git`等，扫描记录一共9086条，考虑是该同学利用`dirsearch`或类似工具对网站进行了目录扫描。

...

```
"http": {"POST /register.php HTTP/1.1\\r\\n": {"_ws.expert": {"http.chat": "", "_ws.expert.message": "POST /register.php HTTP/1.1\\r\\n", "_ws.expert.severity": "2097152", "_ws.expert.group": "33554432"}, "http.request.method": "POST", "http.request.uri": "/register.php", "http.request.version": "HTTP/1.1"}, "http.host": "10.0.0.4", "http.request.line": "Upgrade-Insecure-Requests: 1\r\n", "http.user_agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "http.accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "http.accept_language": "en-US,en;q=0.5", "http.accept_encoding": "gzip, deflate", "http.content_type": "application/x-www-form-urlencoded", "http.content_length_header": "67", "http.content_length_header_tree": {"http.content_length": "67"}, "http.connection": "close", "http.referer": "http://10.0.0.4/register.php", "http.cookie": "PHPSESSID=lhvtnq625or51joujrrvd872e7", "http.cookie_tree": {"http.cookie_pair": "PHPSESSID=lhvtnq625or51joujrrvd872e7"}, "\\r\\n": "", "http.request.full_uri": "http://10.0.0.4/register.php", "http.request": "1", "http.request_number": "1", "http.response_in": "4195680", "http.file_data": "email=fuboat%40outlook.com&username=%27%2Baba%2B%27&password=123456"}, "urlencoded-form": {"Form item: \"email\" = \"fuboat@outlook.com\"": {"urlencoded-form.key": "email", "urlencoded-form.value": "fuboat@outlook.com"}, "Form item: \"username\" = \"'+aba+'\"": {"urlencoded-form.key": "username", "urlencoded-form.value": "'+aba+'"}, "Form item: \"password\" = \"123456\"": {"urlencoded-form.key": "password", "urlencoded-form.value": "123456"}}}}}
```

，并且紧接着就有一次`http://10.0.0.4/login.php`的访问，其`302`跳转至`http://10.0.0.4/index.php`。

```
"http": {"HTTP/1.1 200 OK\\r\\n": {"_ws.expert": {"http.chat": "", "_ws.expert.message": "HTTP/1.1 200 OK\\r\\n", "_ws.expert.severity": "2097152", "_ws.expert.group": "33554432"}, "http.response.version": "HTTP/1.1", "http.response.code": "200", "http.response.code.desc": "OK", "http.response.phrase": "OK"}, "http.date": "Sun, 23 Apr 2023 14:23:26 GMT", "http.response.line": "Content-Type: text/html\r\n", "http.server": "Apache/2.4.7 (Ubuntu)", "http.cache_control": "no-store, no-cache, must-revalidate, post-check=0, pre-check=0", "http.content_encoding": "gzip", "http.content_length_header": "792", "http.content_length_header_tree": {"http.content_length": "792"}, "http.connection": "close", "http.content_type": "text/html", "\\r\\n": "", "http.response": "1", "http.response_number": "1", "http.time": "0.007606000", "http.request_in": "4196758", "http.response_for.uri": "http://10.0.0.4/index.php", "Content-encoded entity body (gzip): 792 bytes -> 1840 bytes": "", "http.file_data": "<!doctype html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"utf-8\">\n    <title>������������</title>\n    <meta http-equiv=\"cleartype\" content=\"on\">\n    <meta name=\"MobileOptimized\" content=\"320\">\n    <meta name=\"HandheldFriendly\" content=\"True\">\n    <meta name=\"apple-mobile-web-app-capable\" content=\"yes\">\n    <meta name=\"viewport\" content=\"width=device-width,height=device-height,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no\" />\n    <link rel=\"stylesheet\" href=\"./stylesheets/index.css\">\n    <link rel=\"stylesheet\" href=\"./stylesheets/flaticon.css\" />\n    <link rel='stylesheet' href='./stylesheets/style.css' />\n  </head>\n  <body>\n\n    <nav id=\"menu\">\n      <div>\n        <div class=\"img-div\">\n          <div class=\"user-img\"><img src=\"./uploads/a.jpeg\"></div>\n          <span class=\"user-name\">\n            0          </span>\n        </div>\n      </div>\n    </nav>\n\n    <main id=\"panel\">\n      <header>\n        <header class=\"pass-header\">\n          <span class=\"pass-header-title\">CTF</span>\n          <div id=\"back-menu\">\n            <div class=\"glyph-icon flaticon-back\">\n            </div>\n          </div>\n          <div id=\"userinfo-wraps\">\n            <div class=\"glyph-icon flaticon-settings-1\">\n            </div>\n          </div>\n      </header>\n      <img style=\"max-width:100%;max-height::100%;overflow:hidden;\" src=\"images/674407.jpg\" alt=\"\">\n      </header>\n    </main>\n    <script src=\"./javascripts/slideout/slideout.min.js\"></script>\n    <script>\n      var slideout = new Slideout({\n        'panel': document.getElementById('panel'),\n        'menu': document.getElementById('menu'),\n        'padding': 256,\n        'tolerance': 70\n      });\n\n      document.querySelector('#back-menu').addEventListener('click', function() {\n        slideout.toggle();\n      });\n    </script>\n\n  </body>\n</html>"}, "data-text-lines": {"<!doctype html>\\n": "", "<html lang=\"en\">\\n": "", "  <head>\\n": "", "    <meta charset=\"utf-8\">\\n": "", "    <title>我的应用</title>\\n": "", "    <meta http-equiv=\"cleartype\" content=\"on\">\\n": "", "    <meta name=\"MobileOptimized\" content=\"320\">\\n": "", "    <meta name=\"HandheldFriendly\" content=\"True\">\\n": "", "    <meta name=\"apple-mobile-web-app-capable\" content=\"yes\">\\n": "", "    <meta name=\"viewport\" content=\"width=device-width,height=device-height,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no\" />\\n": "", "    <link rel=\"stylesheet\" href=\"./stylesheets/index.css\">\\n": "", "    <link rel=\"stylesheet\" href=\"./stylesheets/flaticon.css\" />\\n": "", "    <link rel='stylesheet' href='./stylesheets/style.css' />\\n": "", "  </head>\\n": "", "  <body>\\n": "", "\\n": "", "    <nav id=\"menu\">\\n": "", "      <div>\\n": "", "        <div class=\"img-div\">\\n": "", "          <div class=\"user-img\"><img src=\"./uploads/a.jpeg\"></div>\\n": "", "          <span class=\"user-name\">\\n": "", "            0          </span>\\n": "", "        </div>\\n": "", "      </div>\\n": "", "    </nav>\\n": "", "    <main id=\"panel\">\\n": "", "      <header>\\n": "", "        <header class=\"pass-header\">\\n": "", "          <span class=\"pass-header-title\">CTF</span>\\n": "", "          <div id=\"back-menu\">\\n": "", "            <div class=\"glyph-icon flaticon-back\">\\n": "", "            </div>\\n": "", "          </div>\\n": "", "          <div id=\"userinfo-wraps\">\\n": "", "            <div class=\"glyph-icon flaticon-settings-1\">\\n": "", "      </header>\\n": "", "      <img style=\"max-width:100%;max-height::100%;overflow:hidden;\" src=\"images/674407.jpg\" alt=\"\">\\n": "", "    </main>\\n": "", "    <script src=\"./javascripts/slideout/slideout.min.js\"></script>\\n": "", "    <script>\\n": "", "      var slideout = new Slideout({\\n": "", "        'panel': document.getElementById('panel'),\\n": "", "        'menu': document.getElementById('menu'),\\n": "", "        'padding': 256,\\n": "", "        'tolerance': 70\\n": "", "      });\\n": "", "      document.querySelector('#back-menu').addEventListener('click', function() {\\n": "", "        slideout.toggle();\\n": "", "    </script>\\n": "", "  </body>\\n": "", "</html>": ""}}}}
```

可以看出，`Apr 23, 2023 22:22:36.443178000 中国标准时间`的时候，该同学已经开始尝试使用`'+aba+'`进行SQL注入攻击。可惜，MySQL没法使用`+`号拼接字符串，所以该同学没法得到他想要的回显。从服务器返回的`index.php`的html可以看出，回显的结果是`0`，并不是该同学输入的`+aba+`，但这说明SQL注入是可行的。

果不其然，该同学紧接着又进行了数十次类似的攻击尝试，使用了`abc'+'abc'+'abc`、`'||'abc'||'`、`'+'0'+ASCII(SUBSTR((SELECT+*+FROM+FLAG),1,1))+'`、`'+'0'+ASCII(SUBSTRING((SELECT * FROM FLAG)FROM 1 FOR 1))+'`、`'+CAST(ASCII(SUBSTR((SELECT * FROM flag) FROM 1 FOR 1)) AS CHAR)+'`等字符串作为用户名进行SQL注入攻击。有趣的是，有那么几次攻击尝试中，该同学尝试更换了`ASCII`和`SUBSTR`的大小写进行攻击，意义不明。

从`Apr 23, 2023 23:53:45.585005000 中国标准时间`开始，攻击者使用`0'+ascii(substr((select * from flag) from 1 for 1))+'0`成功拿到了flag第一位的ASCII码。之后在很短时间内，直到`Apr 23, 2023 23:54:57.027632000 中国标准时间`，攻击者一共尝试了45次（即循环至``0'+ascii(substr((select * from flag) from 45 for 1))+'0``），之后就没有攻击记录了，说明该同学已经成功获取了flag。

根据服务器返回的html数据，我们也编写脚本自动解码出了该同学在`Apr 23, 2023 23:53:45.585005000 中国标准时间`时的第四题flag：`7498e38f-35de-4e93-b28a-5c36cfc9241f`。

## 17

只有12条流量数据`Apr 14, 2023 20:13:31`

## 25

## 26

一开始只是普通登录访问。

`Apr 22, 2023 20:43:10.617554000` - `Apr 22, 2023 20:44:07.607579000 中国标准时间` 目录扫描，尝试访问`/wp-login/`、`/wwwroot.tgz`、`/~admin`等大量不存在的url。

然后也只是普通登录访问。

`Apr 22, 2023 21:13:26.970588000 中国标准时间` - `Apr 22, 2023 21:38:05.767854000 中国标准时间` 尝试拿flag

`Apr 22, 2023 21:20:17.601316000 中国标准时间` 时的flag：`cf52e302-5214-4fd8-a643-a6854acf6231`

## 28
