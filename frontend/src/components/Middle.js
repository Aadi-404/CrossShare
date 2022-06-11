// import { logDOM } from "@testing-library/react";
import React, { useState } from 'react';

// import React from "react";
import "../components/style/middle.css";
import imgFile from "./resource/logo.svg";
import axios from 'axios'


export const Middle = () => {

  const fileInput = document.getElementById("fileInput");

  const [cssClass, setCssClass] = useState(["drag_zone"]);


  const InDrag = (e)=>{
    // console.log("You are in ")
    e.preventDefault();
    // e.stopPropagation();


    if(!cssClass.includes("dragged")){
      setCssClass(
        [...cssClass,"dragged"]);
    }
  }
    
  const MoveOut = ()=>{
    // e.stopPropagation();
    // e.preventDefault();
    if(cssClass.includes("dragged")){
      setCssClass(["drag_zone"]);
    }
  }

  const drop = (e)=>{
    e.preventDefault();
    if(cssClass.includes("dragged")){
      setCssClass(["drag_zone"]);
    }
    // console.log(e.dataTransfer.files.length);
    const files = e.dataTransfer.files;
    fileInput.files= files;
    // console.log(fileInput.files);
    // console.log("drop");
    fileSend();


  }
  const fileSend= ()=>{
    let time = new Date();
    const now = time.getFullYear() + "-"+ time.getMonth() + "-"+ time.getDate() +" "+
      time.getHours()+":"+time.getMinutes()+":"+time.getSeconds() ;
    // const now = time.toString();
    // console.log(now);
    // const fileBundle = {
    //   msg : "demo",
    //   file : fileInput.files[0],
    //   time_now : now
    // }
    let data = new FormData();
    data.append('msg','demo');
    // data.append("file",fileInput.files[0])
    data.append("created_at",now);
    const url = `http://127.0.0.1:8000/api/file/`;
    const config = {
      headers: { 'content-type': 'multipart/form-data' }
  }

    // console.log("here i'm ready to upload")
    // console.log(fileBundle);
    console.log(data);
    axios.post(url,data,config)
    .then(res=>{
      console.log("res")
      console.log(res.data);
    }).catch(err =>{
      console.log("error")
      console.log(err);
    })

  }

  const fileGet=()=>{
    axios.get(`http://127.0.0.1:8000/api/5`).then(resp=>{
      console.log(resp.data);
    }).error(err=>{
      console.log(err);
    })
  }

  return (
    <>
      <div className="mid_container">
        <div className="drag_container">
          <div className={cssClass.join(" ") }  onDragOver={InDrag} onDragLeave={MoveOut} onDrop={drop}>
            <div className="img_container" >
              <img
                src={imgFile}
                id="img_over"
                className="center"
                alt="file img"
                draggable="false"
              />
              <img
                src={imgFile}
                className="right"
                alt="file img"
                draggable="false"
              />
              <img
                src={imgFile}
                className="left"
                alt="file img"
                draggable="false"
              />
            </div>
            <form method='POST'  enctype="multipart/form-data">
            {/* {% csrf_token %} */}
              <input type="file" id='fileInput' name='file' onChange={(e) =>{
                // const files = e.target.files;
                // console.log(files);
                e.preventDefault();
                fileInput.files= e.target.files;
                console.log(fileInput);
                // fileSend();
                // fileGet();
              }} />
            </form>
            <div className="drag_line">
              Drag your file here, or <span className="browsebtn" onClick={(e)=>{
                e.preventDefault();
                document.getElementById("fileInput").click();
          }} > Browse</span>
            </div>
          </div>
        <div className='url'>
          Loading
        </div>
        <div className='link'></div>
        </div>
        <div className="share_help">
          <div className="text_cont">Drop files here</div>
          </div>
      </div>
      
    </>
  );
};
