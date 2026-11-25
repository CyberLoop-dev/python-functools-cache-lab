<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=170&section=header&text=Python%20Cache%20Lab&fontSize=38&fontColor=ffffff" alt="Python Cache Lab header"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=2800&pause=900&center=true&vCenter=true&width=820&lines=Python%20Cache%20Lab%20%E2%80%A2%20Explore%20functools.lru_cache%20with%20a%20recursive%20Fibonacci%20example%2C%20visible%20cache%20statistics%2C%20and%20a%20typed-key%20comparison." alt="Animated project title"/></p>
<p align="center">
<img src="https://img.shields.io/github/license/CyberLoop-dev/python-functools-cache-lab?style=flat-square" alt="License"/>
<img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-functools-cache-lab?style=flat-square" alt="Language"/>
<img src="https://img.shields.io/github/stars/CyberLoop-dev/python-functools-cache-lab?style=flat-square" alt="Stars"/>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-functools-cache-lab?style=flat-square" alt="Last commit"/>
</p>

![Project illustration](assets/mark.svg)

## 🔎 Overview
Explore functools.lru_cache with a recursive Fibonacci example, visible cache statistics, and a typed-key comparison.

## ✨ Features
- 🧠 Runs a cached Fibonacci calculation with a configurable cache size
- 📈 Prints hits, misses, current size, and maximum size
- 🧹 Demonstrates clearing the cache and observing fresh misses
- 🔤 Shows how typed=True distinguishes values such as 1 and 1.0

## 🎬 Demo
No hosted demo is published. Run the project locally using the Quick Start command below.

## 🚀 Quick Start
    python -m cache_lab --n 25 --maxsize 4

## 🧰 Tech Stack
- Python 3.10+
- functools standard library
- argparse and unittest

## 🗂️ Folder Structure
    cache_lab/cli.py          Command-line demo
    cache_lab/__main__.py     Module entry point
    tests/test_cli.py         Standard-library tests
    pyproject.toml            Package metadata

## 🛣️ Roadmap
- [ ] Add a comparison with an uncached recursive function
- [ ] Show a short sequence that makes LRU eviction visible

## 🤝 Contributing
Issues and pull requests are welcome. Keep changes focused, document behavior, and add a small reproducible example for new features.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" alt="Animated footer wave"/></p>
