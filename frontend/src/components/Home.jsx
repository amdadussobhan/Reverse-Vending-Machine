import React, { useEffect, useState } from 'react'
import Axios from 'axios'

const Home = () => {
  const [products, setProducts] = useState(null)
  useEffect(() => {
    const getProducts = async () => {
      await Axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/products/',
      }).then(res => {
        setProducts(res.data);
      })
    }
    getProducts()
  }, [])

  return (
    products && products.length > 0 ? (
      <div className='container'>
        {
          products.map(product => (
            <div key={product.id}>
              <h1>{product.name}</h1>
              <p>{product.description}</p>
              <p>{product.price}</p>
            </div>
          ))
        }
      </div>
    ) : (<p>No Product</p>)
  )
}

export default Home