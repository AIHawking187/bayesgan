@echo off
echo Creating conda environment with Python 3.5...
conda create -n bgan35 python=3.5 -y

echo Activating environment...
call conda activate bgan35

echo Installing TensorFlow 1.0.0 and required libraries...
pip install tensorflow==1.0.0
pip install scikit-learn==0.17.1 matplotlib==2.0.2 numpy==1.13.1 pillow==4.2.1 protobuf==3.3.0

echo Fixing Python 2 print statements to Python 3...

for /r %%i in (*.py) do (
    powershell -Command "(Get-Content \"%%i\") -replace 'print \"', 'print(\"' | ForEach-Object {$_ -replace '\"$', '\")'} | Set-Content \"%%i\""
)

echo Done! Your environment and files are ready!
pause
