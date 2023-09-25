# 批量生成图片的 webui 脚本

主文件是 generate-images.ipynb，里面有很多参数需要自己手动设置，具体去看文件里的注释

`webui_api_README.md` 是 webui 的 api 文档，直接复制过来放这里方便查询

`\apiOptions`文件夹下面是各个 api 的参数，只是本人机器里的，并不适合其它环境，如果想要看自己环境里的对应的参数，按文件名执行对应命令就行。

举例说明，如果想要看`api.get_options()`的返回结果，去`withWebUiApi.py`文件里，使用 `api.get_options()`方法，然后把返回的结果保存到`\apiOptions\get_options.txt`里就行了。方便自己以后查阅。
