# main.py

todos = []


def add_todo(task):
    if not task.strip():
        print("待办事项不能为空！")
        return

    todos.append(task)
    print(f"添加成功：{task}")

def show_todos():
    if not todos:
        print("当前没有待办事项")
        return

    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task}")


if __name__ == "__main__":
    add_todo("学习 Git")
    add_todo("学习 merge")
    add_todo("学习 rebase")

    show_todos()