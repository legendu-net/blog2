---
title: Serialization and deserialization in Python
created: 2020-09-03 09:42:01
date: 2026-04-15 19:27:00.979994
authors:
  - bendu
label: serialization-and-deserialization-in-python
license: CC-BY-4.0
tags:
  - computer science
  - Pickle
  - serialization
  - deserialization
  - JSON
  - cloudpickle
  - dill
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

1. [JSON](https://www.json.org/json-en.html)
   (JavaScript Object Notation) is a lightweight data-interchange format.
   It is suggested that you <span style="color:red"> avoid using it </span>.
   Please refer to
   [Shotcomes of JSON](https://www.legendu.net/misc/blog/json-tips/#shortcomes-of-json)
   for detailed discussions on this.
   TOML and YAML are better text-based alternatives to JSON.
   If serialization and deserialization is done in Python only,
   [pickle](http://www.legendu.net/misc/blog/serialize-and-deserialize-object-using-pickle-in-python)
   is preferred.
   If you do want to use JSON in Python,
   please refer to
   [JSON Parsing Libraries in Python](https://www.legendu.net/misc/blog/json-tips/#json-parsing-libraries-in-python)
   for more discussions.

1. TOML

1. YAML

   - YAML is a superset of json.
   - YAML support serialization and deserialization of set while json does not.
   - YAML is more readable.

1. [Pickle](http://www.legendu.net/misc/blog/serialize-and-deserialize-object-using-pickle-in-python)
   is the most popular serialization and deserialization tool in Python.
   It supports serializing/deserializing most (even not all) Python classes.

1. [Dill](https://github.com/uqfoundation/dill)
   extends Python's
   [Pickle](http://www.legendu.net/misc/blog/serialize-and-deserialize-object-using-pickle-in-python)
   module for serializing and de-serializing Python objects to the majority of the built-in python types.
   It also provides some good diagnostic tools for pickling,
   the best of which is the pickle trace.
   For more discussions,
   please refer to
   [How to check which detail of a complex object cannot be pickled](https://stackoverflow.com/questions/22233478/how-to-check-which-detail-of-a-complex-object-cannot-be-pickled)
   .

1. cloudpickle

1. Use Parquet for pandas DataFrame.

## References

- [How to check which detail of a complex object cannot be pickled](https://stackoverflow.com/questions/22233478/how-to-check-which-detail-of-a-complex-object-cannot-be-pickled)
