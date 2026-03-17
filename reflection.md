# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
**1. The New Game button isn't working: The game was supposed to reset when the button is pressed, but it just stays in its current state**
**2. Hints don't match the expectation: Hints seem to be alternating between Go Higher and Go Lower despite whether the input is higher or lower than the secret number**
**3. The score keeps decrementing into the negatives: the score was supposed to stay at zero and increment when the player guesses the number, since the game is based on the number of trials given to the player, not how many times they quessed the right number**
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

**I used CLaude AI. Claude pointed out that New Game doesn't reset status. The new_game blocks resets attempts and secret, but never resets st.session_state.status. I read over the lines Claude said had errors and it's right.**

****

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
**I rerun the code multiple times after fixing the bug. First I run the test_game_logic.py with pytest, after all the tests passed, I run the gaem to see if the updates are reflected on it.**
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  **I run the check_guess function and it turned out, the only output needed were the words, "win", "Too High", and "Too Low." But the code was adding extra details such as "Go Lower/Higher" and "Great".**
- Did AI help you design or understand any tests? How?
**Yes. The error on decrementing/incrementing score was a little bit confusing, and Claude helped me understand the logic behind it as well as designing the tests for it.**

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
**Streamlit reruns the entire script, everytime something happens in the app. This leads to irregular updates of variable states, which might make the app behave unpredictably. This issue is solved by st.session_state, a dictionary that survives reruns. i.e. anything stored there sticks around between script executions for that user's session.**

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
**Writing the tests myself and then following errors to debug.**
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
**I wouldn't ask an AI agent to point out potential bugs in the code before I do it myself.**
- In one or two sentences, describe how this project changed the way you think about AI generated code.
**I realized that if you already have a starter code, it's easy for AI to give you accurate code.**
