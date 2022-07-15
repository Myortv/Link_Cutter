var app = new Vue({
  el: '#app',
  data: {
    outurl: 'Сначала введите Url для сокращения!',
    inputurl: "",
    base_url:  location.protocol.concat("//").concat(window.location.hostname).concat(':').concat(location.port).concat('/'),

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
      this.outurl = this.base_url + response['data']['hashed_url']
      })


    }
  }

})
