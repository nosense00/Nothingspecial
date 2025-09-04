\
    # deploy_github.ps1 -- extract this package and prepare for manual git commit
    Param(
        [string]$ZipPath = "$env:USERPROFILE\Downloads\cursed_dark_site.zip",
        [string]$Target = "$env:USERPROFILE\Desktop\Nothingspecial"
    )
    if(Test-Path $Target){ Remove-Item $Target -Recurse -Force }
    New-Item -ItemType Directory -Path $Target | Out-Null
    Write-Host "Extracting $ZipPath -> $Target"
    Expand-Archive -Path $ZipPath -DestinationPath $Target -Force
    Write-Host "Files extracted. Now open Git Bash or PowerShell and run the usual git commands:"
    Write-Host "cd `"$Target`""
    Write-Host "git init   # if needed"
    Write-Host "git add ."
    Write-Host "git commit -m 'Add cursed dark site bundle'"
    Write-Host "git remote add origin https://github.com/nosense00/Nothingspecial.git"
    Write-Host "git branch -M main"
    Write-Host "git push -u origin main"
