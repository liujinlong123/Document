import java.util.ArrayList;
import java.util.List;

// 2020-07-14 22:18:50.572 3093-3093/com.shanxiuni.cp210a V/DataUtil: 命令49 ------> 
// [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 32, 4, 20, 35, 82, 82, 82, 82, 82, 82, 82, 82, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 67, 81, -126, 51, 6]
// 2020-07-14 22:18:50.574 3093-3093/com.shanxiuni.cp210a V/TEST:  打印版本 ------> 0.0
// 2020-07-14 22:18:51.118 3093-3093/com.shanxiuni.cp210a V/DataUtil: 命令4c ------> 
// [-1, -1, -1, 91, 41, 4, -122, 24, 9, -122, 24, 9, -122, 24, 9, 0, 0, 0, 0, 33, 1, 1, 0, 0, 0, 16, 40, 6, -37]

public class Command {
    public static final String TAG = "Command";

    static {
        System.loadLibrary("native");
    }

    public static native void handleCommand(byte[] data);

    public static void main(String[] args) {
        // 命令初始化
        byte[] data = {
            -1, -1, -1, 91, 41, 4, -122, 24, 9, -122, 24, 9, -122, 24, 9, 0, 0, 0, 0, 33, 1, 1, 0, 0, 0, 16, 40, 6, -37
        };

        List<Byte> list = new ArrayList<>();
        for (int i = 0; i < data.length; i++) {
            list.add(data[i]);
        }

        byte[] copyData = toArray(list);
        handleCommand(copyData);
    }

    /**
     * 转换List<Byte>为byte[]
     * @param list
     * @return
     */
    private static byte[] toArray(List<Byte> list) {
        byte[] data = new byte[list.size()];
        for (int i = 0; i < list.size(); i++) {
            data[i] = list.get(i);
        }

        return data;
    }
}