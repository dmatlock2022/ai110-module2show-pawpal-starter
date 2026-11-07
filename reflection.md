# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

The three main actions a user should be able to perform are:

1. Add and manage care tasks for their pet, such as walks, feeding, medication, or grooming.
2. Generate a daily schedule that considers things like task priority and available time.
3. View the daily plan and understand which tasks were selected and why.

My initial UML design had four main classes: Owner, Pet, Task, and Scheduler. I separated them based on what each part of the system was responsible for instead of putting everything into one class.

The Owner class stores information about the owner, their available time, and their pets. The Pet class stores basic information about each pet and keeps track of that pet's tasks. The Task class represents an individual care task and stores information like its title, duration, priority, frequency, completion status, and scheduled time. The Scheduler class is responsible for the scheduling logic, including getting tasks, sorting or filtering them, building a schedule, and checking for conflicts.

The relationships are that one Owner can have multiple Pets, and each Pet can have multiple Tasks. The Scheduler works with the Tasks to organize them into a daily plan. I kept the scheduling logic separate from the Pet and Owner classes because it seemed cleaner for each class to have one main responsibility.

### b. Design changes

My design changed a little during implementation. I added a `due_date` field to the Task class because recurring tasks needed a way to keep track of when the next occurrence should happen.

I also changed the Task completion behavior so Daily and Weekly tasks can create a new Task for their next occurrence. This was not something the original basic version of Task needed, but it became necessary when I added recurring-task logic.

The Scheduler also went from mostly empty method placeholders to having actual sorting, filtering, scheduling, and conflict-detection behavior.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

The main constraints my scheduler currently considers are the task priority, the amount of time the owner has available, the task's scheduled time, and whether the task has already been completed.

For the daily plan, priority and available time matter the most. A lower priority number means the task is more important. The scheduler sorts incomplete tasks by priority and then adds them to the daily plan as long as they still fit within the owner's available time.

For example, if the owner only has 40 minutes available, the scheduler will add the higher-priority feeding and medication tasks first. If adding a lower-priority 30-minute walk would go over the 40-minute limit, the walk is left out of the plan.

I chose this approach because it was simple to understand and still showed how a program can make decisions based on more than one constraint.

### b. Tradeoffs

For conflict detection, I used two loops to compare each task with the tasks after it and check whether they have the same scheduled time. AI suggested that I could use a dictionary to group tasks by time, which could be faster if there were a very large number of tasks.

I decided to keep the loop version because PawPal+ should only have a small number of pet-care tasks at a time, and the loop version was easier for me to understand and explain. The tradeoff is that the current version may be slower with a very large task list, but it keeps the code simpler for this project.

Another limitation is that conflict detection only checks whether two tasks have the exact same starting time. It does not calculate whether their durations overlap. This makes the method easier to understand, but a more advanced scheduler could compare both start times and durations.

---

## 3. AI Collaboration

### a. How you used AI

I used AI throughout the project for design ideas, checking my logic, debugging, and helping me think through the scheduler one feature at a time.

During the UML and class-design phase, AI helped me decide what responsibilities belonged in Owner, Pet, Task, and Scheduler. During implementation, I used AI to help with things like sorting tasks with `sorted()` and a lambda, recurring tasks using `date` and `timedelta`, and testing the scheduler.

The most useful prompts were specific questions about one feature at a time instead of asking AI to build the entire project. For example, asking how to sort Task objects by a time stored as an `HH:MM` string was more useful than asking it to rewrite the whole scheduler.

I also used separate stages of the conversation for design, implementation, testing, and documentation so I could focus on one part of the project at a time.

### b. Judgment and verification

One example where I did not accept an AI suggestion as-is was conflict detection. AI suggested that I could use a dictionary to group tasks by scheduled time. That could be more efficient, but I decided that the nested-loop version was easier for me to understand and better matched the size of this project.

I verified the code by running `main.py` and creating two tasks at 08:00. The scheduler correctly returned a conflict warning.

I also used automated tests instead of assuming the AI-generated logic was correct. After adding the scheduling features, I ran the test suite and confirmed that all six tests passed.

This helped me treat AI more like a tool that gives suggestions instead of something that should automatically make every design decision.

---

## 4. Testing and Verification

### a. What you tested

I tested the main behaviors of the PawPal+ system, including completing tasks, adding tasks to pets, sorting tasks by time, creating the next occurrence of a daily task, detecting scheduling conflicts, and building a schedule based on the owner's available time.

These tests were important because they cover the main parts of the scheduling logic instead of only checking whether the classes could be created.

I also manually tested the scheduler using `main.py`. I created tasks out of time order and confirmed that they were sorted correctly. I created two tasks at the same time and confirmed that a conflict warning appeared.

For the available-time constraint, I first tested the owner with 120 available minutes and confirmed that all four tasks fit. I then changed the available time to 40 minutes and confirmed that the lower-priority 30-minute walk was left out because it would exceed the available time.

### b. Confidence

I am very confident that the main scheduler features are working correctly because all six automated tests passed.

The current test result is:

```text
6 passed in 0.06s
```

If I had more time, I would add more edge-case tests, such as a pet with no tasks, multiple tasks with the same priority, a Weekly recurring task, tasks without scheduled times, and an owner with no available care time.

---

## 5. Reflection

### a. What went well

The part I am most satisfied with is that the project grew from a UML diagram and mostly empty class methods into a working system without completely changing the original design.

The Owner, Pet, Task, and Scheduler classes still have clear jobs, and the scheduler now handles sorting, filtering, recurring tasks, conflicts, priorities, and available time.

I also liked building the features one at a time because it made debugging easier. When something worked, I could test it before moving on to the next feature.

I was also able to connect the final scheduling logic back into the Streamlit interface so the user can actually see the daily plan and conflict warnings instead of the features only existing in the backend.

### b. What you would improve

If I had another iteration, I would improve the conflict-detection logic so it could detect overlapping tasks instead of only exact matching start times.

I would also improve recurring tasks so the scheduler manages adding the next recurring task automatically instead of only having `mark_complete()` return the new Task object.

Another improvement would be making the scheduling algorithm consider more preferences, such as preferred times of day or tasks that must happen before other tasks.

### c. Key takeaway

One important thing I learned is that designing the classes before writing all of the code made the project easier to manage. Having Owner, Pet, Task, and Scheduler already separated gave me a place to put each new feature without putting everything into one class.

I also learned that working with AI still requires me to make decisions. AI can suggest different ways to solve a problem, but I still need to understand the code, decide whether the suggestion makes sense for the project, and verify that it actually works.

For this project, being the lead architect meant deciding what the program should do, keeping the design understandable, testing the results, and using AI to help with individual problems instead of letting it make every decision for me.