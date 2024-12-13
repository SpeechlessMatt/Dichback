[简体中文](README_CN.md) | **繁體中文** | [English](README_EN.md)


# 二分回溯算法
一種節省步數的，效率高的回溯算法。

> 但是本算法依靠**邏輯元**，如果運行邏輯元的步數算上的話，併不節省步數。所以，如果有特殊的邏輯與-邏輯元，在運算整體和的時候只需要一步，那本算法帶來的優化效率是非常高的。

## 回溯邏輯

回溯步驟比較復雜，直接看代碼可能會好一點

- 定義邏輯與-邏輯函數單元：

    - **logic_unit**(self, **effective_list**: *list*) -> *bool*： 接收一個列錶（有效數據集合）作為參數，遍歴每一個元素，存在一個元素不符合定義的邏輯時就返回`False`,否則返回`True`

- 進入**dichotomy_backtracking_algorithm**(**effective_list**)方法:

    1. **調用邏輯與-邏輯函數單元**（傳參：*effective_list*）：返回`True`或者`False`

    2. **第一次調用**：如果返回值為`True`，則直接退出（因為所有元素均符合定義邏輯），返回值為`False`，則將有效列錶二分為兩個子列錶（`子列錶1`,`子列錶2`），將`子列錶1`作為參數返回**步驟1**

    3. **非第一次調用**：如果返回值為`True`,那麽該列錶內的所有元素均符合定義邏輯，將該列錶元素全部加入*yes_list*，這個時候回溯到它的父列錶中的其他子列錶中（由於二分法，一個父列錶一般就兩個子列錶，也就是說每一個列錶最多只有一個同父同級列錶），如果其他子列錶返回`False`,那麽繼續分割子列錶，直到子列錶長度小於等於`lm`（這一個值事實上會影響算法優化程度，因為這個值限制了子列錶的**最小長度**，防止深度優先搜索過度深入造成浪費，也就是說當`lm=有效列錶長度//3-1`的時候，理論上列錶最多被分割4次），會把子列錶元素逐個窮舉，返回`True`，則加入`yes_list`，然後回溯，將它的同父同級列錶作為參數返回**步驟1**

暫時還沒有配圖，所以可能不太好理解

## 下載和調用

```bash
pip install dichback
```

示例程序
```python
from dichback import AlgorithmSet

class Al(AlgorithmSet):
    LIST = [i for i in range(1, 100) if i%10 == 0]
    def __init__(self):
        super().__init__()

    def logic_unit(self, effective_list: list) -> bool:
        # LIST = [i for i in range(1, 100) if i%2 == 0]
        # 也就是2,4,6,8,10,12...98
        # 在1,2,3,4..99這個數據樣本中LIST的離散程度非常大
        # 因為在這個邏輯單元中相當於True,False,True.False...
        for i in effective_list:
            if not i in self.LIST:
                return False
        return True

if __name__ == '__main__':
    a = Al()
    rep = a.dichotomy_backtracking_algorithm([i for i in range(1, 100)])
    print(a.counts)
    print(rep)
```

`dichback`中**AlgorithmSet**類繼承的時候強制要求定義邏輯元:
```Python
def logic_unit(self, effective_list: list) -> bool
```

同時提供*self.counts*屬性，查看邏輯元調用次數