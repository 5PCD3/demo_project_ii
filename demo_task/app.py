from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb+srv://pcd:mypassword@cluster0.1oyubnl.mongodb.net/?retryWrites=true&w=majority')
db = client['coursify']
developer_col = db['developer']
job_col = db['job']

@app.route("/", methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        form_data = request.form

        if "company_name" in form_data:
            # Form data from the "Need Developers" form
            try:
                company_name = form_data['company_name']
                role = form_data['role']
                salary = form_data['salary']
                experience = form_data['experience']
                about_organization = form_data['about_organization']

                job_details = {
                    "company_name": company_name,
                    "role": role,
                    "salary": salary,
                    "experience": experience,
                    "about_organization": about_organization
                }

                job_col.insert_one(job_details)

            except KeyError as e:
                return f"Error: Missing form field - {e}"

        elif "first_name" in form_data:
            # Form data from the "Search Jobs" form
            try:
                first_name = form_data.get('first_name', '')
                last_name = form_data.get('last_name', '')
                experience = form_data.get('experience', '')
                email = form_data.get('email', '')
                role_search = form_data.get('role_search', '')
                skills_required = 'skills_required' in form_data
                current_ctc = form_data.get('current_ctc', '')
                desired_ctc = form_data.get('desired_ctc', '')
                location = form_data.get('location', '')
                developer_data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "experience": experience,
                    "email": email,
                    "role_search": role_search,
                    "skills_required": skills_required,
                    "current_ctc": current_ctc,
                    "desired_ctc": desired_ctc,
                    "location": location
                }

                developer_col.insert_one(developer_data)

            except KeyError as e:
                return f"Error: Missing form field - {e}"

    # Return the rendered template
    
    return render_template("index.html")

if __name__ == "__main__":

    app.run(host="0.0.0.0")
    #while True:

        #app.run(host="0.0.0.0")
      #  time.sleep(8)