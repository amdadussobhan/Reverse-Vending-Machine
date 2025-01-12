import React from 'react'

const ProductCard = ({product}) => {
    return (
        <div className="card text-center my-3 float-left" style={{ width: '15rem' }}>
            <img src="..." className="card-img-top" alt="..." />
                <div className="card-body">
                    <h5 className="card-title">{product.name}</h5>
                    <h3 className="card-title">{product.price}</h3>
                    <a href="#" className="btn btn-primary">Add to Cart</a>
                </div>
        </div>
    )
}

export default ProductCard