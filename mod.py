from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm, SearchForm, EditForm
from datetime import date
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog
from datetime import datetime
from routes.view_routes import view_routes
from routes.add_routes import add_routes
from routes.edit_routes import edit_routes
import os

from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

from flask_wtf import FlaskForm
from models import ProductType
from wtforms.validators import DataRequired, Optional, InputRequired
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, SelectMultipleField, DateField, HiddenField 

from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog



from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime, date
from sqlalchemy import text
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog


from flask import Blueprint, render_template, request
from models import Product
from forms import MyForm, SearchForm, EditForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents, ProductLog
