import React from 'react';

const Product = ({ name, price, imageUrl }) => {
  return (
    <div className="product">
      <img src={imageUrl} alt={name} />
      <h3>{name}</h3>
      <p>{price} USD</p>
    </div>
  );
}

export default Product;
