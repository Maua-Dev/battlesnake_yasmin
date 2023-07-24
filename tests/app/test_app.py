from src.app.main import read_root, start


class Test_App:
    def test_read_root(self):
        resp = read_root()
        
        assert resp == {
  "apiversion": "1",
  "author": "yasbonilha",
  "color": "#FF5733",
  "head": "all-seeing",
  "tail": "do-sammy",
  "version": "0.0.1-beta"
}
    def test_start(self):
        response = start()
        assert response == "ok"