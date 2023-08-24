# How to run this project

- Make sure that docker is installed on your system
- Navigate to the `infra` directory
- Run command `docker-compose up --build`, on Linux `sudo` may be required
- After some time project is available at http://127.0.0.1/
- Check it by navigating to http://127.0.0.1/api/news, for example

# Developer support

- Docs is available at http://127.0.0.1/api/docs
- Lots of useful stuff lays in Makefile, check it with `make help` in same folder with Makefile
- You can turn on/off email system in settings.py file, check EMAIL_CONFIRMATION constant

# Open bash terminal

You might need it to create superuser for example

Run: `docker exec -it back bash`, linux may need `sudo` prefix
