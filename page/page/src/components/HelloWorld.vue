<template>
  <div class="hello">
    <div>
      <ul>
        <li v-for="(item, index) in books" :key="index">{{item.name}}-{{item.author}}</li>
      </ul>
    </div>
    <ul>
      <li><span>name: </span><input type="text" v-model="name"></li>
      <li><span>author: </span><input type="text" v-model="author"></li>
    </ul>
    <input type="button" value="submit" @click="submitBook">
  </div>
</template>

<script>
import {getBooks, postBooks} from '../network/home/inedx'

export default {
  name: 'HelloWorld',
  data() {
    return {
      books: {},
      name: '',
      author: ''
    }
  },
  props: {
    msg: String
  },
  created(){
    this.loadBooks()
  },
  methods: {
    loadBooks() {
      getBooks().then(res => {
        this.books = res.data
      })
    },
    submitBook() {
      postBooks(this.name, this.author).then(res => {
        console.log(res);
        this.loadBooks();
      }, err => {
        alert(err)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
