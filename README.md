# CodingWiz.dev
A lightweight blog app built with Python and Flask. Source Code from my Python and Flask Web Development Course (Lang: Italian)

![](https://i.imgur.com/8ahzSnh.gif)


### How To Install Locally
```
git clone https://github.com/pymike00/codingwiz-dev.git
cd codingwiz-dev
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
flask shell
from blog.models import User
u = User(username="admin", email="email@provider.com")
u.set_password_hash("your-secret-psw")
db.session.add(u)
db.session.commit()
quit()
flask run
```


### Few things you might want to add/change if you intend to actually use the app:
- Error Logging
- Rate Limiting
- Markdown Preview
- Whatever else you want! The theme is based on Bootstrap 4, so it's easily adaptable.