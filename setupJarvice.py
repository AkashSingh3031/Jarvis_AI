from cx_Freeze import *
includefiles = ['icon.ico']
excludes = []
packages = []
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = [
    ("DesktopShortcut", #Shortcut
     "DesktopFolder",   #Directory_
     "J.A.R.V.I.C.E__AI",  #Name
     "TARGETDIR", #Component_
     "[TARGETDIR]\Jarvice.exe", #Target
     None,  #Arguments
     None,  #Description
     None,  #Hotkey
     None,  #Icon
     None,  #IconIndex
     None,  #ShowCmd
     "TARGETDIR",  #WkDir
    )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {"data": msi_data}
setup(
    version = "0.1",
    description = "JARVICE AI System By ---- AKASH SINGH",
    author = "Akash Singh",
    name = "JARVICE AI",
    options = {'build_exe': {'include_files': includefiles}, 'bdist_msi': bdist_msi_options,},
    executables = [
        Executable(
            script = "Jarvice.py",
            base = base,
            icon = 'icon.ico',
        )
    ]
)