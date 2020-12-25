from flask import Flask, render_template,redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from video import Video

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class DownloadForm(FlaskForm):

    link = StringField('Link to the video: ')
    submit = SubmitField('Download')


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = DownloadForm()
    link = form.link.data
    if form.validate_on_submit():
        video = Video(link)
        if video.vadlidate_link() == True:
            video.download()
            flash('Video downloaded successfully:👍')
        else:
            flash('Error occurred while downloading video. Maybe link is invalid🤔')

        return redirect(url_for('index'))

    return render_template('index.html', form = form)



if __name__ == '__main__':
    app.run()
