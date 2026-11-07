from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: int
    frequency: str
    completed: bool = False
    scheduled_time: Optional[str] = None
    due_date: Optional[date] = None

    def mark_complete(self):
        """Mark the task complete and create the next recurring task."""
        self.completed = True

        if self.frequency.lower() == "daily":
            return Task(
                title=self.title,
                duration_minutes=self.duration_minutes,
                priority=self.priority,
                frequency=self.frequency,
                scheduled_time=self.scheduled_time,
                due_date=date.today() + timedelta(days=1)
            )

        if self.frequency.lower() == "weekly":
            return Task(
                title=self.title,
                duration_minutes=self.duration_minutes,
                priority=self.priority,
                frequency=self.frequency,
                scheduled_time=self.scheduled_time,
                due_date=date.today() + timedelta(days=7)
            )

        return None


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)


class Owner:
    def __init__(self, name: str, available_minutes: int):
        self.name = name
        self.available_minutes = available_minutes
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks from all of the owner's pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.tasks)

        return all_tasks


class Scheduler:
    def __init__(self):
        self.tasks: list[Task] = []

    def get_tasks(self, owner: Owner):
        """Get all pet-care tasks for an owner."""
        self.tasks = owner.get_all_tasks()
        return self.tasks

    def sort_tasks(self):
        """Sort tasks by their scheduled time."""
        self.tasks = sorted(
            self.tasks,
            key=lambda task: task.scheduled_time or "23:59"
        )
        return self.tasks

    def filter_tasks(self, completed=False):
        """Return tasks based on completion status."""
        return [
            task
            for task in self.tasks
            if task.completed == completed
        ]

    def build_schedule(self, available_minutes: int):
        """Build a schedule using priority and available time."""
        schedule = []
        time_used = 0

        # Lower priority number means the task is more important
        incomplete_tasks = self.filter_tasks(completed=False)
        priority_tasks = sorted(
            incomplete_tasks,
            key=lambda task: task.priority
        )

        for task in priority_tasks:
            if time_used + task.duration_minutes <= available_minutes:
                schedule.append(task)
                time_used += task.duration_minutes

        return schedule

    def detect_conflicts(self):
        """Find tasks that are scheduled at the same time."""
        conflicts = []

        for i in range(len(self.tasks)):
            for j in range(i + 1, len(self.tasks)):
                first_task = self.tasks[i]
                second_task = self.tasks[j]

                if (
                    first_task.scheduled_time
                    and first_task.scheduled_time == second_task.scheduled_time
                ):
                    conflicts.append(
                        f"Conflict: {first_task.title} and "
                        f"{second_task.title} are both scheduled at "
                        f"{first_task.scheduled_time}"
                    )

        return conflicts