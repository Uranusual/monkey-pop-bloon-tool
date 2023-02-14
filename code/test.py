import win32process#进程模块
from win32con import PROCESS_ALL_ACCESS #Opencress 权限
import win32api#调用系统模块
import ctypes#C语言类型
import numpy
from win32gui import FindWindow#界面

def GetProcssID(address,bufflength):
    pid = ctypes.c_ulong() # 设置 pid 为 无符号单精度类型
    kernel32 = ctypes.windll.LoadLibrary("kernel32.dll")#加载动态链接库
    hwnd = FindWindow(None, "BloonsTD6")#获取窗口句柄
    hpid, pid = win32process.GetWindowThreadProcessId(hwnd)#获取窗口ID
    hProcess = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)#获取进程句柄
    ReadProcessMemory = kernel32.ReadProcessMemory
    addr = ctypes.c_ulong()
    ReadProcessMemory(int(hProcess), address, ctypes.byref(addr), bufflength, None)#读内存
    win32api.CloseHandle(hProcess)#关闭句柄
    return addr.value
    
def main():
    addr = GetProcssID(0x26B871F0, 6)
    # addr = GetProcssID(0xD0DF1C, 4)
    # ret = addr + 0x1C
    # ret2 = GetProcssID(ret, 4)
    # ret3 = ret2 + 0x28
    # ret4 = GetProcssID(ret3, 4)
    # ret5 = ret4 + 0x288
    # ret6 = GetProcssID(ret5, 4) # 传入偏移地址
    print ("回合数:%d" % addr)

if __name__ == '__main__':
    main()