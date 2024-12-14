import React, {useEffect} from 'react'
import axios from 'axios'


// service
import ProductService from '../services/productService'

function ProductsPage() {

  useEffect(() => {
    ProductService.getAllProducts()
      .then((res)=> console.log(res))
      .catch((err)=> console.log(err))

    // const fetchData = async () => {
    //   try {
    //     const response = await axios.get(
    //       'https://538c-95-155-26-221.ngrok-free.app/product/',  // API endpoint
    //       {
    //         headers: {
    //           'Accept': 'application/json'  // Postavljanje Accept header-a
    //         }
    //       }
    //     );
    //     console.log(response.data);
    //   } catch (error) {
    //     console.log(error.message);
    //   }
    // };

    // fetchData();

  }, [])
  


  return (
    <div>ProductsPage</div>
  )
}

export default ProductsPage