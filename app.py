from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Temporary storage for study tasks
study_tasks = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Study Planner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 60%;
            margin: 40px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input[type='text'], input[type='date'] {
            flex: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            background: #f9f9f9;
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .delete-btn {
            background-color: red;
            text-decoration: none;
            color: white;
            padding: 6px 10px;
            border-radius: 5px;
        }

        .delete-btn:hover {
            background-color: darkred;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Study Planner</h1>

    <form action="/add" method="POST">
        <input type="text" name="subject" placeholder="Enter subject or task" required>
        <input type="date" name="deadline" required>
        <button type="submit">Add Task</button>
    </form>

    <ul>
        {% for task in tasks %}
        <li>
            <span>
                <strong>{{ task.subject }}</strong> - Deadline: {{ task.deadline }}
            </span>
            <a href="/delete/{{ loop.index0 }}" class="delete-btn">Delete</a>
        </li>
        {% endfor %}
    </ul>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, tasks=study_tasks)


@app.route("/add", methods=["POST"])
def add_task():
    subject = request.form.get("subject")
    deadline = request.form.get("deadline")

    study_tasks.append({
        "subject": subject,
        "deadline": deadline
    })

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(study_tasks):
        study_tasks.pop(task_id)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
