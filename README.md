# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
**The game is a number guessing game. There's a secret number, you you got a limited amount of guesses. If your guess if greater than the secret number, the game tells you that it's too high. If the guess is less than the secret number, the game tells you that it's too low.**
- [x] Detail which bugs you found.
**The first bug was that the New Game wasn't resetting status. I added a st.session_state.status = "playing" inside the if new_game: block.**
**The second bug was that the hints were wrong on every other guess. On even-numbered attempts, the secret is cast ti a string (secret = str(st.session_state.secret)). Then check_guess(guess_int, secret) compares an int to a str, triggering the TypeError branch, which does string comparison. I removed the even/odd secret-casting logic and always pass st.session_state.secret directly.**
**The third bug was the score incrementing on wrong guesses. Update score was subtracting 5 for every "Too Low" guess, and alternates between +5/-5 for "Too High" guesses. I removed the "Too High" and "Too Low" branches from update_score so it only updates "Win"**
- [x] Explain what fixes you applied.
**Explanation added above**


## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]
**https://www.loom.com/share/436be25c1b354f4e8effce2ea840814c**

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
