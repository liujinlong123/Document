# Wi-Fi Direct (peer-to-peer or P2P) overview

>Author: Aiden&#160;&#160;&#160;&#160;&#160;&#160;&#160;Date: 2020.05.07

## 基本使用方法  

1. 官方文档地址: [WIFI Direct](https://developer.android.google.cn/guide/topics/connectivity/wifip2p)
2. 基本使用方法参考官方文档内容  

## 构建时注意事项  

1. 主动创建GroupOwner，其它周边设备主动添加到GroupOwner中；其它设备称为GroupClient  

    ```java
    // 创建GroupOwner
    public void createGroupOwner() {
        manager.createGroup(channel, new WifiP2pManager.ActionListener() {
            @Override
            public void onSuccess() {
                Log.v(TAG, " ------> 创建GO成功");
            }

            @Override
            public void onFailure(int reason) {
                Log.v(TAG, " ------> 创建GO失败 reason: " + reason);
            }
        });
    }
    ```

2. 作为GroupOwner的设备，是不知道GroupClient的IP地址的，但是GroupClient可以获得GroupOwner的地址，有两种方式可以获得：  
1). GroupClient通过注册广播 `WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION` 来得到`WifiP2pInfo`对象，通过 `WifiP2pInfo.groupOwnerAddress.hostAddress` 获得IP地址  

    ```java
    // Wi-Fi Direct 连接状态更新监听
    case WifiP2pManager.WIFI_P2P_CONNECTION_CHANGED_ACTION:
        // WiFiP2pInfo - 通过该对象可以获得GroupOwner的IP地址
        WifiP2pInfo wifiP2pInfo = intent.getParcelableExt(WifiP2pManager.EXTRA_WIFI_P2P_INFO);

        // NetworkInfo - 当前WIFI Direct的连接状态
        NetworkInfo networkInfo = intent.getParcelableExt(WifiP2pManager.EXTRA_NETWORK_INFO);

        // WifiP2pGroup - 该对象包含Group的信息, 一个GroupOwner和多个GroupClient
        WifiP2pGroup wifiP2pGroup = intent.getParcelableExt(WifiP2pManager.EXTRA_WIFI_P2P_GROUP)

        shareVM.getWifiP2pInfo().setValue(wifiP2pInfo);
        shareVM.getNetworkInfo().setValue(networkInfo);
        shareVM.getWifiP2pGroup().setValue(wifiP2pGroup)

        Log.v(TAG, "wifiP2pInfo ------> " + wifiP2pInfo);
        Log.v(TAG, "networkInfo ------> " + networkInfo);
        Log.v(TAG, "wifiP2pGroup ------> " + wifiP2pGroup)
        break;
    ```

    获得IP地址

    ```kotlin
    // WifiP2pInfo 对象通过上面广播获得
    wifiP2pInfo.groupOwnerAddress.hostAddress
    ```

    2). 通过接口回调来获得IP：`WifiP2pManager.ConnectionInfoListener`  

    ```java
    manager.requestConnectionInfo(channel, new WifiP2pManager.  ConnectionInfoListener() {
                @Override
                public void onConnectionInfoAvailable(WifiP2pInfo info) {

                }
            });
    ```

    >Note: 需要在收到连接成功广播后再调用上述方法，否则可能会出现`WifiP2pInfo`为空的情况  

3. GroupClient与GroupOwner建立连接之后，使用Socket进行通信
