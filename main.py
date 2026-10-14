from pathlib import Path
from flask import Flask, render_template
import yaml
import shutil
app = Flask(__name__)
config_file = "./config.yml"

@app.route("/")
def home():
    # check if there is config file
    # create a config file if there isn't one
    if Path(config_file).exists() == False:
        shutil.copyfile("./default/config.yml",config_file )
    with open("./config.yml", "r") as ymlfile:
        config = yaml.safe_load(ymlfile)
        title = config["title"]
        introduction = config["introduction"]
        projects = config["projects"]
    return render_template("index.html",
                           projects_list=projects,
                           title=title,
                           introduction=introduction)


if __name__ == "__main__":
    app.run(debug=True)