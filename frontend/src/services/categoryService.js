import axios from 'axios'

class CategoryService {
    static fetchData = async () => {
        try {
          const response = await axios.get(
            `${import.meta.env.VITE_NGROK_URL}category/`,  // API endpoint
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

export default CategoryService