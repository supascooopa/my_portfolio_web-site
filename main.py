from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    with open("my_repos.txt") as file:
        repo_lines = file.readlines()
    with open("project_titles_and_descriptions") as file:
        lines = file.readlines()
        clean_lines = [line.strip("\n") for line in lines]
        new_lines = []
        title_and_description = []
        for line in clean_lines:
            title_and_description.append(line)
            if len(title_and_description) == 2:
                new_lines.append(title_and_description)
                title_and_description = []
    project_dict = {repo_link: about for repo_link, about in zip(repo_lines, new_lines)}

    return render_template("index.html", repo_list=project_dict)


if __name__ == "__main__":
    app.run(debug=True)