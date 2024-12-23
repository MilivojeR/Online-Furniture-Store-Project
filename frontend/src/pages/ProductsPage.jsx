import React, {useEffect, useState} from 'react'
import {toast} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import ProductService from '../services/productService'
import customAxios from '../utils/customAxios';
import CategoryService from '../services/categoryService';

function ProductsPage() {
  const [showModal, setShowModal] = useState(false);
  const [products, setProducts] = useState([]);
  const token = sessionStorage.getItem('access_token');

  const [imageUrls, setImageUrls] = useState([]);
  const [imageUrl, setImageUrl] = useState('');

  const [categories, setCategories] = useState([]);


  useEffect(() => {
    const loadProducts = async () => {
      try {
          const data = await ProductService.fetchData(); 
          setProducts(data); 
      } catch (error) {
          console.error('Greška pri učitavanju proizvoda:', error);
      }
    };

    loadProducts();

    const loadCategories = async () => {
      try {
          const data = await CategoryService.fetchData(); 
          setCategories(data); 
      } catch (error) {
          console.error('Greška pri učitavanju proizvoda:', error);
      }
    };

    loadCategories();
  }, [])

  const openModal = () => {
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
  };

  const deleteProduct = async(id) => {
    await customAxios.delete(`https://b4b7-62-4-41-75.ngrok-free.app/product/${id}`)
               .then(res => {
                  toast.success('Successfully delete');
                  const newProducts = products.filter(p => p.product_id != id);
                  setProducts(newProducts);
                }).catch(error => {
                  toast.error('Delete failed');
                })
  }

  const handleImageUrlChange = (e) => {
    setImageUrl(e.target.value);
  };

  const addImageUrl = () => {
    if (imageUrl && !imageUrls.includes(imageUrl)) {
      setImageUrls([...imageUrls, imageUrl]);
      setImageUrl(''); 
    }
  };

  const removeImageUrl = (url) => {
    setImageUrls(imageUrls.filter((image) => image !== url));
  };

  return (
    <div className='container'>
      <div className='d-flex flex-row mt-2'>
        <h1>All products</h1>
        <button className='btn btn-success btn-sm ms-2' onClick={() => openModal()}>Add new product</button>
      </div>
      <hr/>
      <div className='mt-3 d-flex p-4 flex-wrap justify-content-around'>
        {
          products.map(p => (
          <div className='card me-3 mt-3' style={{width: "350px", height: "550px"}} key={p.product_id}> 
            <img className='card-img-top' style={{height: "255px"}} src={p.product_picture_url.split(', ')[0]}/>
            <div className='card-body'>
              <h4 className='card-title'>{p.product_name}</h4>
              <p className='card-subtitle mb-2 text-muted'>{p.product_description.slice(0, 150)}...</p>
            </div>
            <div className='card-footer'>
              <button className='btn btn-warning btn-sm'>Kontakt za informacije</button>
              {
                token != null && ( <>
                  <button className='btn btn-outline-success btn-sm ms-5'>Edit</button>
                  <button className='btn btn-outline-danger btn-sm ms-2' onClick={() => deleteProduct(p.product_id)}>Delete</button>
                  </>
                )
              }
            </div>
          </div>
          ))
        }
      </div>

      <div className={`modal fade ${showModal ? 'show' : ''}`} tabIndex="-1" style={{ display: showModal ? 'block' : 'none' }} aria-hidden={!showModal}>
                <div className="modal-dialog">
                    <div className="modal-content">

                        <div className="modal-header">
                            <h5 className="modal-title">Add new product</h5>
                            <button type="button" className="btn-close" onClick={closeModal} aria-label="Close"></button>
                        </div>

                        <div className="modal-body">
                            <form>
                              <div>
                                <label className='form-label' htmlFor='product_name'>Name:</label>
                                <input className='form-control' type='text' id='product_name' name='product_name' placeholder='Enter name' required/>
                              </div>
                              <div>
                                <label className='form-label' htmlFor='product_price'>Price:</label>
                                <input className='form-control' type='number' id='product_price' name='product_price' placeholder='Enter price' required/>
                              </div>
                              <div>
                                <label className='form-label' htmlFor='product_video_url'>Video:</label>
                                <input className='form-control' type='text' id='product_video_url' name='product_video_url' placeholder='Enter video url'/>
                              </div>
                              <div>
                              <label htmlFor="imageUrl" className="form-label">
                                Image URL
                              </label>
                              <div className="d-flex">
                                <input
                                  type="text"
                                  className="form-control"
                                  id="imageUrl"
                                  value={imageUrl}
                                  onChange={handleImageUrlChange}
                                  placeholder="Enter image URL"
                                />
                                <button
                                  type="button"
                                  className="btn btn-success ms-2"
                                  onClick={addImageUrl}
                                >
                                  +
                                </button>
                              </div>
                              </div>
                              <div>
                              <label className="form-label">Image URLs</label>
                                <ul className="list-group">
                                  {imageUrls.map((url, index) => (
                                    <li key={index} className="list-group-item d-flex justify-content-between align-items-center">
                                      <img src={url} alt={`Image ${index + 1}`} style={{ width: '50px', height: '50px', objectFit: 'cover' }} />
                                      <button
                                        type="button"
                                        className="btn btn-danger btn-sm"
                                        onClick={() => removeImageUrl(url)}
                                      >
                                        Remove
                                      </button>
                                    </li>
                                  ))}
                                </ul>
                              </div>
                              <div>
                                <label className='form-label' htmlFor='product_description'>Description:</label>
                                <textarea className='form-control' rows='3' id='product_description' name='product_description' placeholder='Enter description' required></textarea>
                              </div>
                              <div>
                              <label className='form-label' htmlFor='product_category_id'>Category:</label>
                              <select className='form-select' id='product_category_id' name='product_category_id'>
                                  
                              </select>
                              </div>
                            </form>
                        </div>

                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" onClick={closeModal}>Close</button>
                            <button type="button" className="btn btn-primary">Create</button>
                        </div>

                    </div>
                </div>
            </div>

            {showModal && <div className="modal-backdrop fade show" onClick={closeModal}></div>}
      
    </div>
  )
}

export default ProductsPage