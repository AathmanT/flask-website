import os

from flask import Flask, render_template, request, send_file

app=Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/upload",methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, "upload/")

    if not os.path.isdir(target):
        os.mkdir(target)

    file = request.files['file']
    filename=file.filename
    if file:
        destination = "/".join([target, filename])
        file.save(destination)

    from_date=request.form.get("from")
    to_date=request.form.get("to")






    return render_template("index1.html")

@app.route("/viewResults")
def viewResults():
    return render_template("index1.html")

@app.route("/download")
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "static/02.png"
    return send_file(path, as_attachment=True)


if __name__=="__main__":
    app.run(debug=True)