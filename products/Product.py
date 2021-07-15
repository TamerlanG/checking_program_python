# I thought of using the prototype pattern + factory pattern,
# to simply create a different products with different configurations
# but I figured that it would be to limiting, so instead I simply went with inheritance

class Product:
    name = ""
    code = ""
    price = 0