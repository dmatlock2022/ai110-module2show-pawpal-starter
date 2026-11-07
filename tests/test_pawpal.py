from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Morning Walk", 30, 2, "One-time")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Mochi", "Dog")
    task = Task("Morning Walk", 30, 2, "Daily")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task


def test_task_sorting():
    scheduler = Scheduler()

    task1 = Task(
        "Morning Walk",
        30,
        2,
        "Daily",
        scheduled_time="09:00"
    )

    task2 = Task(
        "Feed Pet",
        10,
        1,
        "Daily",
        scheduled_time="07:30"
    )

    scheduler.tasks = [task1, task2]

    sorted_tasks = scheduler.sort_tasks()

    assert sorted_tasks[0] == task2
    assert sorted_tasks[1] == task1


def test_daily_recurrence():
    task = Task(
        "Morning Walk",
        30,
        2,
        "Daily"
    )

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task.due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    scheduler = Scheduler()

    task1 = Task(
        "Feed Mochi",
        10,
        1,
        "Daily",
        scheduled_time="08:00"
    )

    task2 = Task(
        "Give Luna Medicine",
        5,
        1,
        "Daily",
        scheduled_time="08:00"
    )

    scheduler.tasks = [task1, task2]

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1


def test_build_schedule_with_time_limit():
    owner = Owner("Dylan", 40)
    pet = Pet("Mochi", "Dog")

    feed = Task("Feed Mochi", 10, 1, "Daily")
    medicine = Task("Medicine", 5, 1, "Daily")
    walk = Task("Morning Walk", 30, 2, "Daily")

    pet.add_task(feed)
    pet.add_task(medicine)
    pet.add_task(walk)
    owner.add_pet(pet)

    scheduler = Scheduler()
    scheduler.get_tasks(owner)

    schedule = scheduler.build_schedule(owner.available_minutes)

    assert feed in schedule
    assert medicine in schedule
    assert walk not in schedule