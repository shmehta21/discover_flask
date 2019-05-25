
##########################
###### imports ##########
#########################
from project import app, db
from project.models import BlogPost
from project.home.forms import MessageForm
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
#from functools import wraps

########################
###### config ##########
########################
home_blueprint = Blueprint('home', __name__, template_folder='templates')



###################################
####### helper functions ##########
###################################
'''
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('users.login'))

	return wrap
'''

#######################
###### routes #########
#######################

@home_blueprint.route('/', methods=['GET','POST'])
@login_required
def home():
	error = None
	form = MessageForm(request.form)
	if form.validate_on_submit():
		new_message = BlogPost(
				form.title.data,
				form.description.data,
				current_user.id
			)
		db.session.add(new_message)
		db.session.commit()
		flash('New entry was successfully posted. Thanks!')
		return redirect(url_for('home.home'))

	else:
		posts = BlogPost.query.filter_by(author_id=current_user.id)
		return render_template('index.html', posts=posts, form=form, error=error)

@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html')
