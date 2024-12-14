[简体中文](README.md) | [繁體中文](README_TW.md) | **English**


# Dichback Algorithm
A step-saving and efficient backtracking algorithm.

> But this algorithm relies on **logical unit** and does not save steps if the number of steps to run the logical elements counts. Therefore, if there are special logical conjunction(or logical OR) units, only simple steps are needed to calculate the sum of logical conjunction(or logical OR) operations, and the optimization efficiency brought by this algorithm is very high.

## Backtracking logic

The backtracking step is complicated, so it might be better to just look at the code

- Define logic conjunction(logic OR) function units:

    - **logic_unit**(self, **effective_list**: *list*) -> *bool* : Accept a list (a collection of valid data) as a parameter, iterate over each element, and return `False` if any element does not conform to the defined logic; otherwise, return `True`.

- Call the function **dichotomy_backtracking_algorithm**(**effective_list**):


    1. **Call the Logic conjunction(logic OR) Function Unit** (parameter : *effective_list* ) : return *bool*

    2. **First Call**：If the return value is `True`, exit directly (since all elements conform to the defined logic); if the return value is `False`, divide the effective list into two sublists (`Sublist 1`, `Sublist 2`), and return `Sublist 1` as a parameter to **Step 1**.


    3. **Not the First Call**：If the return value is `True`, then all elements in the list conform to the defined logic, and all elements of the list are added to `yes_list`. At this point, backtrack to the other sublists in its parent list (since it's a binary division, a parent list generally has only two sublists, meaning each list has at most one sibling list at the same level). If the other sublist returns `False`, continue to divide the sublist until the sublist length is less than or equal to `lm` (this value actually affects the degree of algorithm optimization because it restricts the **minimum length** of the sublist, preventing excessive depth-first search and waste, meaning that when `lm = (length of effective list) // 3 - 1`, theoretically, the list is divided at most 4 times). The elements of the sublist are enumerated one by one, and if `True` is returned, they are added to `yes_list`, then backtrack, and return its sibling list as a parameter to **Step 1**.


No illustrations are available at the moment, so it might be difficult to understand.

## Download and Call

```bash
pip install dichback
```

Example Program
```python
from dichback import AlgorithmSet

class Al(AlgorithmSet):
    LIST = [i for i in range(1, 100) if i%10 == 0]
    def __init__(self):
        super().__init__()

    def logic_unit(self, effective_list: list) -> bool:
        # LIST = [i for i in range(1, 100) if i%2 == 0]
        # 也就是2,4,6,8,10,12...98
        # 在1,2,3,4..99这个数据样本中LIST的离散程度非常大
        # 因为在这个逻辑单元中相当于True,False,True.False...
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


In the `dichback` module, the **AlgorithmSet** class requires that a logical unit be defined when inheriting:
```python
def logic_unit(self, effective_list: list) -> bool
```
At the same time, it provides the *self.counts* attribute to view the number of times the logical unit is called.

## Other algorithms in Dichback

These algorithms all support logical units; for details, please refer to the code comments.

- Simple exhaustion algorithm
- Common dichotomy algorithm