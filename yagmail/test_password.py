from unittest.mock import patch
from password import handle_password

def test_handle_password():
    inputs = iter([
        "short", "shorter", "correctpassword",  # パスワード入力
        "n",  # キーチェーン保存の選択
    ])
    with patch("getpass.getpass", side_effect=inputs):
        result = handle_password("testuser", None)
        print(f"Final Password: {result}")

test_handle_password()
