import axios from 'axios';

/**
 * Responsible for sending out api calls and storing responses
 */
export default class ServerConnection {
    constructor(endpoint){
        this.endpoint = endpoint;
    }

    async apiCallSingle(request){
      const res = await axios.post('/api/getroadobjecttypes', {'request': request});
  
      let data = res.data;
      return data;
    }
}