#include "Command.h"

JNIEXPORT jstring JNICALL Java_Command_stringFromJni
  (JNIEnv* env, jclass thiz, jstring command)
{
    return env->NewStringUTF("Hello World");
}