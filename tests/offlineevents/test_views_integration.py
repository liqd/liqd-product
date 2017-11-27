import pytest

from meinberlin.test.helpers import assert_template_response


@pytest.mark.django_db
def test_detail_view(client, offline_event, partner):
    url = offline_event.get_absolute_url()
    response = client.get(url)
    assert_template_response(
        response, 'meinberlin_offlineevents/offlineevent_detail.html')