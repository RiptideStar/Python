# Shorten URL with Python

## 重要概念

我们通过这个项目来学习加强对这些概念的理解:

1. 什么是API
2. 什么是 WEB API
3. 什么是 REST API
4. 为什么 API 非常重要? 
5. 什么是HTTP? 他最常用的两个请求方法(methods)是什么? 
6. HTTP 和 REST API 是什么关系? 
7. 什么是 Base64 Encoding? 主要用在什么地方?
8. 什么是 IP 地址? 和 DNS 什么关系?
9. 什么是 HTTP call (请求)的 headers, query parameters, payload (body)? 各有什么用？ 
10. 什么是 cookie ? 有什么用？ 
11. 什么是 html, xml 和 json? 他们之间是何关系?
   
* 程序接口(API)就像空气和水一样，已经渗透到你们生活学习中的每一个角落。比如你们的手机上所有的App包括微信都是通过API和后面的服务器进行对话。
* 每一个网址其实都是一个 REST API. REST API 是最常见应用最广泛的 WEB API。 
* 每一个网页的浏览, 都是一个HTTP请求. 每一个HTTP请求都是调用一个 REST API. 
* 离开了 WEB API, 你寸步难行: 不能网上购物，不能网上转账，不能发微信, 不能打车出行...

这些是这个项目会涉及到的一些重要概念。 大家在视频中，如果能够分别阐述自己对他们的理解，那就很好。👍👍
在这些项目中，加深对这些概念的理解，对你们将来的工作和学习会有很大的帮助。 
其实你们天天都在用这些东西. 只不过没有注意到他们时时刻刻发生在身边而已。 理解这些概念以后, 就会清晰知道每次浏览网页或者手机App操作背后发生了什么. 
-- 不仅知其然，还有知其所以然。


## 项目背景和使用场景
1. 大家很可能都遇到过: 要分享的网址很长, 放到社交媒体(微博,微信)上不方便, 怎么办? 
2. 有些程序或者网站需要提供缩短网址的服务, 比如 Twitter 和微博不能超过140个字符。 

比如: 你有这样一个网址: 太长，不好记, 不好分享 --
https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978

你肯定想把它缩短成一个好记的网址。
你有两种做法:
1. 到提供该服务的网站上去, 人工输入你的网址，然后让这个网站给你缩短你的网址。 
2. 调用服务网站提供都API, 自己编程的方法来实现。 
   
如果你要大量处理，或者在程序中来获取这个服务, 那编程来实现是你唯一的选择。 


## 调用第三方 WEB API 来实现缩短网址服务

搜索一下就发现有好多网站提供这样的服务。我们今天来一起探讨一下两个比较常见的网站 --
1. cutt.ly
2. bit.ly

### Cutt.ly 网站和API

1. 注册
2. 查阅API 文档: https://cutt.ly/api-documentation/cuttly-links-api
3. API Key: e77a2e10762f46d8be84d47974d4703310301
4. Python 分四步:
   1. 获取参数
   2. 构建REST API URL: `--- api_url:  https://cutt.ly/api/api.php?key=e77a2e10762f46d8be84d47974d4703310301&short=https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978&name=cs1948`
   3. Call REST API (GET) 缩短网址
   4. 分析返回值
   
Example:
```
python3 ex1-cutt.ly.py https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978 cs1948

--- 命令行参数: ['ex1-cutt.ly.py', 'https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978', 'cs1948']
--- api_url:  https://cutt.ly/api/api.php?key=e77a2e10762f46d8be84d47974d4703310301&short=https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978&name=cs1948
--- data:  {'status': 7, 'fullLink': 'https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978', 'date': '2021-03-07', 'shortLink': 'https://cutt.ly/cs1948', 'title': 'Example Domain'}
--- Shortened URL: https://cutt.ly/cs1948
```
