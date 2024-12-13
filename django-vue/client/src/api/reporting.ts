import axios, { AxiosResponse } from "axios";

export const loadOrders = () => {
  // Django server address; close the slash at the end of the URL
  return axios
    .get("http://localhost:8000/api/orders/")
    .then((response: AxiosResponse) => {
      console.log(response.data);
      return response.data;
    });
};
