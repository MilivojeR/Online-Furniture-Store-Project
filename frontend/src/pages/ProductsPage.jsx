import React, {useEffect, useState} from 'react'
import {toast} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import ProductService from '../services/productService'
import customAxios from '../utils/customAxios';
import CategoryService from '../services/categoryService';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function ProductsPage() {
  const [showModal, setShowModal] = useState(false);
  const [products, setProducts] = useState([]);

  const navigate = useNavigate();

  const token = sessionStorage.getItem('access_token');

  const [imageUrls, setImageUrls] = useState([]);
  const [imageUrl, setImageUrl] = useState('');

  const [categories, setCategories] = useState([]);

  const [flag, setFlag] = useState(null);

  const [productId, setProductId] = useState(null);

  const [formData, setFormData] = useState({
    product_name: '',
    product_price: null,
    product_video_url: '',
    product_picture_url: '',
    product_description: '',
    product_category_id: null
  });

  const loadProducts = async () => {
    try {
        const data = await ProductService.fetchData(); 
        setProducts(data); 
    } catch (error) {
        console.error('Greška pri učitavanju proizvoda:', error);
    }
  };


  useEffect(() => {

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

  const openModal = (flag) => {
    setFlag(flag);
    setShowModal(true);
  };

  const openEditDialog = (p, flag) => {
    setProductId(p.product_id);
    setImageUrls(p.product_picture_url.split(', '));
    setFlag(flag);
    setFormData(p);
    setShowModal(true);
  };

  const closeModal = () => {
    clearForm();
    setShowModal(false);
  };

  const clearForm = () => {
    setFormData({
      product_name: '',
      product_price: 0,
      product_video_url: '',
      product_picture_url: '',
      product_description: '',
      product_category_id: null
    });
    setImageUrls([]);
  }

  const deleteProduct = async(id) => {
    await customAxios.delete(`${import.meta.env.VITE_NGROK_URL}product/${id}`)
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

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async () => {
    const picture_url = imageUrls.join(', ');
    const product = {
      ...formData,
      product_price: parseFloat(formData.product_price),
      product_category_id: Number(formData.product_category_id),
      product_picture_url: picture_url
    }
    console.log(product);
    await axios.post(`${import.meta.env.VITE_NGROK_URL}product`, product, 
                  {
                    headers: {
                      'Authorization': `Bearer ${token}`,
                      'Content-Type': 'application/json'
                    }
                  }
                )
               .then(res => {
                  toast.success('Successfully add');
                  setProducts([...products, res.data]);
                  clearForm();
                  setShowModal(false);
                }).catch(error => {
                  toast.error('Add failed');
                })
  }

  const handleEdit = async () => {
    if (productId == null) {
      toast.error('Edit failed');
      return;
    }
    console.log(productId);
    const picture_url = imageUrls.join(', ');
    const product = {
      ...formData,
      product_price: parseFloat(formData.product_price),
      product_category_id: Number(formData.product_category_id),
      product_picture_url: picture_url
    }
    console.log(product);
    await axios.put(`${import.meta.env.VITE_NGROK_URL}product/${productId}`, product, 
                  {
                    headers: {
                      'Authorization': `Bearer ${token}`,
                      'Content-Type': 'application/json'
                    }
                  }
                )
               .then(res => {
                  toast.success('Successfully edit');
                  clearForm();
                  loadProducts();
                  setShowModal(false);
                }).catch(error => {
                  console.log(error);
                  toast.error('Edit failed');
                })
  }

  const detailsPage = (id) => {
    navigate(`/singleProduct/${id}`);
  }

  return (
    <div className='container'>
      <div className='d-flex flex-row mt-2'>
        <h1>All products</h1>
        {
          token != null && <button className='btn btn-success btn-sm ms-2' onClick={() => openModal(1)}>Add new product</button>
        }
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
              <button className='btn btn-warning btn-sm' onClick={() => detailsPage(p.product_id)}>Details</button>
              {
                token != null && ( <>
                  <button className='btn btn-outline-success btn-sm ms-5' onClick={() => openEditDialog(p, 2)}>Edit</button>
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
                            <h5 className="modal-title">Save product</h5>
                            <button type="button" className="btn-close" onClick={closeModal} aria-label="Close"></button>
                        </div>
                        <div className="modal-body">
                        <form>
                              <div>
                                <label className='form-label' htmlFor='product_name'>Name:</label>
                                <input className='form-control' type='text' id='product_name' name='product_name' value={formData.product_name} onChange={handleChange} placeholder='Enter name' required/>
                              </div>
                              <div>
                                <label className='form-label' htmlFor='product_price'>Price:</label>
                                <input className='form-control' type='number' id='product_price' name='product_price' value={formData.product_price} onChange={handleChange} placeholder='Enter price' required/>
                              </div>
                              <div>
                                <label className='form-label' htmlFor='product_video_url'>Video:</label>
                                <input className='form-control' type='text' id='product_video_url' name='product_video_url' value={formData.product_video_url} onChange={handleChange} placeholder='Enter video url'/>
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
                                <textarea className='form-control' rows='3' id='product_description' name='product_description' value={formData.product_description} onChange={handleChange} placeholder='Enter description' required></textarea>
                              </div>
                              <div>
                              <label className='form-label' htmlFor='product_category_id'>Category:</label>
                              <select className='form-select' id='product_category_id' name='product_category_id' value={formData.product_category_id} onChange={handleChange}>
                                <option value="" selected disabled>Choose category</option>
                                  {
                                    categories.map((option, index) => (
                                      <option key={index} value={option.category_id}>{option.category_name}</option>
                                    ))
                                  }
                              </select>
                              </div>
                              </form>
                        </div>

                        <div className="modal-footer">
                            <button type="button" className="btn btn-secondary" onClick={closeModal}>Close</button>
                            {
                              flag == 1 && <button type="button" className="btn btn-primary" onClick={handleSubmit}>Create</button>
                            }
                             {
                              flag == 2 && <button type="button" className="btn btn-primary" onClick={handleEdit}>Save</button>
                            }
                        </div>

                    </div>
                </div>
            </div>

            {showModal && <div className="modal-backdrop fade show" onClick={closeModal}></div>}
      
    </div>
  )
}

export default ProductsPage