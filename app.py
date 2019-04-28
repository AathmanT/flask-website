import os
from flask import Flask, render_template, request, send_file

import blei_executable_and_tethne,FilterTweetData,plotting

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
    if not(".txt" in file.filename or ".csv" in file.filename):

        return render_template("file Error.html")
    if file:
        destination = "/".join([target, filename])
        file.save(destination)

    from_date=request.form.get("from")
    to_date=request.form.get("to")

    time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    time_stamps=time_stamps[int(from_date):int(to_date)+1]

   # FilterTweetData.preprocess(time_stamps)
   # blei_executable_and_tethne.make_csv(time_stamps)
   # plotting.plot(time_stamps)

    return render_template("index1.html")

@app.route("/viewResults")
def viewResults():
    return render_template("index1.html")

@app.route("/download")
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "static/03.png"
    return send_file(path, as_attachment=True)


if __name__=="__main__":
    app.run(debug=True)