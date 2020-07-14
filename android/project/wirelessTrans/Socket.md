# Socket的使用  

>Author: 刘金龙&#160;&#160;&#160;&#160;&#160;&#160;&#160;Date: 2020.05.07

## Server端监听指定端口

1. 参考官方文档[蓝牙服务端Socket](https://developer.android.google.cn/guide/topics/connectivity/bluetooth#ManageAConnection)  
2. 基本使用(可以参考[java版本](https://developer.android.google.cn/guide/topics/connectivity/bluetooth#java))

    ``` kotlin
    // 定义监听端口
    const val PORT = 8898

    private inner class AcceptThread : Thread() {

        private val mmServerSocket: ServerSocket? by lazy (LazyThreadSafetyMode.NONE) {
            ServerSocket(PORT)
        }

        override fun run() {
            // Keep listening until exception occurs.
            var shouldLoop = true
            while (shouldLoop) {
                val socket: Socket? = try {
                    mmServerSocket?.accept()
                } catch (e: IOException) {
                    Log.e(TAG, "Socket's accept() method failed", e)
                    shouldLoop = false
                    null
                }

                socket?.also {
                    manageMyConnectedSocket(it)

                    // 如果想要和多台设备建立连接，则不能关闭mmServerSocket，该循环应该继续监听PORT
                    mmServerSocket?.close()
                    shouldLoop = false
                }
            }
        }

        // Closes the connect socket and causes the thread to finish.
        fun cancel() {
            try {
                mmServerSocket?.close()
            } catch (e: IOException) {
                Log.e(TAG, "Could not close the connect socket", e)
            }
        }
    }
    ```

## Client端连接到指定Server  

1. 参考官方文档[WIFI Direct传输数据](https://developer.android.google.cn/guide/topics/connectivity/wifip2p#transfer)  
2. 基本使用([可以参考Java版本](https://developer.android.google.cn/guide/topics/connectivity/wifip2p#java))  

    ```kotlin
    val context = applicationContext
    val host: String
    val port: Int
    val len: Int
    val socket = Socket()
    val buf = ByteArray(1024)
    ...
    try {
        /**
         * Create a client socket with the host,
         * port, and timeout information.
         * 拿到IP和PORT后，即可建立Socket连接
         */
        socket.bind(null)
        socket.connect((InetSocketAddress(host, port)), 500)

        ......
        /**
         * 下面是已经建立好连接后的操作
         */
        val outputStream = socket.getOutputStream()

        outputStream.close()
        ......

    } catch (e: FileNotFoundException) {
        //catch logic
    } catch (e: IOException) {
        //catch logic
    } finally {
        /**
         * Clean up any open sockets when done
         * transferring or if an exception occurred.
         */
        socket.takeIf { it.isConnected }?.apply {
            close()
        }
    }
    ```

    >Note: 如果Server端(指定host)没有监听上述PORT，则Socket连接不能建立成功  

## 管理Socket连接(使用InputStream和OutputStream传输数据)

1. 参考官方文档[Manage a connection](https://developer.android.google.cn/guide/topics/connectivity/bluetooth#ManageAConnection)  
2. 基本用法(可以参考[Java版本](https://developer.android.google.cn/guide/topics/connectivity/bluetooth#java))

    ```kotlin
    private const val TAG = "MY_APP_DEBUG_TAG"

    // Defines several constants used when transmitting messages between the
    // service and the UI.
    const val MESSAGE_READ: Int = 0
    const val MESSAGE_WRITE: Int = 1
    const val MESSAGE_TOAST: Int = 2
    // ... (Add other message types here as needed.)

    class MySocketService(
            // handler that gets info from Socket service
            private val handler: Handler) {

        private inner class ConnectedThread(private val mmSocket: Socket) : Thread() {

            private val mmInStream: InputStream = mmSocket.inputStream
            private val mmOutStream: OutputStream = mmSocket.outputStream
            private val mmBuffer: ByteArray = ByteArray(1024) // mmBuffer store for the stream

            override fun run() {
                var numBytes: Int // bytes returned from read()

                // Keep listening to the InputStream until an exception occurs.
                while (true) {
                    // Read from the InputStream.
                    numBytes = try {
                        mmInStream.read(mmBuffer)
                    } catch (e: IOException) {
                        Log.d(TAG, "Input stream was disconnected", e)
                        break
                    }

                    // Send the obtained bytes to the UI activity.
                    val readMsg = handler.obtainMessage(
                            MESSAGE_READ, numBytes, -1,
                            mmBuffer)
                    readMsg.sendToTarget()
                }
            }

            // Call this from the main activity to send data to the remote device.
            fun write(bytes: ByteArray) {
                try {
                    mmOutStream.write(bytes)
                } catch (e: IOException) {
                    Log.e(TAG, "Error occurred when sending data", e)

                    // Send a failure message back to the activity.
                    val writeErrorMsg = handler.obtainMessage(MESSAGE_TOAST)
                    val bundle = Bundle().apply {
                        putString("toast", "Couldn't send data to the other device")
                    }
                    writeErrorMsg.data = bundle
                    handler.sendMessage(writeErrorMsg)
                    return
                }

                // Share the sent message with the UI activity.
                val writtenMsg = handler.obtainMessage(
                        MESSAGE_WRITE, -1, -1, mmBuffer)
                writtenMsg.sendToTarget()
            }

            // Call this method from the main activity to shut down the connection.
            fun cancel() {
                try {
                    mmSocket.close()
                } catch (e: IOException) {
                    Log.e(TAG, "Could not close the connect socket", e)
                }
            }
        }
    }
    ```

    >Note: 关闭InputStream或OutputStream将导致Socket被关闭  
