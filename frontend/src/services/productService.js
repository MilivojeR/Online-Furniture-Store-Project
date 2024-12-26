import axios from 'axios'

class ProductService {
    static fetchData = async () => {
        try {
          const response = await axios.get(
            `${import.meta.env.VITE_NGROK_URL}product`,  // API endpoint
            {
              headers: {
                'Accept': 'application/json',  // Postavljanje Accept header-a
                "ngrok-skip-browser-warning": "69420"
              }
            }
          );
          console.log(response.data);
          return response.data;
        } catch (error) {
          console.log(error.message);
        }
      };

      static fetchDataById = async (id) => {
        try {
          const response = await axios.get(
            `${import.meta.env.VITE_NGROK_URL}product/${id}`,  // API endpoint
            {
              headers: {
                'Accept': 'application/json',  // Postavljanje Accept header-a
                "ngrok-skip-browser-warning": "69420"
              }
            }
          );
          console.log(response.data);
          return response.data;
        } catch (error) {
          console.log(error.message);
        }
      };
}

export default ProductService