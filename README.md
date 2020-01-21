With Utils
==========

So far it's pretty empty, but maybe it'll become an independant lib?

## `iter`

Iteration-related utils

### `n_grams`

Provides a way to create n_grams from an iterator

```python
assert list(n_grams([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
```
