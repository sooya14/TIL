import React, { useState, useEffect, useRef } from "react";

const App = () => {
  const potato = useRef();
  setTimeout(()=> potato.current.focus() , 5000)
  return (
    <div className="App">
      <div>
        <input ref={potato} placeholder="hi" />
      </div>
    </div>
  );
};
