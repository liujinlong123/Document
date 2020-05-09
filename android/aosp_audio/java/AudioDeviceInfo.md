# AudioDeviceInfo阅读理解  

## AudioDeviceInfo类描述

1. AudioDeviceInfo类的创建  

    ```java
    private final AudioDevicePort mPort;

    AudioDeviceInfo(AudioDevicePort port) {
       mPort = port;
    }
    ```

    1). AudioDeviceInfo创建时，需要传入`AudioDevicePort`对象，AudioDeviceInfo的整体描述，都是围绕`AudioDevicePort`展开的。  
    2). 可以得到的设备描述包括：设备标识符(AudioHandle)、产品名称、AudioPort地址、AudioPort角色(Source or Sink)、采样率、通道掩码(位置)、索引通道掩码、通道数量(双声道...)、编码(Encoding)、设备类型等。

2. AudioDeviceInfo是对Audio Device的描述，类中定义了设备类型  

    ```java
    /**
     * A device type associated with an unknown or uninitialized device.
     */
    public static final int TYPE_UNKNOWN          = 0;
    /**
     * A device type describing the attached earphone speaker.
     */
    public static final int TYPE_BUILTIN_EARPIECE = 1;

    ........

    /**
     * A type-agnostic device used for communication with external audio systems
     */
    public static final int TYPE_BUS              = 21;
    /**
     * A device type describing a USB audio headset.
     */
    public static final int TYPE_USB_HEADSET       = 22;
    ```

    > Note: // TODO  need to supply， 设备类型与什么的对应关系？  

    AudioDeviceInfo还有一点比较重要的是，它定义了设备类型的对应关系

    ```java
    private static final SparseIntArray INT_TO_EXT_DEVICE_MAPPING;

    private static final SparseIntArray EXT_TO_INT_DEVICE_MAPPING;

    static {
        INT_TO_EXT_DEVICE_MAPPING = new SparseIntArray();
        INT_TO_EXT_DEVICE_MAPPING.put(AudioSystem.DEVICE_OUT_EARPIECE, TYPE_BUILTIN_EARPIECE);
        INT_TO_EXT_DEVICE_MAPPING.put(AudioSystem.DEVICE_OUT_SPEAKER, TYPE_BUILTIN_SPEAKER);
        INT_TO_EXT_DEVICE_MAPPING.put(AudioSystem.DEVICE_OUT_WIRED_HEADSET, TYPE_WIRED_HEADSET);

        ......

        EXT_TO_INT_DEVICE_MAPPING.put(TYPE_BUS, AudioSystem.DEVICE_OUT_BUS);
    }
    ```

## AudioDevicePort类描述(`AudioDeviceInfo`的构建对象)

### AudioPort类描述(`AudioDevicePort`继承自`AudioPort`)

1. 类的含义：`AudioPort`是对"音频节点"的抽象，该对象由framework创建，是一个隐藏类；`AudioPort`包含了对"音频节点"所支持的各种属性的描述：角色(Source or Sink)、名称、采样率(Sample)、通道掩码(Channel position mask)、索引通道掩码(Channel index mask)、编码(Encoding)、音频增益(Audio Gain)。

    > 该`AudioPort`可支持多种采样率、通道掩码设置、编码、音频增益。

2. 类的构建

3. 与AudioPort相关的类，`AudioHandle`和`AudioPortConfig`，在下面研究。
