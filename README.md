## python のユニットテスト(unittest) のサンプル

## インストール

モジュール`unittest` は標準添付ライブラリなのでインストールは不要。


## 実行サンプル
```shell
python -m unittest test_hello.py
```

### 実行方法を変える。

`__main__` を使えば、ファイルを実行でテストを実行できる。
```shell
python test_hello.py
```
```python
import unittest
## 
class TestHello(unittest.TestCase):
    def test_my(self):
        self.assertTrue(True)
## 
if __name__ == '__main__':
    unittest.main()
```

ただ、こちらの方法だとテスト対象ファイルが曖昧になる。対象ファイルはimport でいい感じに処理する必要がある。

## test ケースの書き方

```python
from unittest import TestCase
class My(TestCase):
    def test_xxx(self):
        self.assertEqual('a','a')
```

クラス名は特になんでも良い、メソッド名は`test_xxx` が必要。


## print() の 標準出力の取得

stdout を一時的に交換する。
```python
import sys 
from io import StringIO
sys.stdout = StringIO()
sys.stdout = sys.__stdout__
```
## 型チェック

型チェックを実現する.
```python
self.assertTrue(type(result) is str)
self.assertIsInstance(result, str)
```

`assertIsInstance ( realValue, expectedValue)` になり、通常のテストコードの`assert(ExpectedValue, real)` と逆になるので注意が必要。

## 例外の検出

例外が起きることをテストする

```python
with self.assertRaises(RuntimeError):
   target.myfunc()
```

