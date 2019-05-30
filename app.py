import os,time
import qttest

from flask import Flask, render_template, request, send_file

import blei_executable_and_tethne,FilterTweetDataByMonth,plotting,FilterTweetDataByDate,FilterTweetDataByYear

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
    #if not(".txt" in file.filename or ".csv" in file.filename):
    if not (".txt" in file.filename):
        return render_template("file Error.html")
    if file:
        destination = "/".join([target, filename])
        file.save(destination)
    form=request.form
    start_time=time.time()
    type=request.form.get("type")

    if(type=="Month"):
        from_date=request.form.get("from")
        to_date=request.form.get("to")
        year=request.form.get("year")

        time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        try:
            time_stamps=time_stamps[int(from_date):int(to_date)+1]
        except Exception:
            return render_template("Time Error.html")

        if (FilterTweetDataByMonth.preprocess("upload/" + filename, year, time_stamps)):
            blei_executable_and_tethne.make_csv(time_stamps, type)
            plotting.plot(time_stamps, type)

        else:
            return render_template("data Error.html")



    elif(type=="Year"):
        from_year = request.form.get("FromYear")
        from_year=int(from_year)
        to_year = request.form.get("ToYear")
        to_year = int(to_year)

        time_stamps=[]

        try:
            for i in range(from_year, to_year+1):
                time_stamps.append(str(i))
        except Exception:
            return render_template("Time Error.html")

        if (FilterTweetDataByYear.preprocess("upload/" + filename, time_stamps)):
            blei_executable_and_tethne.make_csv(time_stamps, type)
            plotting.plot(time_stamps, type)
        else:
            return render_template("data Error.html")



    elif (type == "Date"):

        from_date_list = request.form.get("FromDate")
        from_date_list = from_date_list.split("-")
        from_date=int(from_date_list[2])


        to_date_list = request.form.get("ToDate")
        to_date_list = to_date_list.split("-")
        to_date=int(to_date_list[2])

        year="2019"
        month="Feb"

        time_stamps = []

        try:
            for i in range(from_date, to_date + 1):
                time_stamps.append(str(i))
        except Exception:
            return render_template("Time Error.html")

        if (FilterTweetDataByDate.preprocess("upload/" + filename,year ,month,time_stamps)):
            blei_executable_and_tethne.make_csv(time_stamps, type)
            plotting.plot(time_stamps, type)
        else:
            return render_template("data Error.html")




    print("time elapsed : ",time.time()-start_time)
    return render_template("index1.html",fileExists=True)

@app.route("/viewResults")
def viewResults():
    if os.path.isfile(APP_ROOT+"/static/03.png"):
        print(True)
        return render_template("index1.html",fileExists=True)
    else:
        return render_template("index1.html",fileExists=False)

@app.route("/download")
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "static/03.png"
    return send_file(path, as_attachment=True)


def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

if __name__=="__main__":
    # app.run(debug=True)
    qttest.main(app)