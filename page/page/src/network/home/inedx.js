import axiosInstance from "../request";

// export const getBooks = () => {
//   return axiosInstance({
//     url: '/api/books'
//   })
// }

// export const postBooks = (bookName, bookAuthor) => {
//   console.log(bookName, bookAuthor)
//   return axiosInstance({
//     url: `/api/books/`,
//     method: 'post',
//     data: {
//       'name': bookName,
//       'author': bookAuthor
//     }
//   })
// }



const axios = axiosInstance

export const getBooks = () => {return axios.get(`http://localhost:8000/api/books/`)}

export const postBooks = (bookName, bookAuthor) => {return axios.post(`http://localhost:8000/api/books/`, {'name': bookName, 'author': bookAuthor})}