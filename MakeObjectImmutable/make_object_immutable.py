import collections.abc
import copy

class FrozenDict(collections.abc.Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
        self._hash = None

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(frozenset(self._data.items()))
        return self._hash

    def __eq__(self, other):
        if isinstance(other, FrozenDict):
            return self._data == other._data
        elif isinstance(other, collections.abc.Mapping):
            return self._data == other
        return NotImplemented

    def __repr__(self):
        return f"FrozenDict({self._data!r})"

class ImmutableData:
    def __init__(self, **kwargs):
        object.__setattr__(self, '_initializing', True)

        for key, value in kwargs.items():
            processed_value = self._make_immutable_copy(value)
            object.__setattr__(self, key, processed_value)

        object.__setattr__(self, '_initializing', False)

    def _make_immutable_copy(self, obj):
        if isinstance(obj, collections.abc.MutableSequence):
            return tuple(self._make_immutable_copy(item) for item in obj)
        elif isinstance(obj, collections.abc.MutableMapping):
            return FrozenDict({self._make_immutable_copy(k): self._make_immutable_copy(v) for k, v in obj.items()})
        elif isinstance(obj, collections.abc.MutableSet):
            return frozenset(self._make_immutable_copy(item) for item in obj)
        elif isinstance(obj, (tuple, frozenset, FrozenDict, int, float, str, bool, type(None))):
            return obj
        else:
            try:
                return copy.deepcopy(obj)
            except TypeError:
                return obj

    def __setattr__(self, name, value):
        if not hasattr(self, '_initializing') or not self._initializing:
            raise AttributeError(f"Cannot modify attribute '{name}' of an immutable object.")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        raise AttributeError(f"Cannot delete attribute '{name}' from an immutable object.")

    def __repr__(self):
        attrs = ', '.join(f"{key}={getattr(self, key)!r}" for key in sorted(self.__dict__.keys()) if key != '_initializing')
        return f"{self.__class__.__name__}({attrs})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        self_attrs = {k: v for k, v in self.__dict__.items() if k != '_initializing'}
        other_attrs = {k: v for k, v in other.__dict__.items() if k != '_initializing'}
        return self_attrs == other_attrs

    def __hash__(self):
        items = tuple(sorted((k, v) for k, v in self.__dict__.items() if k != '_initializing'))
        return hash(items)