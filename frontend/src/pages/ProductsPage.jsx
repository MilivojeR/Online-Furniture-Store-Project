import React, {useEffect} from 'react'
import axios from 'axios'


// service
import ProductService from '../services/productService'

function ProductsPage() {

  useEffect(() => {
    // ProductService.getAllProducts()
    //   .then((res)=> console.log(res))
    //   .catch((err)=> console.log(err))

    const fetchData = async () => {
      try {
        const response = await axios.get(
          'https://04dc-62-4-41-75.ngrok-free.app/product',  // API endpoint
          {
            headers: {
              'Accept': 'application/json',  // Postavljanje Accept header-a
              "ngrok-skip-browser-warning": "69420"
            }
          }
        );
        console.log(response.data);
      } catch (error) {
        console.log(error.message);
      }
    };

     fetchData();

  }, [])
  


  return (
    <div className='container'>
      <h1>All products</h1>
      <hr/>
      <div className='mt-3 d-flex p-4 flex-wrap justify-content-around'>
        <div className='card me-3 mt-3' style={{width: "350px", height: "450px"}}> 
          <img className='card-img-top' style={{height: "255px"}} src={`https://www.branchfurniture.com/cdn/shop/products/coralherocopy.jpg?v=1652368917`}/>
          <div className='card-body'>
            <h4 className='card-title'>Naziv proizvoda</h4>
            <h5 className='card-subtitle mb-2 text-muted'>Opis proizvoda</h5>
          </div>
          <div className='card-footer'>
            <button className='btn btn-warning btn-sm'>Kontakt za informacije</button>
          </div>
        </div>
      </div>
      
    </div>
  )
}

export default ProductsPage