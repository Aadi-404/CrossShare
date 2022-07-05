// import React from 'react'
import React, { useState, useEffect } from "react";
// import { useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import axios from "axios";
import "../components/style/download.css";

export const Download = () => {
  const [details, setDetails] = useState(["Here will be details"]);
  let { unique } = useParams();
  const url = `http://127.0.0.1:8000/api/file/${unique}`;
  const [downUrl, setdownUrl] = useState(["empty"]);
  

  useEffect(() => {
    fetchData();
    
    // Inside this callback function we perform our side effects.
  }, []);


  function fetchData() {
    axios
    .get(url)
    .then(function (response) {
      if (response.data.length !== 0) {
        setdownUrl([response.data[0].title]);
        setDetails([response.data[0].title]);
          // console.log(downUrl,details);
          // console.log(response.data[0].file);
        }
        // I need this data here ^^
        return response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
    }
    const durl = `http://127.0.0.1:8000/public/media/${downUrl}`
    


  return (
    <>
      <div className="main-container">
        <div className="download-details"> This field {downUrl}</div>
        <div className="download-button">
          <a href={durl}  target="_blank" download> Download Here </a>
        {/* <a href={durl}  target="_blank" download = "file" > Download Here </a> */}

        </div>
      </div>
    </>
  );
};
