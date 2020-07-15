# AudioAttributes阅读理解

>Author: Aiden&#160;&#160;&#160;&#160;&#160;&#160;&#160;Date: 2020.05.11

## AudioAttributes

### AudioAttributes文档参考

1. 参考官方源码[AudioAttributes](https://developer.android.google.cn/reference/android/media/AudioAttributes?hl=en)  

2. 参考AOSP官网上的描述[Audio Attribute](https://source.android.google.cn/devices/audio/attributes#using)

### AudioAttributes类描述  

1. 含义：该类是对音频流属性的抽象，属性`CONTENT_TYPE`标识当前播放内容，一个`CONTENT_TYPE`对应多个`USAGE`，属性`USAGE`标识当前音频的用途，`FLAG`属性是添加到音频流上的效果属性。

    > Note: 关于`USAGE`的具体应用还需要继续深入， 另外Android 9 添加了`Context`属性，需要后面查看。
