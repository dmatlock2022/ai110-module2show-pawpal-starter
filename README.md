# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

My goal with PawPal+ is to organize pet-care tasks in one place and use simple scheduling logic to help the owner keep track of what needs to be done.

## What You Will Build

The final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks with duration and priority
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly
- Include tests for the most important scheduling behaviors

## Getting Started

### Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

## Suggested Workflow

1. Read the scenario and identify the main requirements.
2. Draft a UML diagram with the main classes and relationships.
3. Convert the UML into Python class stubs.
4. Implement the scheduling logic in small steps.
5. Add tests for the main behaviors.
6. Connect the Python classes to the Streamlit UI.
7. Update the UML if the final design changes.

## 🖥️ Sample Output

```text
Today's Schedule
----------------
- 07:30 Feed Luna (10 min, priority 1)
- 08:00 Feed Mochi (10 min, priority 1)
- 08:00 Give Luna Medicine (5 min, priority 1)
- 09:00 Morning Walk (30 min, priority 2)

Incomplete Tasks
----------------
- Feed Luna
- Feed Mochi
- Give Luna Medicine
- Morning Walk

Schedule Conflicts
------------------
WARNING: Conflict: Feed Mochi and Give Luna Medicine are both scheduled at 08:00
```

## 🧪 Testing PawPal+

Run the full test suite:

```bash
python -m pytest
```

The current tests verify basic task completion and adding tasks to pets.

Current test result:

```text
2 passed
```

Additional scheduler tests will be added for sorting, recurring tasks, and conflict detection.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---|---|---|
| Task sorting | `sort_tasks()` | Sorts tasks by scheduled time so earlier tasks appear first |
| Filtering | `filter_tasks()` | Can return completed or incomplete tasks |
| Conflict handling | `detect_conflicts()` | Warns when two tasks have the same scheduled time |
| Recurring tasks | `mark_complete()` | Daily tasks create a new task for the next day and weekly tasks create one seven days later |

The scheduling logic was kept simple so it is easy to understand and test. For example, conflict detection uses two loops to compare task times. A dictionary could be more efficient for a very large number of tasks, but the loop approach is easier to follow and works well for the small number of tasks expected in PawPal+.

## 📸 Demo Walkthrough

1. Start the Streamlit app and enter the owner's name and available care time.
2. Add pets by entering a pet name and selecting the species.
3. Select a pet and create care tasks with a title, duration, priority, and frequency.
4. View the pets and tasks that have been added to the app.
5. Use the scheduler to work with the owner's current pet-care tasks.
6. The backend can sort tasks by scheduled time, filter tasks by completion status, create future occurrences for recurring tasks, and identify scheduling conflicts.

**Screenshot or video:** Optional.