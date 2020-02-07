from db.data_models import Post, Room
import datetime
def test_post_to_json():
    r = Room(id=1, name="Den")
    p = Post(id=1, room=1, date=datetime.datetime(2020,2,1), title="Test Post",
             body="This is a test of the emergency post system.")

    assert r.to_dict() == {'id': 1, 'name': "Den"}
    assert p.to_dict() == {'id':1, 'room': 1,'date': datetime.datetime(2020,2,1), 'title': "Test Post",
                            'body': "This is a test of the emergency post system."}


def test_room_to_dict():
    r = Room(id=1, name="Crematorium")
    assert r.to_dict() == {'id': 1, 'name': "Crematorium"}
