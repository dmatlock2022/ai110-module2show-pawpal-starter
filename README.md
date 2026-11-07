# PawPal+ (Module 2 Project)

PawPal+ is a Streamlit app that helps a pet owner organize care tasks and create a daily plan.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks such as walks, feeding, medication, enrichment, and grooming
- Consider constraints such as available time and task priority
- Produce a daily plan
- Warn about scheduling conflicts
- Keep track of recurring tasks

The goal of PawPal+ is to organize pet-care tasks in one place and use simple scheduling logic to help the owner decide what needs to be done.

## What PawPal+ Can Do

The project currently includes:

- Owner, Pet, Task, and Scheduler classes
- Adding pets and tasks
- Task duration and priority
- Daily and weekly recurring tasks
- Sorting tasks by scheduled time
- Filtering completed and incomplete tasks
- Detecting tasks scheduled at the same time
- Building a daily plan based on priority and available time
- Automated tests for the main scheduling behaviors
- A Streamlit interface connected to the backend classes

## Getting Started

### Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

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

Run the command-line example:

```bash
python main.py
```

## Project Design

The system uses four main classes:

- `Owner` stores the owner's information, available care time, and pets.
- `Pet` stores the pet's information and its care tasks.
- `Task` represents one care task and stores information such as duration, priority, frequency, completion status, scheduled time, and due date.
- `Scheduler` handles sorting, filtering, building the daily plan, and detecting conflicts.

One Owner can have multiple Pets, and each Pet can have multiple Tasks.

The Scheduler works with the tasks from the owner's pets instead of storing pet information itself.

## 🖥️ Sample Output

Running `main.py` produces output similar to:

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

Daily Plan
----------
- Feed Luna (10 min, priority 1)
- Feed Mochi (10 min, priority 1)
- Give Luna Medicine (5 min, priority 1)
- Morning Walk (30 min, priority 2)
```

The daily plan changes depending on how much care time the owner has available.

For example, when the owner only has 40 minutes available, the higher-priority tasks are selected first and the 30-minute Morning Walk is left out because it would exceed the available time.

## 📐 Smarter Scheduling

| Feature | Method(s) | Description |
|---|---|---|
| Task sorting | `sort_tasks()` | Sorts tasks by scheduled time so earlier tasks appear first |
| Filtering | `filter_tasks()` | Returns completed or incomplete tasks |
| Daily planning | `build_schedule()` | Selects incomplete tasks based on priority and available time |
| Conflict handling | `detect_conflicts()` | Warns when two tasks have the same scheduled time |
| Recurring tasks | `mark_complete()` | Creates the next occurrence of Daily or Weekly tasks |

### Sorting

Tasks are sorted using their `scheduled_time`.

For example:

```text
07:30
08:00
09:00
```

Tasks without a scheduled time are placed at the end of the sorted list.

### Filtering

Tasks can be filtered using their completion status.

The scheduler can return incomplete tasks or completed tasks.

### Daily Plan

The daily plan uses two main constraints:

1. Task priority
2. The owner's available time

A lower priority number means the task is more important.

The scheduler first considers higher-priority tasks and adds them to the plan if they fit within the amount of time the owner has available.

### Conflict Detection

The scheduler compares task times and reports a conflict when two tasks have the same scheduled time.

Example:

```text
WARNING: Conflict: Feed Mochi and Give Luna Medicine are both scheduled at 08:00
```

The conflict detection is intentionally simple. It checks for exact matching times instead of calculating whether the full duration of two tasks overlaps.

### Recurring Tasks

When a Daily task is completed, a new version of the task is created with a due date one day later.

When a Weekly task is completed, a new version is created with a due date seven days later.

One-time tasks do not create another task.

## 🧪 Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The current tests verify:

- Task completion
- Adding a task to a pet
- Sorting tasks by scheduled time
- Daily recurring task behavior
- Schedule conflict detection
- Building a schedule with an available-time limit

Latest test result:

```text
6 passed in 0.06s
```

**Confidence Level: ★★★★★**

The automated tests cover the main behaviors that have been implemented so far.

## 📸 Demo Walkthrough

1. Start the Streamlit app.
2. Enter the owner's name and available care time.
3. Add one or more pets.
4. Select a pet and create care tasks with a title, duration, priority, and frequency.
5. View the pets and tasks currently stored in the app.
6. The backend can sort tasks by time, filter them by completion status, create recurring tasks, detect scheduling conflicts, and build a daily plan based on available time and priority.

The final Streamlit interface directly uses the scheduler to sort tasks, build the daily plan, respect the owner's available time, and display scheduling conflicts with warning messages.