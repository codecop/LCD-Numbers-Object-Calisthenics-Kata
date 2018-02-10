@rem run pytest for all rules' unit tests.
@FOR /F "usebackq delims==" %%i IN (`dir /b /s test\unittest_*.py`) DO @call pytest "%%i"
