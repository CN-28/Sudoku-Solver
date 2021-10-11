# 🧮 Sudoku Solver

`Sudoku Solver` is the window application, which solves a logic-based, combinatorial, number-placement puzzle called <a href="https://en.wikipedia.org/wiki/Sudoku">Sudoku</a>.

# 📜 Table of contents
* [About The Project](#about-the-project)
* [Visualization](#visualization)
* [Installation](#installation)
* [Usage](#usage)
* [Tech stack](#tech-stack)
* [Development plans](#development)
* [License](#license)

<h1 id="about-the-project"> 📗 About The Project </h1>

This Sudoku Solver is a classic 9x9 sudoku solver application.

App uses recursive algorithm with backtracking to solve Sudoku.

In each 1x1 square from 9x9 grid the user can enter number from to 1 to 9.

`SOLVE` - button, which fills the board with solved Sudoku.

`RESET` - button, which clears the whole board of Sudoku.

If you are not familiar with Sudoku rules and don't know how to play, you can learn <a href="https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/">here</a>.

## What was the purpose of this project?
The idea behind this project was to learn better and understand more deeply the <a href="https://en.wikipedia.org/wiki/Recursion">recursion</a> and have fun while learning.

The recursion is really essential and it is used in many fields of Computer Science.

<h1 id="visualization"> 📊 Visualization </h1>

The following visualization shows the solution of extremely hard Sudoku puzzle.

![sudoku](https://user-images.githubusercontent.com/67509491/136785711-fe604fde-d945-45ef-8ec9-b190bb14dd98.gif)

<h1 id="installation"> 🔧 Installation </h1>

To run Sudoku Solver, you need to have <strong>Tkinter</strong> module installed.

If you don't have it installed, open command prompt and enter the following command.

```bash
pip install tk
```

Now download the repository, open your comand prompt in the repository and run <strong>sudoku.py</strong> by typing:
```bash
python sudoku.py
```

<h1 id="usage"> 📋 Usage </h1>

1. Fill the 9x9 board with numbers.
2. Left-click `SOLVE` button to solve Sudoku.
3. Left-click `RESET` button to clear the board and return to first bullet point or quit the appliaction.

If you enter invalid numbers or violate the rules of Sudoku, there will pop up the information that sudoku is not solvable.

<h1 id="tech-stack"> 👨‍💻 Tech stack </h1>

Project is created with:
- <strong>Python
- Tkinter</strong>

<h1 id="development"> 🖥️ Development plans </h1>

In the future I am going to improve this project by adding an option to solve Sudoku 
from the photo using OpenCV library in Python and making a better looking and more sophisticated GUI.

<h1 id ="license"> ⚖️ License </h1>

![GitHub](https://img.shields.io/github/license/CN-28/Sudoku-Solver)
