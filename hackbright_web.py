"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    row = hackbright.get_grade_by_github(github)
    print(row)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           row=row)

    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-form")
def student_display_form():
    """Add a student."""

    return render_template("student_add.html")

@app.route("/student-add", methods=["POST"])
def student_info_confirm():
    """Prints out the student info to confirm and thank."""

    first_name = request.form.get('first')
    last_name = request.form.get('last')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_add_result.html", first_name = first_name, 
                            last_name = last_name, github = github)




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
