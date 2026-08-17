from flask import Flask, render_template, request, redirect, abort
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="computer_inventory"
    )
    return connection


@app.route("/")
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM computers")
    computers = cursor.fetchall()

    cursor.close()
    connection.close()

    is_admin = request.remote_addr == "127.0.0.1"

    return render_template(
        "index.html",
        computers=computers,
        is_admin=is_admin
    )

@app.route("/add", methods=["GET", "POST"])
def add_computer():

    if request.method == "POST":

        asset_name = request.form["asset_name"]
        serial_number = request.form["serial_number"]
        brand = request.form["brand"]
        model = request.form["model"]
        os = request.form["os"]
        location = request.form["location"]
        status = request.form["status"]

        connection = get_db_connection()
        cursor = connection.cursor()

        sql = """
            INSERT INTO computers
            (asset_name, serial_number, brand, model, os, location, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            asset_name,
            serial_number,
            brand,
            model,
            os,
            location,
            status
        )

        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()

        return redirect("/")

    return render_template("add.html")
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_computer(id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":

        asset_name = request.form["asset_name"]
        serial_number = request.form["serial_number"]
        brand = request.form["brand"]
        model = request.form["model"]
        os = request.form["os"]
        location = request.form["location"]
        status = request.form["status"]

        sql = """
            UPDATE computers
            SET asset_name = %s,
                serial_number = %s,
                brand = %s,
                model = %s,
                os = %s,
                location = %s,
                status = %s
            WHERE id = %s
        """

        values = (
            asset_name,
            serial_number,
            brand,
            model,
            os,
            location,
            status,
            id
        )

        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()

        return redirect("/")

    cursor.execute(
        "SELECT * FROM computers WHERE id = %s",
        (id,)
    )

    computer = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("edit.html", computer=computer)
@app.route("/delete/<int:id>")
def delete_computer(id):

    if request.remote_addr != "127.0.0.1":
        abort(403)

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM computers WHERE id = %s",
        (id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)