# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment
## In this section, students will provide their initial thoughts on the project assignment, including their understanding of the requirements, any assumptions they made, points that need clarification, and their overall approach to tackling the project.
## Initial Thoughts
I thought we would just make the standard script with loops and input functions.
## Assumptions Made
I assumed the AI would just write the enitire script and tests for me in one go without me having to think too much about the architecture. I also assumed the agent would eventually start to 'hallucinate' and get multiple errors but it remained working fine.
## Points Needing Clarification
As there were no global values, I needed calrification to seperate parts of the code that are game logic and parts that are the game's UI.

# Key Learnings
## Here, students will summarize the most important things they learned while working on the project. This could include computer science related concepts, technical skills, insights about using CoPilot effectively, and any new concepts or tools they encountered
## Computer Science Concepts and Technical Skills
I got more practice coding functions and its my first experience writing tests using the Arrange, Act, Assert pattern.
## Insights about Using CoPilot Effectively
I learned that Copilot is way more useful and efficient when you use it to learn or tutor you compared to standard LLMs.
## New Concepts or Tools Encountered
Using Pytest, and seeing how Copilot can read multiple files in my workspace to write a README or update my JOURNAL seems like a cool workflow.

# Report on CoPilot Prompting Experience
## Student may pull examples from the JOURNAL.md to illustrate their experience, including specific interactions that were particularly helpful or challenging.
### Types of prompts that worked well
Asking it to read the current code and generate documentation based on it like when I asked it to write the README and explain how to run the tests gave good results.
### Types of prompts that did not work well or failed
Broad prompts don't work well because the AI does the most common way of doing things and not pay attention to the assignment constraints.

# Limitations, Hallucinations and Failures
## In this section, students will document any instances where CoPilot provided incorrect or misleading information (hallucinations) or where it failed to provide a useful response. They will analyze why these issues occurred and how they impacted their work on the project.
## For example: Fabricated APIs, Deprecated functions, Subtle logical errors, Confident but wrong explanations, Over-engineered solutions, Under-engineered solutions, overcomplicated code, oversimplified code, etc.
## Examples of Hallucinations or Failures or Misleading Information or Confident but Wrong Explanations, or Over-engineered or Under-engineered Solutions
I did not experience any of this, but I did see one typo from the AI's response, also there are failures to this instruction "update the journal with the latest interactions" , when it has not been prompted for a few responses.
## Analysis of Why These Issues Occurred
I think LLMs make typos when trying to generate fast responses. And I think the agent fails to continuously update the journal when asking it more about the scripts code and logic, the chats longer history might also cause this. 
## Impact on the Project
It had minimal impact as the typo was still understandable and for the journal logging, I could just remind it every time it stops. 

# AI Trust
## When did I trust the AI?
I fully trusted the AI for writing comments in the files, updating my journal, and generating the framework for my unit tests.
## When did I stop trusting it?
I stopped trusting it to automatically remember all the constraints without being reminded.
## What signals or situations or patterns indicated low reliability?
Whenever the agent stops journal logging the interactions, I am reminded that its attention diverts from past instructions. 

# What I Learned
## What did you learn about software development?
I learned that software development isn't just writing code, it also includes lots of planning and handling of edge cases. 
## What did you learn about using AI tools?
They are great for speed, but you really need to understand what its generating and what your goal is using strong prompts and validations.
## When should you trust AI? When should you double-check it?
Trust AI for syntax, documentation, and generating new ideas. Double-check its logic, conditions, and specific constraints.

# Reflection
## Did AI make you faster? Why or why not?
Yes, it definitely made me faster. Having the AI format my journal, write the README, and plan the test functions saved me time so I only mainly had to focus on the logic.
## Did you feel in control of the code?
I felt in control because the agent didn't just give me answers so I couldn't just copy-paste. I had to validate the rules and invariants.
## Would you use AI the same way next time? What would you change?
Next time, I think it would be more efficientr to establish the project structure earlier. I would tell the AI to set up my logic, UI, and test files separately from the start.