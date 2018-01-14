@setlocal
@set PYTHONPATH=pylint;%PYTHONPATH%
call pylint pylint\samples\sample.py --load-plugins two-instance-variables,no-else
@endlocal
