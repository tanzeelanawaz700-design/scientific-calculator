<div align="center">

# 🧮 Scientific Calculator

A clean, desktop scientific calculator built with **Python** and **Tkinter**.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-4D9BA8)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

<!-- Replace this with your own screenshot: put it in an "images" folder -->
<img src="images/screenshot.png" alt="Scientific Calculator Screenshot" width="360">

</div>

---

## ✨ Features

- **Basic operations:** addition, subtraction, multiplication, division
- **Trigonometry:** `sin`, `cos`, `tan` (input in degrees)
- **Logarithms:** `log` (base 10) and `ln` (natural log)
- **Powers and roots:** `x²`, `xʸ`, `√`
- **Other functions:** `1/x`, `%`, `±`
- **Constants:** `π` and `e`
- **Error handling:** division by zero, invalid input and negative square roots show `Error`
- **Real calculator layout:** scientific keys on top, number pad below, large `=` button

## 🖼️ Layout

```
sin   cos   tan   log   ln    √
x²    xʸ    1/x   π     e     %
7     8     9     ÷     (     )
4     5     6     ×     C     ±
1     2     3     −     [  =  ]
[ 0 ]       .     +     [  =  ]
```

## 🚀 Getting Started

### Requirements

- Python 3.8 or newer
- Tkinter (included with most Python installations)

### Run it

```bash
# 1. Clone the repository
git clone https://github.com/tanzeelanawaz700-design/scientific-calculator.git

# 2. Go into the folder
cd scientific-calculator

# 3. Start the calculator
python scientific_calculator.py
```

> On some Linux systems you may need to install Tkinter first:
> `sudo apt install python3-tk`

## 📖 How to Use

1. Type the first number using the number buttons.
2. Press an operator (`+`, `−`, `×`, `÷`, `xʸ`).
3. Type the second number and press `=`.
4. For functions like `sin`, `√` or `log`, type the number first, then press the function key.
5. Press `C` to clear everything.

## 🗂️ Project Structure

```
scientific-calculator/
├── scientific_calculator.py
├── images/
│   └── screenshot.png
├── README.md
└── LICENSE
```

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [math](https://docs.python.org/3/library/math.html) module

## 🗺️ Roadmap

- [ ] Support for brackets `( )` in full expressions
- [ ] Keyboard input
- [ ] Degrees / radians toggle
- [ ] Calculation history
- [ ] Light and dark theme

## 🤝 Contributing

Suggestions and improvements are welcome.

1. Fork the project
2. Create your branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push the branch: `git push origin feature/new-feature`
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

## 👤 Author

**Tanzeela Nawaz**
BS Bioinformatics Student

[![GitHub](https://img.shields.io/badge/GitHub-tanzeelanawaz700--design-181717?logo=github)](https://github.com/tanzeelanawaz700-design)

---

<div align="center">⭐ If you like this project, give it a star!</div>
