# 🤖 Right-Hand Maze Solver

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Reeborg's World](https://img.shields.io/badge/Reeborg's_World-Educational-green?style=for-the-badge)](https://reeborg.ca/reeborg.html)
[![100 Days of Code](https://img.shields.io/badge/100_Days_of_Code-Day_6-blue?style=for-the-badge)](https://www.udemy.com/course/100-days-of-code/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Right_Hand_Rule-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/Maze_solving_algorithm)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Course](https://img.shields.io/badge/Instructor-Angela_Yu-purple?style=for-the-badge)](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)

🧭 **A Python implementation of the right-hand rule algorithm for maze solving using Reeborg's World**

## 📖 About

🎓 This is my solution for **Day 6** of Angela Yu's 100 Days of Code Python course! Built for Reeborg's World maze challenges, this algorithm uses the classic right-hand rule to navigate through any simply-connected maze.

### 🏷️ Tags
`python` `maze-solver` `algorithms` `right-hand-rule` `reeborg` `100-days-of-code` `angela-yu` `pathfinding` `robotics` `wall-following` `educational` `automation`

## 🎯 Problem Statement

🌟 **Lost in a Maze Challenge**: Reeborg was exploring a dark maze and the battery in its flashlight ran out. Help Reeborg find the exit using the right-hand rule algorithm!

## 🧠 Algorithm: Right-Hand Rule

The robot follows these simple prioritized rules:

1. **🔄 Always try to turn right first** - If the right side is clear, turn right and move
2. **➡️ Go straight** - If the front is clear but right is blocked, move forward  
3. **↩️ Turn left** - If both right and front are blocked, turn left to find a new path

✨ The right-hand rule is like walking through a maze with your right hand always touching the wall - you'll eventually find the exit!

## 💻 Code Implementation

```python
def turn_right():
    """Turn right by turning left three times"""
    turn_left()
    turn_left() 
    turn_left()

# Initial positioning
while front_is_clear():
    move()
turn_left()

# Main algorithm - Right-hand rule
while not at_goal():
    if right_is_clear():        # 🔄 Priority 1: Turn right
        turn_right()
        move()
    elif front_is_clear():      # ➡️ Priority 2: Go straight
        move()
    else:                       # ↩️ Priority 3: Turn left
        turn_left()
```

## 🔧 How It Works

### **🧭 Algorithm Logic**
1. **Initial Setup**: Position Reeborg at maze entrance
2. **Wall Following**: Keep "right hand" on the wall at all times
3. **Priority System**: Right → Forward → Left decision making
4. **Goal Detection**: Continue until `at_goal()` returns True

### **⚙️ Technical Details**
- **Custom Function**: `turn_right()` simulates right turn using three left turns
- **Sensor Usage**: `right_is_clear()`, `front_is_clear()`, `at_goal()`
- **Loop Structure**: `while` loop with `if/elif/else` branching

## 🚀 Features

- ✅ **Guaranteed Solution**: Works for any simply-connected maze
- ✅ **Efficient Navigation**: Optimal wall-following strategy  
- ✅ **Clean Code**: Well-commented and educational
- ✅ **No Memory Required**: Stateless algorithm
- ✅ **Educational Value**: Demonstrates fundamental CS concepts

## 🎮 Usage

1. 🌐 **Visit** [Reeborg's World](https://reeborg.ca/reeborg.html)
2. 🎯 **Select** a maze challenge (Day 6 levels recommended)
3. 📋 **Copy** the code from `maze_solver.py`
4. 🏃‍♂️ **Paste** into Reeborg's editor and run
5. 🎉 **Watch** Reeborg navigate to the goal automatically!

## 🧩 Key Concepts Learned

- **🔄 Algorithmic Thinking**: Breaking complex problems into simple rules
- **🤖 Robot Control**: Basic autonomous navigation principles
- **🎯 Decision Making**: Priority-based conditional logic
- **♻️ Function Design**: Creating reusable helper functions
- **🔁 Loop Logic**: Combining `while` loops with conditional statements

## 📊 Algorithm Analysis

| Aspect | Details |
|--------|---------|
| **⏱️ Time Complexity** | O(n) - visits each cell at most twice |
| **💾 Space Complexity** | O(1) - no memory of previous positions |
| **🎯 Success Rate** | 100% for simply-connected mazes |
| **🔧 Maze Types** | Works on any maze without isolated walls |

## 🏆 Why This Algorithm Matters

The right-hand rule isn't just a coding exercise - it's fundamental in:

- **🤖 Robotics**: Real-world robot navigation systems
- **🎮 Game AI**: Pathfinding in video games  
- **📊 Graph Theory**: Traversal algorithms
- **🏛️ Architecture**: Emergency evacuation planning
- **🧭 Navigation**: GPS and mapping applications

## 🎓 Course Context

**📅 100 Days of Code - Day 6**
- **👩‍🏫 Instructor**: Angela Yu
- **🎯 Learning Focus**: Functions, loops, and conditional statements
- **🌐 Platform**: Reeborg's World educational environment
- **📚 Course**: Complete Python Pro Bootcamp

## 📈 Learning Journey

This project represents foundational knowledge that scales to:

- 🗺️ **Advanced Pathfinding**: A*, Dijkstra's algorithm
- 🦾 **Robotics**: SLAM, autonomous navigation
- 🧠 **Machine Learning**: Reinforcement learning for navigation
- 🎮 **Game Development**: AI character movement

## 🔗 Related Projects

Check out my other 100 Days of Code projects:
- 🐍 [Day 1-5]: Python Fundamentals
- 🎯 [Day 7+]: Advanced Python Challenges

## 📸 Demo

![Maze Solution Demo](https://via.placeholder.com/600x400/2E3440/81A1C1?text=Reeborg+Solving+Maze)

*Reeborg successfully navigating through the maze using the right-hand rule*

## 🛠️ Installation & Setup

```bash
# No installation required! 
# Simply visit Reeborg's World in your browser
# Copy the code and paste it into the editor
```

## 🤝 Contributing

Feel free to:
- 🐛 Report bugs or issues
- 💡 Suggest improvements
- 🔀 Fork and create variations
- ⭐ Star if you found this helpful!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **👩‍🏫 Angela Yu** - For the amazing 100 Days of Code course
- **🤖 Reeborg's World** - For providing the educational platform
- **🏛️ Algorithm History** - Ancient maze-solving techniques inspiring modern CS

---

### 🔗 Connect & Follow

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/qusai-Kagalwala)
[![100 Days Progress](https://img.shields.io/badge/100_Days-Progress_Tracker-success?style=for-the-badge)](https://github.com/qusai-Kagalwala)

💻 *Built with ❤️ and ☕ during my Python learning adventure!*

**⭐ Star this repo if it helped you learn something new!**
