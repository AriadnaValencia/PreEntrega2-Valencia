import React from 'react';

const CardWidget = () => {
    const notificationNumber = 10; // Número hardcodeado
  
    return (
      <div className="card-widget">
        <div className="icon">
          <i className="fas fa-bell"></i> {/* Cambia el ícono según tus necesidades */}
        </div>
        <div className="notification">
          {notificationNumber}
        </div>
      </div>
    );
  }
  
  export default CardWidget;