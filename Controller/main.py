from flask import Flask, render_template, request, redirect,url_for
import pymysql as pmy
from Kwic_Modules import *
from Model import db
from file_upload import *
from Search_data import *

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__,template_folder='../View/templates', static_folder='../View/static')


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call 
# the associated function.
@app.route('/',methods=['GET','POST'])
# ‘/’ URL is bound with hello_world() function.
def homepage():
    if request.method=="POST":
        keywords = request.form['keywords'].lower().split()
        search=request.form['submit']
        # if search=="Submit":
        #     return render_template("Search_Result.html")
        return render_template("Homepage.html", results="done")
    if request.method == "GET":
        return render_template("Homepage.html")

@app.route('/upload',methods=['GET','POST'])
def file_upload():
    # Logic for the file upload page
    if request.method=="POST": # Checks if the POST method is used
        uploaded_file=request.files['file']
        if uploaded_file:
            file_content = uploaded_file.read().decode("utf-8")
            f=File_Upload()
            try:
                f.upload_file(file_content)
                return render_template('File_Upload.html', file_uploaded=True)
            except Exception as e:
                file_upload_error = str(e)
        else:
            return render_template('File_Upload.html',file_uploaded=False)
    return render_template('File_Upload.html', file_uploaded=False)

@app.route('/search',methods=['GET',"POST"])
def search():
    if request.method=="POST":
        keywords = request.form['keywords']
        # print(keywords.split())
        s=Search()
        print(keywords)
        result=s.search_data(keywords.split())
        return render_template('Search_Result.html',Web_links=result)
    return render_template('Search_Result.html')

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()