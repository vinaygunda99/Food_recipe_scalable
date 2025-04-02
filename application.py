from flask import Flask,redirect, request, render_template, jsonify,session,redirect,url_for,send_from_directory
from database import create_connection
import requests
from flask_session import Session
import os

app = Flask(__name__)
app.config["SESSION_TYPE"]="filesystem"
Session(app)
app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'
app=application

@app.route("/",methods=["GET","POST"])
def login():
    if 'username' in session:
        # return render_template("recipe.html")
        return redirect(url_for('recipe'))
    else:
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            
            if email and password:
                conn = create_connection()
                cur = conn.cursor()
                cur.execute("select * from user_master where user_email=%s and user_password=%s",(email, password))
                res = cur.fetchone()
                if res is None:
                    message='Wrong email/password'
                    return render_template("login.html",message=message )
                else:
                    session['username']=email
                    return redirect(url_for('recipe'))
            else:
                return "Data not found"
        else:
            return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup():
    if 'username' in session:
        return redirect(url_for('recipe'))
    else:
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            password = request.form.get("password")
            con_password = request.form.get("con-password")
            if password== con_password:
                
                if name and email and password:
                    conn = create_connection()
                    cur = conn.cursor()
                    cur.execute("select * from user_master where user_email=%s",(email,))
                    res = cur.fetchone()
                    if res is None:
                        cur.execute("insert into user_master (user_name, user_email, user_password) values (%s,%s,%s)",(name, email, password))
                        conn.commit()
                        cur.close()
                        return render_template("login.html" )
                    else:
                        session['username']=email
                        message='This mail already exist!'
                        return render_template("register.html",message=message )

                else:
                    message='check your cred'
                    return render_template("register.html",message=message )
            else:
                message="Check your password"
                return render_template("register.html",message=message)
            return render_template("login.html")
        else:
            return render_template("register.html")

@app.route("/recipe",methods=["GET","POST"])
def recipe():
    if 'username' in session:
        if request.method == 'POST':
            re_id=request.form.get('recipe_name')
            conn = create_connection()
            cur = conn.cursor()
            cur.execute("select * from recipe where recipe_id=%s",(re_id,))
            res = cur.fetchall()
            return render_template("recipe.html",res=res)
        else:
            if 'username' in session:
                return render_template("recipe.html")
            else:
                return render_template("login.html")
    else:
            return render_template("login.html")

@app.route("/translator",methods=["GET","POST"])
def translator():
    if 'username' in session:
        translated_text = None
        if request.method == "POST":
            name = request.form['r_name']
            ingredient = request.form['r_ing']
            procedure = request.form['r_pro']
            image=request.form['r_image']
            res=[(1,name,procedure,ingredient,image)]

            API_URL = "http://translationapi-x23302712.eba-kkxumgu2.ap-northeast-1.elasticbeanstalk.com/translate"

            try:
                ##translating the name
                json_data = {"text": name }
                response = requests.get(API_URL, json=json_data, stream=True)
                if response.status_code == 200:
                    data = response.json()
                    trans_name = data.get("Translated Text", "No text translated")
                    print("TRANSLATED TEXT ---------->> ",translated_text)
                else:
                    translated_text = "Failed to translate text. Error from API."
                ## Translating the ingredients
                json_data = {"text": ingredient }
                response = requests.get(API_URL, json=json_data, stream=True)
                if response.status_code == 200:
                    data = response.json()
                    trans_ing = data.get("Translated Text", "No text translated")
                    print("TRANSLATED TEXT ---------->> ",translated_text)
                else:
                    translated_text = "Failed to translate text. Error from API."
                # Translating the procedure
                json_data = {"text": procedure }
                response = requests.get(API_URL, json=json_data, stream=True)
                if response.status_code == 200:
                    data = response.json()
                    trans_pro = data.get("Translated Text", "No text translated")
                    print("TRANSLATED TEXT ---------->> ",translated_text)
                else:
                    translated_text = "Failed to translate text. Error from API."
            except Exception as e:
                translated_text = f"An error occurred: {str(e)}"
        return render_template("recipe.html",trans_name=trans_name,trans_pro=trans_pro,trans_ing=trans_ing,res=res)
    else:
            return render_template("login.html")

@app.route("/text_to_speech", methods=["GET", "POST"])
def text_to_speech():
    download_url = None
    API_URL = "http://scalable-api-x23301295.eba-2tmezkmp.ap-southeast-2.elasticbeanstalk.com/text-to-speech"

    if request.method == "POST":

        #translated text#
    
        trans_name = request.form['trans_name']
        trans_ing = request.form['trans_ing']
        trans_pro = request.form['trans_pro']
        text_input= f'recipe name {trans_name}, recipe ingredients {trans_ing} , recipe procedure {trans_pro}'
        
        #original text ### we are also taking original text beacuse we are calling same webpage which is requesting the original text in the begining as res
        name = request.form['r_name']
        ingredient = request.form['r_ing']
        procedure = request.form['r_pro']
        image=request.form['r_image']
        res=[(1,name,procedure,ingredient,image)]
        
        if text_input:
           
            json_data = {"text": text_input}
            try:
                response = requests.get(API_URL, json=json_data, stream=True)
            
                if response.status_code == 200:
                    
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'api_audio.mp3')
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                    
                    download_url = url_for('uploaded_file', filename='api_audio.mp3')
                else:   
                    download_url = "Error generating audio. Try again."
            except Exception as e:
                download_url = f"An error occurred: {str(e)}"
    
    return render_template("recipe.html", download_url=download_url,trans_name=trans_name,trans_pro=trans_pro,trans_ing=trans_ing,res=res)
    
@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename,as_attachment=True)


@app.route('/logout', methods=["GET","POST"] )
def logout():
    session.pop('username',None)
    return render_template("login.html")
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)