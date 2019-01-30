<!--<template>
  <div class="hello">
    <h3>{{ msg }}</h3>
    <p class="mb-2">The application is configured and ready to import our components. You will find MDB Vue docs <a href="https://mdbootstrap.com/vue/" target="_blank">here</a>.</p>
    <p>Please type <span class="black-text">npm run demo</span> or <span class="black-text">yarn demo</span> to launch our Demonstration Page. The files with the code are placed in the <span class="black-text">demo</span> directory.</p>
    <p>If You want to completely remove our demo from Your App, easily type <span class="black-text">npm run remove-demo</span> or <span class="black-text">yarn remove-demo</span>.</p>
  </div>
</template>-->

<template>
  <mdb-container>
      <div>
        <p>Home page</p>
        <p>Random number from backend: {{ band }}</p>
        <mdb-btn @click="getBand" color="primary">Primary</mdb-btn>
        <!--<button @click="getBand">Get the band</button>-->
      </div>
  
<!--
    <mdb-card>
      <mdb-card-image src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%286%29.jpg" alt="Card image cap"></mdb-card-image>
      <mdb-card-body>
        <mdb-card-title>Basic card</mdb-card-title>
        <mdb-card-text>Some quick example text to build on the card title and make up the bulk of the card's content.</mdb-card-text>
        <mdb-btn color="primary">Button</mdb-btn>
      </mdb-card-body>
    </mdb-card>
    -->
  </mdb-container>
</template>
      

<script>
  import { mdbContainer, mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText, mdbBtn } from 'mdbvue';
  import axios from 'axios';

  export default {
    name: 'CardPage',
    data() {
      return {
          band: "none"
      }
    },
    components: {
      mdbContainer, 
      mdbCard,
      mdbCardImage,
      mdbCardBody,
      mdbCardTitle,
      mdbCardText,
      mdbBtn
    },
    created () {
      this.band = "init"
    },
    methods: {
      getBand () {
        const path = 'http://localhost:5000/api/test'
        axios.get(path)
        .then(response => {
          this.band = response.data
        })
        .catch(error => {
          console.log(error)
        })
      }
    }
  };
</script>



<!--
<script>
    import { mdbTbl, mdbTblHead, mdbTblBody } from 'mdbvue';

    export default {
      name: 'TablePage',
      components: {
        mdbTbl,
        mdbTblHead,
        mdbTblBody
      }
    };
  </script>-->

<!--<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your MDB Vue.js App'
    };
  }
}
</script>-->

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  font-weight: normal;
  padding-top: 20px;
  padding-bottom: 30px;
}
p {
  color: #969696;
  margin-bottom: 0;
  font-size: 14px;
}
</style>
