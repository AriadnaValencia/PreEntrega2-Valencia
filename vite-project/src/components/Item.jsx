import React from 'react';
import { Link } from 'react-router-dom';

const Item = ({ id, name }) => {
  return (
    <div className="item">
      <Link to={`/item/${id}`}>{name}</Link>
    </div>
  );
}

export default Item;
