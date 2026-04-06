---
title: Debug a Rust Application
created: 2021-06-16 22:44:54
date: 2026-04-05 19:42:37.732121
authors:
- bendu
label: debug-a-rust-application
license: CC-BY-4.0
tags:
- Computer Science
- programming
- debug
- CodeLLDB
- Rust
- VSCode
- Visual Studio Code
---
**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**


## Debugging Rust in VSCode
1. Install the extension 
    [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb)
    .

2. Uncheck "Pause on panic" (checked by default).

## Debug Rust Using rust-gdb

## Debug Rust Using rust-lldb

## Debug Rust Using [rr](https://github.com/rr-debugger/rr)
is a lightweight tool for recording, 
replaying and debugging execution of applications (trees of processes and threads). 
Debugging extends gdb with very efficient reverse-execution, 
which in combination with standard gdb/x86 features like hardware data watchpoints, makes debugging much more fun. 

## References

- [Rust Autocomplete and Debugging in VS Code](https://www.youtube.com/watch?v=2VPSzb7RNtY)

- [Debugging Rust in VSCode](https://jason-williams.co.uk/debugging-rust-in-vscode)

- [Debugging Rust with VS Code](https://dev.to/rogertorres/debugging-rust-with-vs-code-11dj)

- [Debugging Rust programs with lldb on MacOS](https://bryce.fisher-fleig.org/debugging-rust-programs-with-lldb/)

- [Debugging Rust apps with GDB](https://blog.logrocket.com/debugging-rust-apps-with-gdb/)

- [Debugging Rust Tests](https://whamcloud.github.io/Online-Help/docs/Contributor_Docs/cd_Debugging_Rust_Tests.html)

- [How to debug unit test of rust?](https://github.com/vadimcn/vscode-lldb/issues/35)

- [vscode-lldb Manual -- Cargo Support](https://github.com/vadimcn/vscode-lldb/blob/v1.4.5/MANUAL.md#cargo-support)

- [How to debug Cargo tests (with CLI or IDE)?](https://github.com/rust-lang/cargo/issues/6821)




