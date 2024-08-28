from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired

class CPIPredictionForm(FlaskForm):
    gender = RadioField('Gender ', 
                        choices=[('Male', 'Male'),
                                 ('Female', 'Female')
                                ],
                        validators=[DataRequired()])

    category = RadioField('Category ', 
                          choices=[('General', 'General'),
                                   ('OBC', 'OBC'),
                                   ('St/Sc', 'St/Sc'),
                                   ('other (PWD)', 'Other (PWD)')],
                          validators=[DataRequired()])

    parental_education = RadioField('Parental Education', 
                                     choices=[('Primary (1-8)', 'Primary (1-8)'),
                                              ('Secondary (9-12)', 'Secondary (9-12)'),
                                              ('Tertiary (graduation or above)', 'Tertiary (graduation or above)')],
                                     validators=[DataRequired()])

    hometown_area = RadioField('Please specify the type of area where your hometown is', 
                               choices=[('Rural', 'Rural'),
                                        ('Semi-Urban', 'Semi-Urban'),
                                        ('Urban', 'Urban')],
                                       
                               validators=[DataRequired()])

    family_annual_income = RadioField('Family annual income', 
                                      choices=[('Below 1 lakh', 'Below 1 lakh'),
                                               ('1 - 2.5 lakh', '1 - 2.5 lakh'),
                                               ('2.5 - 5 lakh', '2.5 - 5 lakh'),
                                               ('5 - 10 lakh', '5 - 10 lakh'),
                                               ('above 10 lakh', 'Above 10 lakh')],
                                      validators=[DataRequired()])

    guidance_from_family = RadioField('Do you have proper guidance or mentorship in studies from your family member (parents, siblings, cousins)', 
                                      choices=[('yes', 'Yes'),
                                               ('no', 'No')],
                                      validators=[DataRequired()])

    family_member_in_same_field = RadioField('Is there any of your sibling or cousin into higher study same as you?', 
                                             choices=[('Yes', 'Yes'),
                                                      ('No', 'No')],
                                             validators=[DataRequired()])

    percentage_10th = RadioField('Percentage in 10th', 
                                  choices=[('Below 60%', 'Below 60%'),
                                           ('60-70%', '60-70%'),
                                           ('70-80%', '70-80%'),
                                           ('80-90%', '80-90%'),
                                           ('Above 90%', 'Above 90%')],
                                  validators=[DataRequired()])

    percentage_12th = RadioField('Percentage in 12th', 
                                  choices=[('Below 60%', 'Below 60%'),
                                           ('60-70%', '60-70%'),
                                           ('70-80%', '70-80%'),
                                           ('80-90%', '80-90%'),
                                           ('Above 90%', 'Above 90%')],
                                  validators=[DataRequired()])

    medium_studied_in = RadioField('Which medium did you study in?', 
                                   choices=[('English', 'English'),
                                            ('Hindi', 'Hindi'),
                                            ('Regional languages (like Bangla, Oriya etc)', 'Regional languages (like Bangla, Oriya etc)')],
                                   validators=[DataRequired()])

    cpi_graduation = StringField('CPI in graduation (if completed) or like if you had 70% type 7.0', validators=[DataRequired()])

    course = RadioField('Which course are you pursuing?', 
                        choices=[('M.sc.', 'M.sc.'),
                                 ('B.sc', 'B.sc'),
                                 ('Bvoc software development', 'Bvoc software development'),
                                 ('MCA', 'MCA'),
                                 ('B.tech', 'B.tech'),
                                 ('M.tech', 'M.tech'),
                                 ('Law', 'Law'),
                                 ('MA', 'MA'),
                                 ('B.Ed', 'B.Ed'),
                                 ('P.hD.', 'P.hD.'),
                                 ('BA', 'BA'),
                                 ('MBA', 'MBA'),
                                 ('BCA', 'BCA'),
                                  ('Bcom', 'Bcom'),
                                 ('D.el.ed', 'D.el.ed'),
                                 ('B.Lib.I.Sc.', 'B.Lib.I.Sc.'),
                                 ('Ett', 'Ett'),
                                 ('Cosmetology ', 'Cosmetology'),
                                 ('Pcs ', 'Pcs'),
                                 ('Other', 'Other')],
                        validators=[DataRequired()])

    college_type = RadioField('College type', 
                              choices=[('IIT', 'IIT'),
                                       ('NIT', 'NIT'),
                                       ('Reputed University (like BHU, DU etc)', 'Reputed University (like BHU, DU etc)'),
                                       ('Regional and private colleges', 'Regional and private colleges')],
                              validators=[DataRequired()])

    attendance_in_class = RadioField('Attendance in class (in percentage)', 
                                      choices=[('90%', '90%'),
                                               ('80%', '80%'),
                                               ('70%', '70%'),
                                               ("didn't attended classes properly", "Didn't attend classes properly")],
                                      validators=[DataRequired()])

    living_arrangement = RadioField('Living arrangement', 
                                    choices=[('Hostel room', 'Hostel room'),
                                             ('PG room', 'PG room'),
                                             ('Home', 'Home'),
                                             ('Other', 'Other')],
                                    validators=[DataRequired()])

    participation_in_class = RadioField('Participation in class (raising hand, asking doubts and all)', 
                                        choices=[('frequently (almost daily )', 'Frequently (almost daily)'),
                                                 ('once in a while', 'Once in a while'),
                                                 ('never', 'Never')],
                                        validators=[DataRequired()])

    homework_submission = RadioField('Homework submission (completed when?)', 
                                     choices=[('2 or more days before due date', '2 or more days before due date'),
                                              ('on the due date (night before)', 'On the due date (night before)'),
                                              ('missed some homeworks didn\'t complete', 'Missed some homeworks didn\'t complete')],
                                     validators=[DataRequired()])

    preparation_level_for_exam = RadioField('Usually preparation level for exam', 
                                            choices=[('100% (class notes + assignments + book\'s que)', '100% (class notes + assignments + book\'s que)'),
                                                     ('80% (Class notes + assignments)', '80% (Class notes + assignments)'),
                                                     ('50% (assignments or class notes only)', '50% (assignments or class notes only)'),
                                                     ('10% (nothing much)', '10% (nothing much)')],
                                            validators=[DataRequired()])


    internet_usage = RadioField('Internet Usage (used for study purpose on daily basis)', 
                                choices=[('0 hours', '0 hours'),
                                         ('1-2 hours', '1-2 hours'),
                                         ('2-4 hours', '2-4 hours'),
                                         ('5+', '5+')],
                                validators=[DataRequired()])

    weekend_plans = RadioField('Weekend plans usually', 
                               choices=[('Netflix and Chill', 'Netflix and Chill'),
                                        ('Going out side with friends', 'Going outside with friends'),
                                        ('almost sleeping all day', 'Almost sleeping all day'),
                                        ('revising the week\'s study material', 'Revising the week\'s study material')],
                               validators=[DataRequired()])
    
    study_technique =RadioField('Study technique',
                                choices=[('summarizing and making short notes','summarizing and making short notes'),
                                            ('revising the whole notes without short notes','revising the whole notes without short notes'),
                                            ('practice by writting','practice by writting')])

    study_environment = RadioField('Study environment (preferred one or where mostly you study)', 
                                   choices=[('library (self)', 'Library (self)'),
                                            ('home (self)', 'Home (self)'),
                                            ('library (group study)', 'Library (group study)'),
                                            ('home (group study)', 'Home (group study)')],
                                   validators=[DataRequired()])

    learning_style = RadioField('Learning style (preferred way to learn)', 
                                choices=[('from Professor in the class', 'From Professor in the class'),
                                         ('from friends after the class', 'From friends after the class'),
                                         ('from youTube or some online platforms', 'From YouTube or some online platforms'),
                                         ('reading from books', 'Reading from books')],
                                validators=[DataRequired()])

    
    sleeping_time = RadioField('sleeping patterns (what time usually you sleep)', 
                                 choices=[('12 am or before', '12 am or before'),
                                          ('1 am', '1 am'),
                                          ('2 am', '2 am'),
                                          ('3 am or later', '3 am or later')],
                                 validators=[DataRequired()])

    extracurricular_activities = RadioField('Extracurricular Activities (participation in sports or clubs or fests)', 
                                            choices=[('yes', 'Yes'),
                                                     ('no', 'No')],
                                            validators=[DataRequired()])
    class_buddy_friend =RadioField('Your class and bench buddy friend',
                                   choices=[('better than you in study','better than you in study'),
                                            ('almost same as you in study','almost same as you in study'),
                                            ('worse than you in study','worse than you in study')])

    relationship_status_in_last_sem = RadioField('Relationship Status (in last semester)', 
                                      choices=[('Healthy Relationship', 'Healthy Relationship'),
                                               ('Toxic Relationship', 'Toxic Relationship'),
                                               ('Single', 'Single')],
                                      validators=[DataRequired()])

    submit = SubmitField('Submit')
