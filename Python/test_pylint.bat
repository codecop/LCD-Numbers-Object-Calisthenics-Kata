@setlocal
@set PYTHONPATH=pylint;%PYTHONPATH%
call pylint --rcfile objectcalisthenics.pylintrc pylint\samples\sample.py
@rem ---jobs 4 --load-plugins two-instance-variables,no-else
@endlocal
