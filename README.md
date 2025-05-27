# 🤖 Right-Hand Maze Solver

## 📚 Project Overview
This is my solution for **Day 6** of Angela Yu's **100 Days of Code** Python course! 🐍

Built for **Reeborg's World** maze challenges, this algorithm uses the classic **right-hand rule** to navigate through any simply-connected maze. 

## 🎯 How It Works
The robot follows these simple rules:
1. 🔄 **Always try to turn right first** - if the right side is clear, turn right and move
2. ➡️ **Go straight** - if the front is clear but right is blocked, move forward  
3. ↩️ **Turn left** - if both right and front are blocked, turn left to find a new path

## 🧠 The Algorithm Logic
```python
while not at_goal():
    if right_is_clear():        # 🔄 Priority 1: Turn right
        turn_right()
        move()
    elif front_is_clear():      # ➡️ Priority 2: Go straight
        move()
    else:                       # ↩️ Priority 3: Turn left
        turn_left()
```

## 🏃‍♂️ Why Right-Hand Rule?
The right-hand rule is like walking through a maze with your right hand always touching the wall - you'll eventually find the exit! It's guaranteed to work for any maze without loops (simply-connected mazes). 🌟

## 🛠️ Built With
- **Python** 🐍
- **Reeborg's World** environment 🌍
- Love for problem-solving! ❤️

## 🚀 Usage
Simply run this code in Reeborg's World maze levels and watch the robot navigate to the goal automatically!

## 📝 Part of My Coding Journey
This project represents Day 6 of my 100 Days of Code challenge with Angela Yu. Each day I'm building my Python skills one project at a time! 💪

## 🎉 Connect With Me
Feel free to check out my other 100 Days of Code projects and follow my coding journey!

---
*Made with 💻 and ☕ during my Python learning adventure!*
