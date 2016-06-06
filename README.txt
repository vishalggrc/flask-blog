1. Drop all the tables:
    python manage.py shell
    from flask_blog import db
    db.drop_all()
2. python manage.py db init
    Creating directory /home/ubuntu/workspace/flask_blog/migrations ... done
    Creating directory /home/ubuntu/workspace/flask_blog/migrations/versions ... done
    Generating /home/ubuntu/workspace/flask_blog/migrations/env.py ... done
    Generating /home/ubuntu/workspace/flask_blog/migrations/alembic.ini ... done
    Generating /home/ubuntu/workspace/flask_blog/migrations/script.py.mako ... done
    Generating /home/ubuntu/workspace/flask_blog/migrations/README ... done
    Please edit configuration/connection/logging settings in '/home/ubuntu/workspace/flask_blog/migrations/alembic.ini' before proceeding.
3. To generate migration file
    python manage.py db migrate
    INFO  [alembic.runtime.migration] Context impl MySQLImpl.
    INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
    INFO  [alembic.autogenerate.compare] Detected added table 'author'
    INFO  [alembic.autogenerate.compare] Detected added table 'blog'
    Generating /home/ubuntu/workspace/flask_blog/migrations/versions/e9391af00738_.py ... done
4. To update db: python manage.py db upgrade
5. Options: python manage.py db migration
usage: Perform database migrations
manage.py db: error: invalid choice: 'migration' 
(choose from 'show', 'init', 'merge', 'edit', 'current', 'history', 'upgrade', 'branches', 'revision', 'stamp', 'heads', 'migrate', 'downgrade')