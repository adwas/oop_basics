
To run the tests execute:
python3 -m pytest

To see more detailed execution add -v 
python3 -m pytest -v

To narrow execution use keyword switch -k:
 python3 -m pytest -v -k TestTemperatureCase

python3 -m pytest -v -k test_point_class_point_constructor tests/a003_gfx2d_test.py 
