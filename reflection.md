# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The three main actions a user should be able to perform are:

1. Add and manage care tasks for their pet, such as walks, feeding, medication, or grooming.
2. Generate a daily schedule that considers things like task priority and available time.
3. View the daily plan and understand which tasks were selected and why.

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design has four main classes: Owner, Pet, Task, and Scheduler. I separated them based on what each part of the system is responsible for instead of putting everything into one class.

The Owner class stores information about the owner, their available time, and their pets. The Pet class stores basic information about each pet and keeps track of that pet's tasks. The Task class represents an individual care task and stores information like its title, duration, priority, frequency, completion status, and scheduled time. The Scheduler class is responsible for the actual scheduling logic, including getting tasks, sorting or filtering them, building a schedule, and eventually checking for conflicts.

The relationships are that one Owner can have multiple Pets, and each Pet can have multiple Tasks. The Scheduler works with the Tasks to organize them into a daily plan. I kept the scheduling logic separate from the Pet and Owner classes because it seemed cleaner for each class to have one main responsibility.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
