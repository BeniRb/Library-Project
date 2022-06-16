
import app.tools.books as tb
import app.tools.customers as tc
import app.tools.loans as tl
from flask import Flask,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/books')
def books():
    return render_template('/books/bookshomepage.html')

@app.route("/books/addBook", methods=['GET', 'POST'])
def addBook():
    return tb.Book.addBook(tb.Book)

@app.route("/books/showAllBooks", methods=['GET', 'POST'])
def displayAllBooks():
    return tb.Book.showAllBooks(tb.Book)

@app.route("/books/removeBook",methods=['GET','POST'])
def removeBook():
    return tb.Book.removeBook(tb.Book)

@app.route("/books/findBook",methods=['GET','POST'])
def findbook():
    return tb.Book.findBook(tb.Book)

@app.route('/customers',methods=['GET','POST'])
def customers():
    return render_template('/customers/customershomepage.html')

@app.route("/customers/addCustomer",methods=['GET','POST'])
def addCustomer():
    return tc.Customer.addCustomer(tc.Customer)

@app.route("/customers/removeCustomer",methods=['GET','POST'])
def removeCustomer():
    return tc.Customer.removeCustomer(tc.Customer)

@app.route("/customers/displayAllCustomers",methods=['GET','POST'])
def displayAllCustomers():
    return tc.Customer.displayAllCustomers(tc.Customer)

@app.route("/customers/findCustomer",methods=['GET','POST'])
def findcustomer():
    return tc.Customer.findCustomer(tc.Customer)

@app.route("/loans")
def loans():
    return render_template("/loans/loanhomepage.html")

@app.route("/loans/loanabook", methods=['GET','POST'])
def loanabook():
    return tl.loans.loanabook(tl.loans)

@app.route("/loans/displayallloans",methods=['GET','POST'])
def displayloans():
    return tl.loans.displayallloans(tl.loans)

@app.route("/loans/returnabook",methods=['GET','POST'])
def returnabook():
    return tl.loans.returnabook(tl.loans)

@app.route("/loans/displaylateloans",methods=['GET','POST'])
def displaylateloans():
    return tl.loans.displaylateloans(tl.loans)

@app.route('/contact')
def contact():
    return render_template('contact.html')
