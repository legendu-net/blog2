---
title: Cell and RefCell in Rust
created: 2023-02-02 17:21:12
date: 2026-04-13 23:14:32.814407
authors:
  - bendu
label: cell-and-refcell-in-rust
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Cell
  - RefCell
  - borrow checker
  - interior mutability
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

https://doc.rust-lang.org/std/cell/

https://doc.rust-lang.org/std/cell/struct.RefCell.html

[Rust Cell and RefCell](https://blog.iany.me/2019/02/rust-cell-and-refcell/)

Rc + RefCell is another alternative to circumvent Rust's borrow checker at compile time.
Checks at runtime and might might panic if there are borrowing issues in your code.

comes at a performance penalty as it is slower to track borrowing at runtime.

1. Avoid use Cell and RefCell
   unless you have to rely on them to circumvent Rust's borrow checker at compile time.

## References

- [Cell and RefCell](https://subscription.packtpub.com/book/programming/9781789616705/6/ch06lvl1sec44/cell-and-refcell)
