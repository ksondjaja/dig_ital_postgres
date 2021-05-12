"""empty message

Revision ID: e94d563a2497
Revises: 
Create Date: 2021-01-06 05:03:20.466700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e94d563a2497'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(length=64), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('mcq_quizzes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('is_approved', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('videoscramble',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('timeframes', sa.String(length=400), nullable=True),
    sa.Column('is_approved', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mcq_answersets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.Column('seconds_taken', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['mcq_quizzes.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mcq_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=400), nullable=True),
    sa.Column('quiz_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['mcq_quizzes.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mcq_options',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=400), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('is_correct', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['mcq_questions.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mcq_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answerset_id', sa.Integer(), nullable=True),
    sa.Column('option_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['answerset_id'], ['mcq_answersets.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['option_id'], ['mcq_options.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mcq_answers')
    op.drop_table('mcq_options')
    op.drop_table('mcq_questions')
    op.drop_table('mcq_answersets')
    op.drop_table('videoscramble')
    op.drop_table('mcq_quizzes')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###