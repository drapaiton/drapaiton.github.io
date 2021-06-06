import { useEffect, useState, useRef } from "react";

const useFetch = (messageJSON, method, url) => {
  const cache = useRef({});
  const [data, setData] = useState([]);

  const options = {
    method,
    mode: "cors",
    //cache: "no-cache",
    //credentials: "same-origin",
    //headers: {
    //  "Content-Type": "application/json; charset=utf-8",
    //},
    //redirect: "follow",
    //referrerPolicy: "no-referrer",
    body: JSON.stringify(messageJSON),
  };

  useEffect(() => {
    if (!url) return;
    const fetchData = async () => {
      if (cache.current[url]) {
        const data = cache.current[url];
        setData(data);
      } else {
        const request = new Request(url, options);
        fetch(request)
          .then((response) => {
            if (response.status === 200) {
              return response.json();
            } else {
              throw new Error("Something went wrong on api server!");
            }
          })
          .then((response) => {
            setData(response);
          })
          .catch((error) => {
            console.error(error);
          });
        console.log();
      }
    };

    fetchData();
  }, [url]);

  return { data };
};

export default useFetch;
