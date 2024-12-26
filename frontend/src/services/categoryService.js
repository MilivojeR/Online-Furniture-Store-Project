import axios from 'axios'

class CategoryService {
    static fetchData = async () => {
        try {
          const response = await axios.get(
            "https://9a80-62-4-41-75.ngrok-free.app/category/",  // API endpoint
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