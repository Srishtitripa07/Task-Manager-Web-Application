from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
host="localhost",
user="root",
password="Tripathi#12345",
database="task_manager"
)

cursor = db.cursor()

@app.route("/")
def index():

    search = request.args.get("search")

    if search:
        cursor.execute("""
        SELECT tasks.*, users.name 
        FROM tasks
        LEFT JOIN users ON tasks.created_by = users.id
        WHERE title LIKE %s
        """,('%'+search+'%',))
    else:
        cursor.execute("""
        SELECT tasks.*, users.name
        FROM tasks
        LEFT JOIN users ON tasks.created_by = users.id
        ORDER BY tasks.id DESC
        """)

    tasks = cursor.fetchall()

    return render_template("index.html",tasks=tasks,search=search)


@app.route("/create",methods=["GET","POST"])
def create():

    if request.method=="POST":

        title=request.form["title"]
        description=request.form["description"]
        due_date=request.form["due_date"]
        status=request.form["status"]
        remarks=request.form["remarks"]

        sql="""
        INSERT INTO tasks
        (title,description,due_date,status,remarks,created_by,updated_by)
        VALUES(%s,%s,%s,%s,%s,1,1)
        """

        cursor.execute(sql,(title,description,due_date,status,remarks))
        db.commit()

        return redirect("/")

    return render_template("create_task.html")


@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id):

    if request.method=="POST":

        title=request.form["title"]
        description=request.form["description"]
        due_date=request.form["due_date"]
        status=request.form["status"]
        remarks=request.form["remarks"]

        sql="""
        UPDATE tasks
        SET title=%s,
        description=%s,
        due_date=%s,
        status=%s,
        remarks=%s,
        updated_by=1
        WHERE id=%s
        """

        cursor.execute(sql,(title,description,due_date,status,remarks,id))
        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM tasks WHERE id=%s",(id,))
    task=cursor.fetchone()

    return render_template("edit_task.html",task=task)


@app.route("/delete/<int:id>")
def delete(id):

    cursor.execute("DELETE FROM tasks WHERE id=%s",(id,))
    db.commit()

    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)