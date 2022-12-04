# Creating a path for the files in the C: drive of the user
New-Item -Path "C:\" -Name "StuGrading" -ItemType "directory"

# Obtaining the executable from my github, and setting a path for the download
$url = "https://raw.githubusercontent.com/Dvaughn5/Student_Grading/master/App.py" # Download from here
$path = "C:\StuGrading\StudentGrading.py" # Store here which also acts as a target for the desktop shortcut

$icoUrl = "https://github.com/Dvaughn5/Student_Grading/blob/master/icons8-python-100.png"
$icoPath = "C:\StuGrading\icon.ico"
# Writing the request to download the executable 
Invoke-WebRequest -Uri $url -OutFile $path
Invoke-WebRequest -Uri $icoUrl -OutFile $icoPath

# Creating the desktop shortcut 
$ShortcutPath = "C:\Public\Desktop\Grading.lnk"

# Creating Windows Script Host Object
$WScript = New-Object -ComObject WScript.Shell

# Creating the actual shortcut
$shortcut = $WScript.CreateShortcut($ShortcutPath)

# Icon creation
$shortcut.IconLocation = "C:\StuGrading\icon.ico"

# Adding target path and saving
$shortcut.TargetPath = $path
$shortcut.Save()