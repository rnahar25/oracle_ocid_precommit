import pytest

from ocid_precommit import main

# Input, expected return value
TESTS = (
    (b'ocid1.tenancy.oc1..aaaaaaaaba3pv6wkcr4jqae5f44n2b2m2yt2j6rx32uzr4h25vqstifsfdsq', 1),
    (b'ocid1.instance.oc1.phx.abuw4ljrlsfiqw6vzzxb43vyypt4pkodawglp3wqxjqofakrwvou52gb6s5a', 1),
    (b'ocid1.instance.oc2.phx.abuw4ljrlsfiqw6vzzxb43vyypt4pkodawglp3wqxjqofakrwvou52gb6s5a', 1),
    (b'ocid1.instance.oc3.phx.abuw4ljrlsfiqw6vzzxb43vyypt4pkodawglp3wqxjqofakrwvou52gb6s5a', 1),
    (b'ocid in instance', 0),
    (b'please include ocid link', 0),
    (b'', 0),
)


@pytest.mark.parametrize(('input_s', 'expected_retval'), TESTS)
def test_main(input_s, expected_retval, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)
    assert main([str(path)]) == expected_retval
