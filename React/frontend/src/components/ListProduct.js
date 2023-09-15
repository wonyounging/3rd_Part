import React, { useRef, useEffect, useState } from 'react';
import './main.css';
import ProductItem from './ProductItem';
import { useNavigate, userNavigate } from 'react-router';

function ListProduct() {
  const navigate = useNavigate();
  const [items, setProductList] = useState([]);
  const product_name = useRef();

  function getList(url) {
    fetch(url)
//  서버 호출
      .then(response => { return response.json(); })
//          서버 응답                      json으로 변환
//     응답 출력함수
      .then(data => { setProductList(data); });
  }
  useEffect(() => { getList('http://localhost/list'); }, []);
//          (입력) => {출력}

  return (
    <>
        <h2>상품목록</h2>
        상품명: <input name='product_name' ref={product_name} />
        <button type='button' onClick={() => {
        getList(`http://localhost/list?product_name=${product_name.current.value}`)
        }}>조회</button>
        <br /><br />
        <button onClick={() => navigate('/write')}>상품등록</button>
        <hr />
        등록된 상품수: {items.length}
        <br /><br />
        <div style={{
        display: 'grid',
        gridTemplateRows: '1fr',  // 1행
        gridTemplateColumns: '1fr 1fr 1fr 1fr 1fr',   // 5열
        }}>
        {items.map(   // 반복문
            ({ product_code, product_name, price, filename }) => (
            <ProductItem
                product_code={product_code}
                product_name={product_name}
                price={price}
                filename={filename}
                key={product_code}
            />
            )
        )}
        </div>
    </>
    );
}
export default ListProduct;