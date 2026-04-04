---
title: "Easy-Made Mistake with C++ Iterator"
created: 2015-02-13 22:47:56
date: 2016-07-13 22:47:56
authors:
  - bendu
label: easy-made-mistake-with-cpp-iterator
license: CC-BY-4.0
tags:
  - programming
  - C++
  - iterator
  - mistake
  - error
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


the wrong way

```
for(auto it=l.cbegin(); it!=l.cend(); ++it){
    for(auto jt=++it; jt!=l.cend(); ++jt){
        cout << *it << " <-> " << *jt << endl;
    }
}
```

it is increased again in the inner loop!!!


the correct way

    for(auto it=l.cbegin(); it!=l.cend(); ++it){
        for(auto jt=next(it); jt!=l.cend(); ++jt){
            cout << *it << " <-> " << *jt << endl;
        }
    }

it is very tricky to iterate a container and delete elements
blog about it
