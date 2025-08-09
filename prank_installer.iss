[Setup]
AppName=Prank Toolbox
AppVersion=1.0
DefaultDirName={autopf}\Prank Toolbox
DefaultGroupName=Prank Toolbox
OutputBaseFilename=PrankToolbox_Installer
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Files]
Source: "dist\PrankToolbox.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\self_destruct_deluxe.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\infinite_update.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\useless_button.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\fake_bsod.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\dancing_icons.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\Prank Toolbox"; Filename: "{app}\PrankToolbox.exe"
Name: "{commondesktop}\Prank Toolbox"; Filename: "{app}\PrankToolbox.exe"

[Run]
Filename: "{app}\PrankToolbox.exe"; Description: "Launch Prank Toolbox"; Flags: nowait postinstall skipifsilent