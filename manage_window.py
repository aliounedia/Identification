import ctypes
from ctypes import wintypes

def set_DisableTaskmgr(value):
    import _winreg

    task_key = _winreg.CreateKey(
        _winreg.HKEY_CURRENT_USER,
        'Software\Microsoft\Windows\CurrentVersion\Policies\System')
    _winreg.SetValueEx(task_key, 'DisableTaskMgr', 0,
                       _winreg.REG_DWORD, value)
    _winreg.CloseKey(task_key)


    #





FindWindow = ctypes.windll.user32.FindWindowA
FindWindow.restype = wintypes.HWND
FindWindow.argtypes = [
    wintypes.LPCSTR, #lpClassName
    wintypes.LPCSTR, #lpWindowName
]

SetWindowPos = ctypes.windll.user32.SetWindowPos
SetWindowPos.restype = wintypes.BOOL
SetWindowPos.argtypes = [
    wintypes.HWND, #hWnd
    wintypes.HWND, #hWndInsertAfter
    ctypes.c_int,  #X
    ctypes.c_int,  #Y
    ctypes.c_int,  #cx
    ctypes.c_int,  #cy
    ctypes.c_uint, #uFlags
] 

TOGGLE_HIDEWINDOW = 0x80
TOGGLE_UNHIDEWINDOW = 0x40

def hide_taskbar():
    handleW1 = FindWindow(b"Shell_traywnd", b"")
    SetWindowPos(handleW1, 0, 0, 0, 0, 0,
                 TOGGLE_HIDEWINDOW)


def hide_Taskmgr():
    set_DisableTaskmgr(1)


def unhide_Taskmgr():
    set_DisableTaskmgr(0)


def unhide_taskbar():
    handleW1 = FindWindow(b"Shell_traywnd", b"")
    SetWindowPos(handleW1, 0, 0, 0, 0, 0,
                 TOGGLE_UNHIDEWINDOW)


##    
##if __name__=="__main__":
##    #set_DisableTaskmgr(1)
##    #hide_taskbar()
##    unhide_taskbar()
