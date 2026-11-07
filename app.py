import streamlit as st
from datetime import time

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")

st.markdown(
    """
PawPal+ helps a pet owner keep track of pet-care tasks
and build a daily care plan.
"""
)


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------

# Keep the owner and scheduler between Streamlit reruns
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", 120)

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

owner = st.session_state.owner
scheduler = st.session_state.scheduler


# ---------------------------------------------------------
# Owner information
# ---------------------------------------------------------

st.subheader("Owner Information")

owner_name = st.text_input(
    "Owner name",
    value=owner.name
)

available_minutes = st.number_input(
    "Available care time today (minutes)",
    min_value=1,
    max_value=1440,
    value=owner.available_minutes
)

if st.button("Update owner"):
    owner.name = owner_name
    owner.available_minutes = int(available_minutes)

    st.success("Owner information updated.")


st.divider()


# ---------------------------------------------------------
# Pets
# ---------------------------------------------------------

st.subheader("Pets")

pet_name = st.text_input(
    "Pet name",
    value="Mochi"
)

species = st.selectbox(
    "Species",
    ["Dog", "Cat", "Other"]
)

if st.button("Add pet"):
    cleaned_name = pet_name.strip()

    if not cleaned_name:
        st.warning("Please enter a pet name.")

    elif any(
        pet.name.lower() == cleaned_name.lower()
        for pet in owner.pets
    ):
        st.warning("A pet with that name already exists.")

    else:
        new_pet = Pet(cleaned_name, species)
        owner.add_pet(new_pet)

        st.success(f"{cleaned_name} was added.")


if owner.pets:
    st.write("Current pets:")

    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species})")

else:
    st.info("No pets added yet.")


st.divider()


# ---------------------------------------------------------
# Tasks
# ---------------------------------------------------------

st.subheader("Pet Care Tasks")

if not owner.pets:
    st.info("Add a pet before creating tasks.")

else:
    selected_pet_name = st.selectbox(
        "Pet",
        [pet.name for pet in owner.pets]
    )

    selected_pet = next(
        pet
        for pet in owner.pets
        if pet.name == selected_pet_name
    )

    task_title = st.text_input(
        "Task title",
        value="Morning Walk"
    )

    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=20
    )

    priority_name = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    frequency = st.selectbox(
        "Frequency",
        ["Daily", "Weekly", "One-time"]
    )

    scheduled_time = st.time_input(
        "Scheduled time",
        value=time(8, 0)
    )

    priority_values = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    if st.button("Add task"):
        cleaned_title = task_title.strip()

        if not cleaned_title:
            st.warning("Please enter a task title.")

        else:
            new_task = Task(
                title=cleaned_title,
                duration_minutes=int(duration),
                priority=priority_values[priority_name],
                frequency=frequency,
                scheduled_time=scheduled_time.strftime("%H:%M")
            )

            selected_pet.add_task(new_task)

            st.success(
                f"{cleaned_title} was added for "
                f"{selected_pet.name}."
            )


# ---------------------------------------------------------
# Current tasks
# ---------------------------------------------------------

all_tasks = scheduler.get_tasks(owner)

if all_tasks:
    st.markdown("### Current Tasks")

    sorted_tasks = scheduler.sort_tasks()

    task_rows = []

    for task in sorted_tasks:
        pet_name_for_task = ""

        for pet in owner.pets:
            if task in pet.tasks:
                pet_name_for_task = pet.name
                break

        task_rows.append(
            {
                "Pet": pet_name_for_task,
                "Time": task.scheduled_time,
                "Task": task.title,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
                "Frequency": task.frequency,
                "Completed": task.completed
            }
        )

    st.table(task_rows)

else:
    st.info("No tasks added yet.")


st.divider()


# ---------------------------------------------------------
# Daily schedule
# ---------------------------------------------------------

st.subheader("Daily Plan")

if st.button("Generate schedule"):

    all_tasks = scheduler.get_tasks(owner)

    if not all_tasks:
        st.warning("Add at least one task first.")

    else:
        # Check for scheduling conflicts
        conflicts = scheduler.detect_conflicts()

        if conflicts:
            for conflict in conflicts:
                st.warning(conflict)

        # Build the daily plan
        daily_plan = scheduler.build_schedule(
            owner.available_minutes
        )

        if not daily_plan:
            st.info(
                "No incomplete tasks fit within the "
                "available care time."
            )

        else:
            st.success(
                f"{len(daily_plan)} task(s) were added "
                f"to today's plan."
            )

            st.write(
                "Higher-priority incomplete tasks are "
                "considered first, as long as they fit "
                "within the available care time."
            )

            plan_rows = []

            for task in daily_plan:
                pet_name_for_task = ""

                for pet in owner.pets:
                    if task in pet.tasks:
                        pet_name_for_task = pet.name
                        break

                plan_rows.append(
                    {
                        "Pet": pet_name_for_task,
                        "Time": task.scheduled_time,
                        "Task": task.title,
                        "Duration": task.duration_minutes,
                        "Priority": task.priority
                    }
                )

            st.table(plan_rows)