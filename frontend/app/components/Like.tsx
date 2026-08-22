'use client';


import axios from "axios"
import { useState , useEffect } from "react"
import { Heart } from "lucide-react";


export default function Likes(){

    const [likes, setLikes] = useState(0)
    const [liked , setLiked] = useState(false)
    const [image,setImage] = useState()

    useEffect(()=>{
        const like = axios.get('http://localhost:8000/user/api/v1/profile/1').then(res => setLikes(res.data.likes))
        const avatar = axios.get('http://localhost:8000/user/api/v1/profile/1').then(res => setImage(res.data.avatar))
        
    },[])



    const like = async function(){
        const likeCount = await axios.get('http://localhost:8000/user/api/v1/profile/1/likes')
        setLikes(likeCount.data)
        setLiked(true)

    }    


  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <img src={image} alt="" />
      
      <div className="w-40 h-40 bg-white rounded-2xl shadow-lg flex flex-col items-center justify-center gap-3">
        
        <button
          onClick={like}
          className="p-3 rounded-full hover:bg-gray-100 transition"
        >
          <Heart
            size={32}
            className={liked ? "fill-red-500 text-red-500" : "text-gray-700"}
          />
        </button>

        <span className="text-lg font-semibold text-gray-700">
          {likes}
        </span>

      </div>

    </div>
  );
}