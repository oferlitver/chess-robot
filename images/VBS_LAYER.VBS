Dim wshShell
Dim fso
Dim loc
Dim cmd

Sub python_test()
	python = "C:\Intelitek\SCORBASE\Projects\ER4u\chess_ofer_ori\test.py"
	Set wshShell = CreateObject("WScript.Shell")
	wshShell.Run python
End Sub

Function white_origin()
	Set objFSO = CreateObject("Scripting.FileSystemObject")
	Set objFile = objFSO.OpenTextFile("C:\Intelitek\SCORBASE\Projects\ER4u\chess_ofer_ori\file_wo.txt", 1)
	white_origin = objFile.ReadAll
End Function

Function white_destination()
	Set objFSO = CreateObject("Scripting.FileSystemObject")
	Set objFile = objFSO.OpenTextFile("C:\Intelitek\SCORBASE\Projects\ER4u\chess_ofer_ori\file_wd.txt", 1)
	white_destination = objFile.ReadAll
End Function

Function black_origin()
	Set objFSO = CreateObject("Scripting.FileSystemObject")
	Set objFile = objFSO.OpenTextFile("C:\Intelitek\SCORBASE\Projects\ER4u\chess_ofer_ori\file_bo.txt", 1)
	black_origin = objFile.ReadAll
End Function

Function black_destination()
	Set objFSO = CreateObject("Scripting.FileSystemObject")
	Set objFile = objFSO.OpenTextFile("C:\Intelitek\SCORBASE\Projects\ER4u\chess_ofer_ori\file_bd.txt", 1)
	black_destination = objFile.ReadAll
End Function


'Set fso = CreateObject("C:\Intelitek\SCORBASE\Projects\ER4u\chess_ofer_ori\Python\test.py")
'loc = fso.GetAbsolutePathName(".")
'WScript.Echo loc

'~ cmd = "%ComSpec% /k C:\Languages\Python\python.exe " + loc + "\test.py"
'cmd = "C:\Languages\Python\python.exe " + loc + "\test.py"

'WScript.Echo cmd