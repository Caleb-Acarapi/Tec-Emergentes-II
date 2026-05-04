from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ─── MODELO ───────────────────────────────────────────────
class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price=${self.price}, stock={self.stock})"


# ─── 1. INIT: Crear tablas ────────────────────────────────
def init_db():
    with app.app_context():
        db.create_all()
        print(" Tablas creadas exitosamente")


# ─── 2. CREATE: Insertar productos ───────────────────────
def insert_products():
    with app.app_context():
        p1 = Product(name="Laptop", price=1500.0, stock=10)
        p2 = Product(name="Mouse", price=25.5, stock=50)
        p3 = Product(name="Teclado", price=45.0, stock=30)
        p4 = Product(name="Monitor", price=320.0, stock=8)

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()
        print(" Productos insertados correctamente")


# ─── 3. READ: Consultar productos ────────────────────────
def query_products():
    with app.app_context():
        print("\n Lista de productos:")
        todos = Product.query.all()
        for p in todos:
            print(f"  {p}")

        print("\n Productos con stock mayor a 10:")
        filtrados = Product.query.filter(Product.stock > 10).all()
        for p in filtrados:
            print(f"  {p}")

        print("\nBuscar producto con id=1:")
        uno = Product.query.filter_by(id=1).first()
        if uno:
            print(f"  {uno}")


# ─── 4. UPDATE: Actualizar un producto ───────────────────
def update_product():
    with app.app_context():
        product = Product.query.filter_by(id=1).first()
        if product:
            product.name = "Laptop Pro"
            product.price = 1800.0
            product.stock = 5
            db.session.commit()
            print(f"\n Producto actualizado: {product}")
        else:
            print("\n Producto no encontrado")


# ─── 5. DELETE: Eliminar un producto ─────────────────────
def delete_product():
    with app.app_context():
        product = Product.query.filter_by(id=4).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            print("\n Producto eliminado correctamente")
        else:
            print("\nProducto no encontrado")


# ─── FLUJO COMPLETO ───────────────────────────────────────
if __name__ == "__main__":
    init_db()
    insert_products()
    query_products()
    update_product()
    delete_product()
    print("\n Lista final de productos:")
    query_products()
