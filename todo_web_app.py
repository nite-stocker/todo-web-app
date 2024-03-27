import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Too Doo")
st.subheader("Add or complete a todo.")

st.text_input(label="Add todo",
              label_visibility="hidden",
              placeholder="Enter a todo",
              on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
