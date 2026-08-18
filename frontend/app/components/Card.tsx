'use client';

import { useData } from "./useHook";

export default function Card(){
    
    const {all , data,loding , fetchdata,setAll} = useData()
    

    console.log(data)

    return <>
    
    {data.length > 1 ? data.map( (res) => <h1 key={res.id || res.email}> {res.id} : {res.email}</h1> ) : <h1>{data.email}</h1>}
    {loding || <h1>Loding...</h1>}
    <button className='bg-blue-500 text-white p-2 rounded max-w-lg' onClick={() => {fetchdata() ;setAll(!all) }}>{all ? 'all' : 'single one'}</button>

    
        </>
}