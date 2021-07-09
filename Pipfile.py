
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
bottle = "*"
google-cloud-storage = "*"
pyjwt = "*"
peewee = "*"
dropbox = "*"

[dev-packages]

[requires]
python_version = "3.9"

[scripts]
start = "python main.py"
