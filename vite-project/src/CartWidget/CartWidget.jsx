import React from 'react';

const CartWidget = () => {
    const notificationNumber = 10; // Número hardcodeado
  
    return (
      <div className="cart-widget">
        <div className="icon">
          <i className="as fa-shopping-cart"></i> {/* Me falta agregar un ícono */}
        </div>
        <div className="notification">
          {notificationNumber}
        </div>
      </div>
    );
  }
  
  export default CartWidget;