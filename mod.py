from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Product(db.Model):
    """
    Represents a product in the system.

    Attributes:
    - product_id: Unique identifier for the product, generated using UUID.
    - product_name: Name of the product.
    - product_description: Description of the product.
    - upcoming_change: Indicates if there is an upcoming change for the product.
    - deprecated: Indicates if the product is deprecated.
    - product_status: Status of the product.
    - last_updated: Date when the product was last updated.
    - created: Date when the product was created.
    - product_status_detail: Additional details about the product status.
    """

    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))

    # Relationships
    components = db.relationship('ProductComponents', back_populates='child_product', foreign_keys='[ProductComponents.component_id]')
    composed_of = db.relationship('ProductComponents', back_populates='parent_product', foreign_keys='[ProductComponents.product_id]')

class ProductPortfolios(db.Model):
    """
    Represents different portfolios for products.

    Attributes:
    - category_id: Unique identifier for the product portfolio.
    - category_name: Name of the product portfolio.
    """

    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "category_id"
    __term__ = "category_name"

    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_portfolio_map = db.relationship('ProductPortfolioMap', backref='product_portfolio', lazy='dynamic')

class ProductPortfolioMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductPortfolios.

    Attributes:
    - product_id: Foreign key to Product.
    - category_id: Foreign key to ProductPortfolios.
    """

    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "category_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)



# Fetch the associated product portfolios
    product_portfolios = ProductPortfolioMap.query.filter_by(product_id=product_id).all()

    # Extract category_ids from the portfolio mappings
    category_ids = [portfolio.category_id for portfolio in product_portfolios]

    # Fetch the actual portfolios based on the category_ids
    portfolios = ProductPortfolios.query.filter(ProductPortfolios.category_id.in_(category_ids)).all()
