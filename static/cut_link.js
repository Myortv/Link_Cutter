var app = new Vue({
  el: '#app',
  data: {
    outurl: 'Сначала введите Url для сокращения!',
    inputurl: ""

  },
  methods: {
    generate: function () {
      axios({
        method: 'post',
        url: '/api/link',

        headers: {
          'X-CSRFToken': Cookies.get('csrftoken')
        },

        data: {
          original_link: this.inputurl,
        },

      })
      .then(response => {
      this.outurl = 'http://localhost:8008/' + response['data']['hashed_url']
      })


    }
  }

})
