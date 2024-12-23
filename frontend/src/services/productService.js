import axios from 'axios'

class ProductService {
    static getAllProducts = () => axios.get('https://bc98-95-155-32-29.ngrok-free.app/products/')
}

export default ProductService