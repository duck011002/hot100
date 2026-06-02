@echo off
cd /d "%~dp0"
"%USERPROFILE%\anaconda3\envs\excel\python.exe" -m streamlit run app.py
