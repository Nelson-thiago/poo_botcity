$exclude = @("venv", "desktopBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desktopBot.zip" -Force