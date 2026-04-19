---
title: Tips on rustup
created: 2021-04-24 08:36:28
date: 2026-04-13 23:15:05.294041
authors:
  - bendu
label: tips-on-rustup
license: CC-BY-4.0
tags:
  - computer science
  - programming
  - Rust
  - rustup
  - rustfmt
  - toochain
  - stable
  - beta
  - nightly
---

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## Install rustup

### Linux and macOS

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | bash -s -- -y
```

Rust tools (`rustc`, `cargo`, `rustup`, etc)
will be added to Cargo's bin directory,
located at `$HOME/.cargo/bin`.

You can also run the following command to install rust.

```bash
xinstall rustup -ic
```

### Windows

1. Download rustup.exe and install it.

1. Download and install the
   [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)
   .
   Select C++ tools during the installation.

1. Restart your computer.

## Install stable/nightly Versions of Rust

rustup toolchain install stable
rustup toolchain install beta
rustup toolchain install nightly
rustup default stable

## Install rust-src

rustup component add rust-src

## Install rustfmt

rustup component add rustfmt

## Install Clippy

rustup component add clippy

## References

- https://rust-lang.github.io/rustup/index.html

- https://github.com/rust-lang/rustup

- [Unable to compile Rust hello world on Windows: linker link.exe not found](https://stackoverflow.com/questions/55603111/unable-to-compile-rust-hello-world-on-windows-linker-link-exe-not-found)
