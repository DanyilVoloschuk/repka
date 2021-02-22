import pytest

from repks.apps.hello_repka.api.v1.views.views import HelloRepkaView


@pytest.mark.repka
def test_repka_text():
    assert HelloRepkaView.get_text() == 'hello, repka'
