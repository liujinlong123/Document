#include "Command.h"
#include <iostream>

using namespace std;
JNIEXPORT void JNICALL Java_Command_handleCommand
  (JNIEnv *env, jclass thiz, jbyteArray data)
{
    // 定义
    int i, length;
    jbyte* pointer;

    pointer = env->GetByteArrayElements(data, NULL);
    length = env->GetArrayLength(data);

    for (i = 0; i < length; i++) {
        cout << (int) pointer[i] << "  ";
    }
    cout << endl;

    // deinit
    env->ReleaseByteArrayElements(data, pointer, 0);

}