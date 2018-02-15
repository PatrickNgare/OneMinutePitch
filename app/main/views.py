from flask import render_template, request, redirect, url_for, abort  
from . import main  
from .forms import CommentsForm, PitchForm
from ..models import Comment, Pitch, User, PitchCategory
from flask_login import login_required, current_user
from .. import db




@main.route('/')
def index():
   

    
    pitches= Pitch.get_all_pitches()  
    title='Pitch Deck'
    search_pitch = request.args.get('pitch_query')

    return render_template('index.html', pitches= pitches)

#this section consist of the category root functions

@main.route('/inteview/pitches/')
def interview():
    
    pitches= Pitch.get_all_pitches()
    
    return render_template('interview.html', pitches= pitches )

@main.route('/picklines/pitches/')
def pick_up_line():
    

    pitches= Pitch.get_all_pitches()

    return render_template('picklines.html', pitches= pitches )

@main.route('/promotion/pitches/')
def promotion():
    

    pitches= Pitch.get_all_pitches()

    return render_template('promotion.html', pitches= pitches )


@main.route('/product/pitches/')
def product():
    
    pitches= Pitch.get_all_pitches()
    return render_template('product.html', pitches= pitches )
 


@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    pitch_comments = Comment.get_comments(pitch_id)

    return render_template('pitch.html',title= title ,found_pitch= found_pitch, pitch_comments= pitch_comments)



@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def create_pitch():
   
    form = PitchForm()


    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        pitch= form.content.data
        category_id = form.category_id.data
        new_pitch= Pitch(pitch= pitch, category_id= category_id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('create_pitch.html', create_pitch= form, category= category)

@main.route('/category/<int:id>')
def category(id):
    
    category = PitchCategory.query.get(id)

    if category is None:
        abort(404)

    pitches_in_category = Pitches.get_pitch(id)
   
    return render_template('category.html' ,category= category, pitches= pitches_in_category)

@main.route('/pitch/comment/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
  
    if form.validate_on_submit():
        new_comment = Comment(pitch_id =id,comment=form.comment.data,username=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    
    return render_template('comment.html',comment_form=form)




@main.route('/view/comment/<int:id>')
def view_comments(id):
    
    comments = Comment.get_comments(id)
    return render_template('show_comments.html',comments = comments, id=id)





