import openai
from flask import Flask,render_template,request
import flask
import re

openai.api_key = "YOUR__OPEN_AI__KEY"

app = Flask(__name__)

@app.route('/')
def hello_world():
 return '<h2>GPT-3 Powered API<h2>'

@app.route('/write_product_description/<product_name>',methods=['POST', 'GET'])
def write_product_description(product_name):
   
    prompt = f"Write a product description for a {product_name} in attrative tone. The description should focus solely on these features and not include any additional information or unnecessary words. Key features and benefits and other specifications should be returned in a bullet list"
    response = openai.Completion.create( model="text-davinci-002",
    prompt=prompt,
    temperature=0.8,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    model = response['choices'][0]['text']
    model=re.sub("\\n","",model)
    name = model
    
 
    return flask.jsonify({f'{product_name}': name})

@app.route('/write_ad_creation/<ad_name>',methods=['POST', 'GET'])
def write_ad_creation(ad_name):
   
    prompt = f"Write an ad for a {ad_name} product aimed at attracting buyers."
    response = openai.Completion.create( model="text-davinci-002",
    prompt=prompt,
    temperature=0.8,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    model = response['choices'][0]['text']
    model=re.sub("\\n","",model)
    name = model
    
 
    return flask.jsonify({f'{ad_name}': name})


@app.route('/write_blog_post/<post_name>',methods=['POST', 'GET'])
def write_blog_post(post_name):
   
    prompt = f"Write a blog post on the topic of {post_name}."
    response = openai.Completion.create( model="text-davinci-002",
    prompt=prompt,
    temperature=0.8,
    max_tokens=400,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    model = response['choices'][0]['text']
    model=re.sub("\\n","",model)
    name = model
    
 
    return flask.jsonify({f'{post_name}': name})

if __name__ == '__main__':
    app.run()

