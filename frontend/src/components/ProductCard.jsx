import React from 'react'

const ProductCard = ({ product }) => {
    return (
        <div className='d-inline-flex m-3 shadow-sm rounded'>
            <div className="card text-center border-light" style={{ width:'14rem' }}>
                <img src={ product.image } className="card-img-top mx-auto mt-3" alt="product" style={{ width:'12rem', height:'12rem', objectFit:'cover'}} />
                <div className="card-body">
                    <h5 className="card-title">{product.name}</h5>
                    <h4 className="card-title">{product.price}</h4>
                    <a href="/" className="btn btn-outline-secondary w-100">Add to Cart</a>
                </div>
            </div>
        </div >
    )
}

export default ProductCard