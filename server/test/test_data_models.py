from db.data_models import ModelBase, Post, Room, House, BlockedRooms
import datetime
def test_post_to_json():
    r = Room(1, "Den")
    p = Post(1, r, datetime.datetime.now(), "Test Post", "This is a test of the emergency post system.")

    j = p.to_json()

    assert(p)
