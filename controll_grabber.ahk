#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

VarName = ED_SCREENSHOT_MODE

Update(val)
{
    IniWrite, %val%, config.ini, ed, mode
}

F1::Update(0)
F2::Update(1)
F3::Update(2)
F4::Update(4)

F6::
    RUN venv\Scripts\Activate.bat
    RUN venv\Scripts\python.exe main.py
Return

F8::
    val = ''
    IniRead val, config.ini, ed, mode, 0
    MsgBox %val%
Return