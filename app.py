from flask import Flask, render_template
from utils import get_candidate, get_candidates_by_skill, get_candidates_by_name, load_candidates_from_json

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('list.html', candidates=load_candidates_from_json())


@app.route('/candidate/<x>')
def candidate_page(x):
    candidate = get_candidate(int(x))
    name = candidate['name']
    position = candidate['position']
    picture = candidate['picture']
    skills = candidate['skills']
    return render_template('card.html', name=name, position=position, picture=picture, skills=skills)


@app.route('/search/<candidate_name>')
def candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', len=len(candidates), candidates=candidates)


@app.route('/skill/<skill_name>')
def skill_page(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', len=len(candidates), candidates=candidates, skill_name=skill_name)


app.run()
