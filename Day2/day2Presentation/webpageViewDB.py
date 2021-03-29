from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    sql = '''
      SELECT univ_name,AVG(ranking) as Average_Ranking from (SELECT * from autism_universities
      UNION SELECT * from autism_universities2
      UNION SELECT * from autism_universities3
      ORDER by univ_name)
      GROUP by univ_name
      ORDER by Average_Ranking
    '''
    conn = sqlite3.connect("autismUniversitiesDB.db")
    c = conn.cursor()
    c.execute(sql)
    records = c.fetchall()
    datalist = []
    for record in records:
        datalist.append(record)
    return datalist


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
