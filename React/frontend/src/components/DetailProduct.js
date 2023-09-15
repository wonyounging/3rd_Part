import React, { useRef, useEffect, useState } from 'react';
import './main.css';
import { useNavigate } from 'react-router-dom';

function useFetch(url) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch(url)
            .then(response => {
                return response.json();
            })
            .then(data => {
                setData(data);
                setLoading(false);
            })
        }, []);
        return [data, loading];
}

function DetailProduct() {
    const paths = window.location.href.split('/');
    const url = 'http://localhost/' + paths[paths.length - 2] + '/' + paths[paths.length - 1];
    const [data, loading] = useFetch(url);
    const navigate = useNavigate();
    const product_name = useRef();
    const price = useRef();
    const description = useRef();
    const img = useRef();

    if (loading) {
        return (
        <div>loading</div>
        )
    } else {
        let src='';
        let image_url = '';
        if (data.filename !== '-') {
            src = `http://localhost/static/images/${data.filename}`;
            image_url = `<img src=${src} width='300px' height='300px' />`;
        } else {
            image_url='';
        }
        return (
            <>
                <table>
                    <tbody>
                        <tr>
                            <td>상품명</td>
                            <td><input ref={product_name} defaultValue={data.product_name} /></td>
                        </tr>
                        <tr>
                            <td>가격</td>
                            <td><input type='number' ref={price} defaultValue={data.price} /></td>
                        </tr>
                        <tr>
                            <td>상품설명</td>
                            <td><textarea rows='5' cols='60' ref={description} defaultValue={data.description} /></td>
                        </tr>
                        <tr>
                            <td>상품이미지</td>
                            <td>
                                <span dangerouslySetInnerHTML={{ __html: image_url }}></span>
                                <br />
                                <input type='file' ref={img} />
                            </td>
                        </tr>
                        <tr>
                            <td colSpan='2' align='center'>
                                <button onClick={() => navigate('/')}>목록</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </>
        );
    }
}

export default DetailProduct;