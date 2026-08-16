'use client';


import axios from 'axios';
import { useState , useEffect } from 'react';

export default function Card(){
    
    const [data,setData] = useState([])

    useEffect(() => {

        const fetchData = async ()=> {
            const fetchedData = await axios.get('http://127.0.0.1:8000/user/api/v1') ;
            setData(fetchedData.data)
        }
        fetchData()

    },[])


    console.log(data)

    return <>
    
        {data.map( (res) => <h1 key={res.id || res.email}> {res.id} : {res.email}</h1> )}

    
        </>
}