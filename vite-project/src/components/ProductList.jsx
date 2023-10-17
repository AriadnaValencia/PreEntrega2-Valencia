import React from 'react';
import Product from './Product';

const ProductList = () => {
  const products = [
    {
      id: 1,
      name: 'Lifting',
      price: 5.600,
      imageUrl: 'C:\Users\ari_e\OneDrive\Escritorio\REACT\vite-project\src\assets\image\img-liftings\lifting-antesydespues2.png'
    },
    {
      id: 2,
      name: 'Perfilado',
      price: 3.600,
      imageUrl: 'C:\Users\ari_e\OneDrive\Escritorio\REACT\vite-project\src\assets\image\img-perfilados\perfilado-antesydespues.png'
    },
    {
      id: 3,
      name: 'Esmaltado',
      price: 4.100,
      imageUrl: 'C:\Users\ari_e\OneDrive\Escritorio\REACT\vite-project\src\assets\image\img-uñas\semis-simbolos.png'
    },
  ];

  return (
    <div className="product-list">
      {products.map(product => (
        <Product
          key={product.id}
          name={product.name}
          price={product.price}
          imageUrl={product.imageUrl}
        />
      ))}
    </div>
  );
}

export default ProductList;
