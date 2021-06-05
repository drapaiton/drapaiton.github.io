import { useEffect, useState } from "react";

const useAPI = () => {
  const [settings, setSettings] = useState({
    method: "",
    data: {},
    url: "",
  });
  const [fetch, setFetch] = useState({});

  const options = {
    method: settings.method,
    mode: "no-cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify({ body: settings.data }),
  };

  useEffect(() => {
    if (Object.values(settings.data).length !== 0) {
      fetch(settings.url, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: JSON.stringify({ body: settings.data }),
      })
        .then((response) => response)
        .then((payload) => {
          setFetch(payload.json());
        });
    }
  }, [settings.data]);

  const apiFetch = async () => {
    const response = await fetch(settings.url, options);
    const res = response.json();
    console.log("res---->", res);
    setFetch(res);
  };

  const handleFetch = (payload, method, url) => {
    setSettings({
      ...settings,
      method,
      data: payload,
      url,
    });
  };

  return { fetch, handleFetch };
};

export default useAPI;
