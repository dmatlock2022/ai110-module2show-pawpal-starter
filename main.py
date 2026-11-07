from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner
dylan = Owner("Dylan", 120)

# Create pets
mochi = Pet("Mochi", "Dog")
luna = Pet("Luna", "Cat")

# Create tasks
walk = Task(
    "Morning Walk",
    30,
    2,
    "Daily",
    scheduled_time="09:00"
)

feed_dog = Task(
    "Feed Mochi",
    10,
    1,
    "Daily",
    scheduled_time="08:00"
)

feed_cat = Task(
    "Feed Luna",
    10,
    1,
    "Daily",
    scheduled_time="07:30"
)

medicine = Task(
    "Give Luna Medicine",
    5,
    1,
    "Daily",
    scheduled_time="08:00"
)

# Add tasks to pets
mochi.add_task(walk)
mochi.add_task(feed_dog)
luna.add_task(feed_cat)
luna.add_task(medicine)

# Add pets to owner
dylan.add_pet(mochi)
dylan.add_pet(luna)

# Get all tasks with the scheduler
scheduler = Scheduler()
scheduler.get_tasks(dylan)

# Sort tasks by scheduled time
sorted_tasks = scheduler.sort_tasks()

print("Today's Schedule")
print("----------------")

for task in sorted_tasks:
    print(
        f"- {task.scheduled_time} "
        f"{task.title} "
        f"({task.duration_minutes} min, priority {task.priority})"
    )

# Show only incomplete tasks
print("\nIncomplete Tasks")
print("----------------")

incomplete_tasks = scheduler.filter_tasks()

for task in incomplete_tasks:
    print(f"- {task.title}")

    # Check for scheduling conflicts
print("\nSchedule Conflicts")
print("------------------")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for conflict in conflicts:
        print(f"WARNING: {conflict}")
else:
    print("No conflicts found.")