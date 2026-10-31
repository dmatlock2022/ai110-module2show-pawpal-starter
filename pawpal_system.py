from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: int
    frequency: str
    completed: bool = False
    scheduled_time: Optional[str] = None

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


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
        pass

    def filter_tasks(self):
        pass

    def build_schedule(self, available_minutes: int):
        pass

    def detect_conflicts(self):
        pass