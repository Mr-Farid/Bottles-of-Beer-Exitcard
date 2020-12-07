import pytest
import exercise

def test_case(capsys, num1, result):
  
  exercise.main()
  out, err = capsys.readouterr()

  assert out == ""
  assert err == ''