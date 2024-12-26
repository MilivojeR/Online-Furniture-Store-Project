import React, { useEffect, useState } from 'react'
import {useParams} from 'react-router-dom';
import ProductService from '../services/productService';
import CategoryService from '../services/categoryService';
import Iframe from 'react-iframe'

function SingleProductPage() {
  const {id} = useParams();
  const [product, setProduct] = useState();
  const [imageUrls, setImageUrls] = useState([]);
  const [activeIndex, setActiveIndex] = useState(0);
  const [category, setCategory] = useState();

  const next = () => {
    setActiveIndex((prevIndex) => (prevIndex + 1) % imageUrls.length);
  };

  const prev = () => {
    setActiveIndex((prevIndex) => (prevIndex - 1 + imageUrls.length) % imageUrls.length);
  };

  useEffect(() => {
    const loadProductById = async () => {
      try {
          const data = await ProductService.fetchDataById(id);
          console.log(data);
          setImageUrls(data.product_picture_url.split(', '));
          setProduct(data); 
      } catch (error) {
          console.error('Greška pri učitavanju proizvoda:', error);
      }
    };
    loadProductById();   
  }, []);

  useEffect(() => {
    const loadCategories = async () => {
      try {
          const data = await CategoryService.fetchData();
          setCategory(data.find(c => c.category_id == product.product_category_id));
      } catch (error) {
          console.error('Greška pri učitavanju proizvoda:', error);
      }
    };

    loadCategories();
  }, [product]);
  
  return (
    <div className='container mt-5 d-flex flex-column mb-5'>
      <div className='row'>
        <div className='col-md-6'>
          <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
                <div class="carousel-inner">
                  {
                    imageUrls.map((p, index) => (
                      <div className={`carousel-item ${index === activeIndex ? 'active' : ''}`} key={index} >
                        <img src={p} className="d-block carousel-image" alt="Slika nije učitana" style={{height: '650px', width: '650px'}}/>
                      </div>
                    ))
                  }
                </div>
                <button className="carousel-control-prev" type="button" onClick={prev}>
                  <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" onClick={next}>
                  <span className="carousel-control-next-icon" aria-hidden="true"></span>
                  <span className="visually-hidden">Next</span>
                </button>
            </div>
        </div>
        <div className='col-md-6 text-center'>
          <h1 className='text-center'>{product?.product_name}</h1>
          <hr/>
          <h3>Price: {product?.product_price} EUR</h3>
          <h3>Category: {category?.category_name}</h3>
          <h3>Description: {product?.product_description}</h3>
          <hr/>
          <Iframe url={product?.product_video_url}
        width="640px"
        height="320px"
        id=""
        className=""
        display="block"
        position="relative"/>
        </div>
      </div>
    </div>
  )
}

export default SingleProductPage