from pawpal_system import Owner, Pet, Task, Scheduler


# Create owner
dylan = Owner("Dylan", 120)

# Create pets
mochi = Pet("Mochi", "Dog")
luna = Pet("Luna", "Cat")

# Create tasks
walk = Task("Morning Walk", 30, 2, "Daily")
feed_dog = Task("Feed Mochi", 10, 1, "Daily")
feed_cat = Task("Feed Luna", 10, 1, "Daily")

# Add tasks to pets
mochi.add_task(walk)
mochi.add_task(feed_dog)
luna.add_task(feed_cat)

# Add pets to owner
dylan.add_pet(mochi)
dylan.add_pet(luna)

# Get all tasks with the scheduler
scheduler = Scheduler()
tasks = scheduler.get_tasks(dylan)

# Print today's schedule
print("Today's Schedule")
print("----------------")

for task in tasks:
    print(f"- {task.title} ({task.duration_minutes} min, priority {task.priority})")