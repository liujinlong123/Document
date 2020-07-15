# AudioFormat 阅读理解

>Author: Aiden&#160;&#160;&#160;&#160;&#160;&#160;&#160;Date: 2020.05.09  

## 前提  

1. 阅读官方文档[AudioFormat](https://developer.android.google.cn/reference/kotlin/android/media/AudioFormat?hl=en)  
2. 参考源码部分  

## 理解(相关概念Sample Rate、Encoding、Channel Mask)  

1. AudioFormat主要围绕Audio Frame(音频帧)展开，举例：  
    >  如果Channel = stereo(双声道), Encoding(位深) = 16bit, 那么1个Audio Frame = 2个Sample，两个Sample分别输出到两个Channel，每一个Sample的Encoding为16bit，1个Audio Frame = 4byte。  
    >> For linear PCM, an audio frame consists of a set of samples captured at the same time, whose count and channel association are given by the channel mask, and whose sample contents are specified by the encoding. For example, a stereo 16 bit PCM frame consists of two 16 bit linear PCM samples, with a frame size of 4 bytes.

2. Audio Frame中Sample的排列顺序
    > 假设1个Audio Frame由2个Sample(Sample0, Sample1)构成，此时双声道(Stereo)输出，Sample0应该输出到哪一个Channel，Sample1应该输出到哪一个Channel(可能存在Channel0、Channel1、Channel2、Channel3...)，由Channel Mask来确定。

3. Channel Mask(声道掩码) 分为Channel position masks和Channel index masks  
    1). Channel position masks(位置声道掩码)
    > 举例：假设Channel position mask = CHANNEL_OUT_QUAD(前左、前右、后左、后右)。 CHANNEL_OUT_QUAD(四声道输出) = (CHANNEL_OUT_FRONT_LEFT | CHANNEL_OUT_FRONT_RIGHT | CHANNEL_OUT_BACK_LEFT | CHANNEL_OUT_BACK_RIGHT) = 1100 1100(每一个bit1位对应后右、后左、前右、前左)  
    对应1个Audio Frame = Sample0、Sample1、Sample2、Sample3，按照lsb -> msb(小端有效位 -> 大端有效位，从右往左)的顺序，Sample0输出到CHANNEL_OUT_FRONT_LEFT(前左)、Sample1输出到CHANNEL_OUT_FRONT_RIGHT(前右)、Sample2输出到CHANNEL_OUT_BACK_LEFT(后左)、Sample3输出到CHANNEL_OUT_BACK_RIGHT(后右)。
    >> For a channel position mask, each allowed channel position corresponds to a bit in the channel mask. If that channel position is present in the audio frame, that bit is set, otherwise it is zero. The order of the bits (from lsb to msb) corresponds to the order of that position's sample in the audio frame.

    2).Channel position masks存在的问题
    > Here's an example where channel index masks address this confusion: dealing with a 4 channel USB device. Using a position mask, and based on the channel count, this would be a CHANNEL_OUT_QUAD device, but really one is only interested in channel 0 through channel 3. The USB device would then have the following individual bit channel masks: CHANNEL_OUT_FRONT_LEFT, CHANNEL_OUT_FRONT_RIGHT, CHANNEL_OUT_BACK_LEFT and CHANNEL_OUT_BACK_RIGHT. But which is channel 0 and which is channel 3?
    >> 对于1)中，Sample0、Sample1、Sample2、Sample3对应输出到前左、前右、后左、后右，但是并不是对应输出到Channel0、Channel1、Channel2、Channel3...，Channel position mask(前左)与Channel index(Channel 0..3..)的对应关系由人为指定(可能是底层指定)或音频系统指定。

    3).Channel index masks(索引声道掩码)
    > 举例：对于一个拥有4个声道的USB的设备来说, Channel index mask = 0xF = 1111(lsb -> msb 对应Channel0、Channel1、Channel2、Channel3)，如果我们想选择Channel0和Channel2双声道来播放音频，则Channel index mask = 0x5 = 0101
    >> For a channel index mask, each channel number is represented as a bit in the mask, from the lsb (channel 0) upwards to the msb, numerically this bit value is 1 << channelNumber. A set bit indicates that channel is present in the audio frame, otherwise it is cleared. The order of the bits also correspond to that channel number's sample order in the audio frame.  
    For the previous 4 channel USB device example, the device would have a channel index mask 0xF. Suppose we wanted to select only the first and the third channels; this would correspond to a channel index mask 0x5 (the first and third bits set). If an AudioTrack uses this channel index mask, the audio frame would consist of two samples, the first sample of each frame routed to channel 0, and the second sample of each frame routed to channel 2. The canonical channel index masks by channel count are given by the formula (1 << channelCount) - 1.
