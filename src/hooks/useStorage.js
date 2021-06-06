import { useState, useEffect } from 'react';

const useStorage = (nickname) => {
  const [storage, setStorage] = useState(null);

  useEffect(() => {
    if (getLocalstorage())
  }, []);

  const setLocalstorage = (nickname) => {
    localStorage.setItem('username', nickname);
    setStorage(nickname);
  }

  const getLocalstorage = (value) => {
    return localStorage.getItem(value);
  }

  const setUserName = (value) => {
    setLocalstorage(value);
  }

  const checkUserName = (value) => {
    return getLocalstorage(value);
  }

  return {
    storage,
    setUserName,
    checkUserName,
    setLocalstorage
  }

}

export default useStorage;
