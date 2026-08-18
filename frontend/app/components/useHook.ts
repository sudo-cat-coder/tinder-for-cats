import { useState } from "react"
import axios from "axios"

export function useData(){

    const [data,setData] = useState([])
    const [all , setAll] = useState(false)
    const [loding,setLoding] = useState(false)

    const fetchdata = () => {

        const fetchAllData = async ()=> {
            setLoding(false)
            const fetchedData = await axios.get('http://127.0.0.1:8000/user/api/v1') ;
            setLoding(true)
            setData(fetchedData.data)
        }
        const fetchSingleData = async ()=> {
            setLoding(false)
            const fetchedData = await axios.get('http://127.0.0.1:8000/user/api/v1/1') ;
            setLoding(true)
            setData(fetchedData.data)
        }
        if (all){
            fetchAllData()
            return
        }
        fetchSingleData()}

        return {all , data,loding , fetchdata,setAll}

}
