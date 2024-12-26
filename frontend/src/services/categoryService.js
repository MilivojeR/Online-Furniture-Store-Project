import axios from 'axios'

class CategoryService {
    static fetchData = async () => {
        try {
          const response = await axios.get(
<<<<<<< HEAD
            `${import.meta.env.VITE_NGROK_URL}category/`,  // API endpoint
=======
            "https://9874-62-4-41-75.ngrok-free.app/category/",  // API endpoint
>>>>>>> 1ad1f86e6fc763abc9f7af10a40395c401cc3935
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