@setlocal
@set PYTHONPATH=pylint;%PYTHONPATH%
call pylint lcd --load-plugins NoElse
@endlocal
