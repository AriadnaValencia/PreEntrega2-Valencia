import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { obtenerProductosPorCategoria, obtenerProductoPorId } from './async-mocks';

const ItemListContainer = () => {
  const [productos, setProductos] = useState([]);
  const { categoryId, itemId } = useParams();

  useEffect(() => {
    const cargarProductos = async () => {
      if (categoryId) {
        const productosCategoria = await obtenerProductosPorCategoria(categoryId);
        setProductos(productosCategoria);
      }

      if (itemId) {
        const producto = await obtenerProductoPorId(itemId);
        setProductos([producto]);
      }
    };

    cargarProductos();
  }, [categoryId, itemId]);

  return (
    <div>
      {productos.map(producto => (
        <div key={producto.id}>
          <h3>{producto.nombre}</h3>
          <p>{producto.descripcion}</p>
        </div>
      ))}
    </div>
  );
}

export default ItemListContainer;
