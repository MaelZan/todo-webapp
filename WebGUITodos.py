import streamlit as st
import Functions_for_todos


todos = Functions_for_todos.get_todos()

def add_todo():
    user_todo = st.session_state['new_todo'] + '\n'
    todos.append(user_todo)
    Functions_for_todos.write_todos(todos)


st.title("My Todo App")
st.write("Increase your productivity !")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions_for_todos.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a todo', placeholder='Add new todo ...',
              on_change=add_todo, key='new_todo')
