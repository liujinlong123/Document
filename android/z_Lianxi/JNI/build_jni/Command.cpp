#include "Command.h"
#include <iostream>

JNIEXPORT void JNICALL Java_Command_handleCommand
  (JNIEnv *env, jclass thiz, jbyteArray data)
{
    std::cout << "Hello In JNI" << std::endl;
}