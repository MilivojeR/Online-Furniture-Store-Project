import axios from 'axios'

class ProductService {
    static getAllProducts = () => axios.get('https://538c-95-155-26-221.ngrok-free.app/product/')
}

export default ProductService