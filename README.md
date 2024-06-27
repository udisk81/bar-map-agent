通过替换BAR游戏的地图下载器pr-downloader，使用你指定的http代理加速下载游戏中的地图。

# 安装
1. 找到`BAR启动器/bin/pr-downloader`，把它重命名为`BAR启动器/bin/pr-downloader-old`。![4](https://github.com/udisk81/bar-map-agent/assets/172959786/ff45876f-b238-4344-9474-8720e0bdf116)

2. 下载这个[编译好的压缩包](https://github.com/udisk81/bar-map-agent/releases/download/0.1/exe.win-amd64-3.12.zip)到`BAR启动器/bin/`中，并且解压，这样BAR就会在下载地图的时候执行它。 ![2](https://github.com/udisk81/bar-map-agent/assets/172959786/0747a478-7672-4eb8-ad88-213a971cc450)

3. 然后打开proxy.ini，在其中设置你本地使用的http代理。 ![3](https://github.com/udisk81/bar-map-agent/assets/172959786/d99bfd90-38ae-4c13-a664-c18ad6820cea)

# 编译
如果你不想使用上面这个编译好的压缩包，你也可以用下面的命令自己编译。
```
python setup.py build
```

# 已知问题
1. 这个脚本无法在BAR游戏中显示下载进度，请使用任务管理器之类的工具查看下载速度。


