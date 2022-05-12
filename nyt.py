from flask import Flask,render_template,request

import login
import requests
api_key=login.nyt_api

list_url='https://api.nytimes.com/svc/books/v3/lists/names.json?api-key='+api_key

r=requests.get(list_url)
try:
    r=r.json()
    results=r.get('results',[])
    list_data=[]
    for result in results:
        list_data.append({'list_name':result['display_name'],'encoded_name':result['list_name_encoded']})
except Exception:
    list_data=[{'list_name':'No List','encoded_name':'no_list'}]

# print(list_data)

# ================================================================
def get_encoded_list_name(input_list,selected_list):
    # encoded_name_of_list=''
    for item in input_list:
        if item['list_name']==selected_list:
            encoded_name_of_list=item['encoded_name']
            break
        
    return encoded_name_of_list

# ================================================================

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    return render_template('index.html',lists=list_data)

@app.route('/books',methods=['GET','POST'])
def books():
    print(request.form.get('date-input'))
    selected_list=get_encoded_list_name(list_data,request.form.get('lists'))
    if not request.form.get('date-input'):
        url='https://api.nytimes.com/svc/books/v3/lists/current/'+selected_list+'.json?api-key='+api_key
    else:
        picked_date=request.form.get('date-input').split('/')
        picked_date=f'{picked_date[2]}-{picked_date[0]}-{picked_date[1]}'
        url='https://api.nytimes.com/svc/books/v3/lists/'+picked_date+'/'+selected_list+'.json?api-key='+api_key
    r=requests.get(url)
    try:
        r=r.json()
        results=r.get('results',[]).get('books',[])
        image_data=[]
        for result in results:
            image_data.append({'title':result['title'],'author':result['author'],'image':result['book_image'],'amazon':result['amazon_product_url'],'description':result['description']}) 

    except Exception as e:
        print(e)
        image_data=[{'title':'no title','author':'no author','image':'https://salautomotive.in/wp-content/uploads/2017/01/no-image-available.jpg','amazon':'https://amazon.com','description':'no description'}]
        
    return render_template('books.html',images=image_data,list_name=request.form.get('lists'))
if __name__=="__main__":
    app.run(debug=True,port=8080)