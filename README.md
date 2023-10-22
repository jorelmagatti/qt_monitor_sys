# qt_monitor_sys
Um simples monitor de sistemas com python PySide Qt Core 


<h1 align="center">Welcome to qt_monitor_sys �</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/jorelmagatti" target="_blank">
    <img alt="Twitter: jorelmagatti" src="https://img.shields.io/twitter/follow/jorelmagatti.svg?style=social" />
  </a>
</p>

> Um simples monitor de sistemas com python PySide Qt Core. O design foi criado no Qt-Designer e exportado para python, aproveitei esta base e refatorei para estrutura presente

## Preview

<img align="center" alt="monitr_python_qt" src="https://drive.google.com/file/d/1znWiTzQfpuuy-q0FkC34OtZt9AaZnwGL/view?usp=sharing">

## Envirement

```sh
pyenv shell 3.8.10
```

## Usage

```sh
python __main__.py
```

## Map
```bash
📦qt_monitor_sys
 ┣ 📂.git
 ┃ ┣ 📂branches
 ┃ ┣ 📂hooks
 ┃ ┃ ┣ 📜applypatch-msg.sample
 ┃ ┃ ┣ 📜commit-msg.sample
 ┃ ┃ ┣ 📜fsmonitor-watchman.sample
 ┃ ┃ ┣ 📜post-update.sample
 ┃ ┃ ┣ 📜pre-applypatch.sample
 ┃ ┃ ┣ 📜pre-commit.sample
 ┃ ┃ ┣ 📜pre-merge-commit.sample
 ┃ ┃ ┣ 📜pre-push.sample
 ┃ ┃ ┣ 📜pre-rebase.sample
 ┃ ┃ ┣ 📜pre-receive.sample
 ┃ ┃ ┣ 📜prepare-commit-msg.sample
 ┃ ┃ ┣ 📜push-to-checkout.sample
 ┃ ┃ ┣ 📜sendemail-validate.sample
 ┃ ┃ ┗ 📜update.sample
 ┃ ┣ 📂info
 ┃ ┃ ┗ 📜exclude
 ┃ ┣ 📂logs
 ┃ ┃ ┣ 📂refs
 ┃ ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┃ ┗ 📂remotes
 ┃ ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┃ ┗ 📜HEAD
 ┃ ┃ ┗ 📜HEAD
 ┃ ┣ 📂objects
 ┃ ┃ ┣ 📂info
 ┃ ┃ ┗ 📂pack
 ┃ ┃ ┃ ┣ 📜pack-24cb85054289aeaf84892b1f79d1c2a601cfad31.idx
 ┃ ┃ ┃ ┣ 📜pack-24cb85054289aeaf84892b1f79d1c2a601cfad31.pack
 ┃ ┃ ┃ ┗ 📜pack-24cb85054289aeaf84892b1f79d1c2a601cfad31.rev
 ┃ ┣ 📂refs
 ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┣ 📂remotes
 ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┗ 📜HEAD
 ┃ ┃ ┗ 📂tags
 ┃ ┣ 📜FETCH_HEAD
 ┃ ┣ 📜HEAD
 ┃ ┣ 📜config
 ┃ ┣ 📜description
 ┃ ┣ 📜index
 ┃ ┗ 📜packed-refs
 ┣ 📂src
 ┃ ┣ 📂ui
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜ui_form.cpython-38.pyc
 ┃ ┃ ┣ 📂events_timer_ui
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜time_updates.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜time_updates.py
 ┃ ┃ ┣ 📂font_ui
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜font_monitor.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜font_monitor.py
 ┃ ┃ ┣ 📂icon_ui
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜icon_monitor.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜icon_monitor.py
 ┃ ┃ ┣ 📂label_ui
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜label_monitor.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜label_monitor.py
 ┃ ┃ ┣ 📂progressbar_ui
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜progressbar_monitor.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜progressbar_monitor.py
 ┃ ┃ ┣ 📂timer_ui
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┃ ┗ 📜timer_monitor_ui.cpython-38.pyc
 ┃ ┃ ┃ ┗ 📜timer_monitor_ui.py
 ┃ ┃ ┗ 📜ui_form.py
 ┃ ┗ 📂util
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┗ 📜ui_util.cpython-38.pyc
 ┃ ┃ ┗ 📜ui_util.py
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┗ 📜__main__.py
```
## Doc
```sh
README.md
```
## Author

� **Jorel Magatti (JorelDev)**

* Twitter: [@jorelmagatti](https://twitter.com/jorelmagatti)
* Github: [@jorelmagatti](https://github.com/jorelmagatti)
* LinkedIn: [@jorelmagatti](https://linkedin.com/in/jorelmagatti)
* Instagram: [@jorelmagatti](https://www.instagram.com/jorel_magatti/)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_