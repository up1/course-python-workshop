from hello import say_hi

def test_say_hi():
    assert say_hi("Alice") == "Hi, Alice!"
    assert say_hi("Bob") == "Hi, Bob!"
    assert say_hi("Charlie") == "Hi, Charlie!"
    assert say_hi("") == "Hi, !"
    assert say_hi(None) == "Hi, None!"