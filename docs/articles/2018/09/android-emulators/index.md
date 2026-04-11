---
title: Android Emulators
created: 2018-09-12 23:41:58
date: 2026-04-10 15:23:12.894642
authors:
  - bendu
label: android-emulators
license: CC-BY-4.0
tags:
  - software
  - Android
  - emulation
  - emulator
  - AnBox
  - VirtualBox
  - xDroid
---

:::{list-table} Android Emulators
:widths: auto
:header-rows: 1

*   - Name 
    - Free 
    - OS 
    - Hyper-v Compat on Win
    - ARM-only App Support 
    - Development 
*   - [GenyMotion](https://www.genymotion.com)
    - Limited 
    - Windows, macOS, Linux 
    - Partial 
    - Limited 
    - Active 
*   - [AnBox Cloud](https://anbox-cloud.io/)
    - Limited 
    - Ubuntu 
    - NA 
    - ? 
    - Active 
:::

<table style="width:100%">
  <tr>
    <th> Name </th>
    <th> Free </th>
    <th> OS </th>
    <th> Hyper-v Compat on Win</th>
    <th> ARM-only App Support </th>
    <th> Development </th>
  </tr>
  <tr>
    <td> 
    <a href="https://www.genymotion.com"> GenyMotion </a>
    <a href="#footnote1">[1]</a>
    </td>
    <td> Limited </td>
    <td> Windows, macOS, Linux </td>
    <td> Partial </td>
    <td> Limited </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.bluestacks.com"> BlueStacks </a>
    <a href="#footnote2">[2]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS (M chip) </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.ldplayer.net"> LDPlayer </a>
    <a href="#footnote3">[3]</a>
    </td>
    <td> Yes </td>
    <td> Windows </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.linzhuotech.com/index.php/home/index/xdroid.html"> xDroid </a>
    <a href="#footnote1">[9]</a>
    </td>
    <td> Limited </td>
    <td> Linux </td>
    <td> NA </td>
    <td> Limited </td>
    <td> Slow </td>
  </tr>
  <tr>
    <td> 
    <a href="https://mumu.163.com"> MuMu App Player </a>
    <a href="#footnote5">[5]</a>
    </td>
    <td> Yes </td>
    <td> macOS (M chip) </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://syzs.qq.com/"> 腾讯手游助手 </a>
    <a href="#footnote5">[6]</a>
    </td>
    <td> Yes </td>
    <td> Windows </td>
    <td> No </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://waydro.id/"> Waydroid </a>
    <a href="#footnote1">[11]</a>
    </td>
    <td> Yes </td>
    <td> Linux </td>
    <td> NA </td>
    <td> Yes </td>
    <td> Slow </td>
  </tr>
  <tr>
    <td> 
    <a href="https://anbox-cloud.io/"> AnBox Cloud </a>
    <a href="#footnote4">[4]</a>
    </td>
    <td> Limited </td>
    <td> Ubuntu </td>
    <td> NA </td>
    <td> ? </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://www.android-x86.org"> Android-x86 + VM </a>
    <a href="#footnote6">[7]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS, Linux </td>
    <td> Yes </td>
    <td> Limited </td>
    <td> Inactive </td>
  </tr>
  <tr>
    <td> 
    <a href="https://developer.android.com/studio"> Android SDK + Android Studio </a>
    <a href="#footnote7">[8]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS, Linux </td>
    <td> ? </td>
    <td> Yes </td>
    <td> Active </td>
  </tr>
  <tr>
    <td> 
    <a href="https://github.com/budtmo/docker-android"> docker-android </a>
    <a href="#footnote1">[10]</a>
    </td>
    <td> Yes </td>
    <td> Windows, macOS, Linux </td>
    <td> Yes </td>
    <td> Limited </td>
    <td> Active </td>
  </tr>
</table>

[1] [GenyMotion](https://www.genymotion.com/) works well.

[2] [BlueStacks](https://www.bluestacks.com/) works well.

[3] [LDPlayer](https://www.ldplayer.net/) is also called 雷电模拟器 in Chinese. It works well.

[4] [AnBox Cloud](https://anbox-cloud.io/) is developed by Canonical and works on Ubuntu only.

[5] [MuMu App Player](https://mumu.163.com/) works well.
Specially, Tribal Pioneer works on MuMu App Player on macOS.

[7] [Android X86](https://www.android-x86.org/)
provides ISO images and RPM files for Fedora Linux distributions.
ISO images can be used with VM tools (such as KVM, VirtualBox, VMware, etc)
just like you can other operating systems in virtual machines.
It's currently inactive and ISO images are outdated.

[8] Android SDK and Android Studio works together to emulate software found on Android
using the resources of your PC.
Android developers mostly use Android SDK tools for testing and development purposes,
but it'll work for casual use and play as well.

[9] xDroid can run but has various issues.

[10] Docker-Android is a docker image
built to be used for everything
related to mobile website testing and Android project.

[11] Waydroid is a container-based approach to boot a full Android system on Linux.
It is a successor of AnBox.

## References

- [Waydroid | Android in a Linux container](https://waydro.id/)

- [Setting up Android-x86 with Virt-Manager - ROllerozxa](https://voxelmanip.se/2022/07/12/setting-up-android-x86-with-virt-manager/)

- [Run ARM apps on the Android Emulator](https://android-developers.googleblog.com/2020/03/run-arm-apps-on-android-emulator.html)

- [安卓虚拟键盘_干货分享：推荐几款性能不错的安卓模拟器](https://blog.csdn.net/weixin_39991222/article/details/109897655?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control)

- [Android Emulators @ GameTechWiki](https://emulation.gametechwiki.com/index.php/Android_emulators)

- [Tips on Virtualbox](http://www.legendu.net/misc/blog/virtualbox-tip)

- [x86 Virtualization in Browser](https://copy.sh/v86/)

- [Run ARM apps on the Android Emulator](https://android-developers.googleblog.com/2020/03/run-arm-apps-on-android-emulator.html)