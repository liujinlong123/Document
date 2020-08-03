# 每一个Android.mk开始都必须添加
LOCAL_PATH := ${call my-dir}

# 清除LOCAL_XXX 比如LOCAL_MODULE、LOCAL_SRC_FILES、LOCAL_STATIC_LIBRARIES
# 但是不会清除LOCAL_PATH
include ${CLEAR_VARS}

# 在进行Android NDK的开发当中有时想看看Android.mk文件当中某个变量的值，可以再Android.mk文件当中用warning语句实现该功能
# $(warning "the value of LOCAL_PATH is ${LOCAL_PATH}")

# 我们想要编译的动态库或者静态库的名字, 编译系统会自动添加前缀和后缀 libcommand-jni.so
LOCAL_MODULE := command-jni

# WARNING: Unsupported source file extensions in Android.mk for module command-jni
LOCAL_CPP_EXTENSION := .cxx .cpp .cc

# 头文件的搜索路径
LOCAL_C_INCLUDES := ${LOCAL_PATH}/native/include

# 源文件地址, 这里必须是c或者c++文件
LOCAL_SRC_FILES := ${LOCAL_PATH}/native/source/Command.cpp

# include $(CLEAR_VARS)
# LOCAL_MODULE := libPmAsiicEndec
# ifeq ($(TARGET_ARCH_ABI), arm64-v8a)
#    LOCAL_SRC_FILES := util/endec/libPmAsiicEndec_64.a
# else
#    LOCAL_SRC_FILES := util/endec/libPmAsiicEndec.a
# endif
# include $(PREBUILT_STATIC_LIBRARY)

# 生成可执行文件
# include ${BUIDL_EXECUTABLE}

# The last line helps the system tie everything together
# This script determines what to build, and how to do it.
include ${BUILD_SHARED_LIBRARY}

# 编译出静态库 .a文件
# include ${BUILD_STATIC_LIBRARY}