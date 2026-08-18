'use client';


import axios from 'axios';
import { useState , useEffect } from 'react';

export default function Card(){
    
    const [data,setData] = useState([])
    const [all , setAll] = useState(false)

    const fetchdata = () => {

        const fetchAllData = async ()=> {
            const fetchedData = await axios.get('http://127.0.0.1:8000/user/api/v1') ;
            setData(fetchedData.data)
        }
        const fetchSingleData = async ()=> {
            const fetchedData = await axios.get('http://127.0.0.1:8000/user/api/v1/1') ;
            setData(fetchedData.data)
        }
        if (all){
            fetchAllData()
            return
        }
        fetchSingleData()}
    

    

    console.log(data)

    return <>
    
    {data.length > 1 ? data.map( (res) => <h1 key={res.id || res.email}> {res.id} : {res.email}</h1> ) : <h1>{data.email}</h1>}
    <button className='bg-blue-500 text-white p-2 rounded max-w-lg' onClick={() => {fetchdata() ;setAll(!all) }}>{all ? 'all' : 'single one'}</button>

    
        </>
}