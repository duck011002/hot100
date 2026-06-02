$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = Join-Path $env:USERPROFILE "anaconda3\envs\excel\python.exe"
Set-Location $root
& $python -m streamlit run app.py
