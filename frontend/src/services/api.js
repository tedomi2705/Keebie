import axios from 'axios';

const api = axios.create({
  // Use relative URL instead of REACT_APP_BASE_URL
  baseURL: '/api',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  }
});

export default api;