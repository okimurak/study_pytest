from src.hogehoge import HogeHoge

def test_say(capfd):
  instance = HogeHoge("Taro")
  instance.say()

  out, err = capfd.readouterr()
  assert out == "Hello ! My name is Taro.\n"
  assert err is ''