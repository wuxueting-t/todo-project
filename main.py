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


# 必须先定义 main 函数
def main():
    while True:
        print("\n======== Todo 管理系统 ========")
        print("1. 添加待办")
        print("2. 查看待办")
        print("3. 退出程序")

        choice = input("请选择操作：")

        if choice == "1":
            task = input("请输入待办事项：")
            add_todo(task)

        elif choice == "2":
            show_todos()

        elif choice == "3":
            print("退出 Todo 管理系统！")
            break

        else:
            print("无效选择，请重新输入！")


# 最后才调用 main
if __name__ == "__main__":
    main()
    