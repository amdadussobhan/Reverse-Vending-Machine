import React, { useEffect, useState } from 'react'
import Axios from 'axios'
import ProductCard from './ProductCard'

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
            <ProductCard key={product.id} product={product} />
          ))
        }
      </div>
    ) : (<p>No Product</p>)
  )
}

export default Home