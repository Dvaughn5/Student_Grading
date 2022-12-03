# Creating a path for the files in the C: drive of the user
New-Item -Path "C:\" -Name "StuGrading" -ItemType "directory"

# Obtaining the executable from my github, and setting a path for the download
$url = "https://github.com/Dvaughn5/Student_Grading/blob/master/StudentGrading?raw=true" # Download from here
$path = "C:\StuGrading\StudentGrading.exe" # Store here 

# Writing the request to download the executable 
Invoke-WebRequest -Uri $url -OutFile $path

# Creating the desktop shortcut 
$ShortcutPath = "C:\Users\Desktop\Grading.lnk"

# Creating Windows Script Object
$WScript = New-Object -ComObject ("WScript.Shell")

# Creating the actual shortcut
$shortcut = $WScript.CreateShortcut($ShortcutPath)

# Adding target path and saving
$shortcut.TargetPath = $path
$shortcut.Save()