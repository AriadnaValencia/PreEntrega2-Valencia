import React from 'react';

const ItemListContainer = ({ greeting }) => {
  return (
    <div className="container">
      <div className="row">
        <div className="col-md-12">
          <div className="my-5">
            <h2>{greeting}</h2>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ItemListContainer;
