from db.data_models import ModelBase, Post, Room, House, BlockedRooms
import datetime
def test_post_to_json():
    r = Room(id=1, name="Den")
    p = Post(id=1, room=r, date=datetime.datetime(2020,2,1), title="Test Post",
             body="This is a test of the emergency post system.")

    assert p.to_dict() == { 'id':1, 'date': datetime.datetime(2020,2,1), 'title': "Test Post",
                            'body': "This is a test of the emergency post system."}

