荒野回放 WebGL 构建包使用说明
==============================

不要直接双击 index.html，也不要只拷贝 Build 目录。整个文件夹原样放到 HTTP 服务器上访问。

目录必须包含：
- index.html
- Build/
- StreamingAssets/
- TemplateData/

访问方式：
- 包内回放：http://服务器/（读 StreamingAssets/replay.txt）
- 远程回放：http://服务器/?replay=http://回放地址/replay.txt
- 相对回放：http://服务器/?replay=/StreamingAssets/replay.txt

回放加载不了时：
- 页面用域名打开、进度条卡住 → 浏览器缓存问题。先清该站点数据或换无痕；本包已关 dataCaching，重发新包后自然不再复发。
- 页面能开但回放不启动 → F12 Console 看 CORS 报错（Access-Control-Allow-Origin），目标回放服务器需放行你的页面 origin。
- 页面和回放都走 http:// → 已开启 insecureHttpOption=AlwaysAllowed，无需额外配置。
