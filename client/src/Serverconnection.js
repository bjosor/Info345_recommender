import axios from 'axios';

/**
 * Responsible for sending out api calls and storing responses
 */
export default class ServerConnection {
    constructor(endpoint){
        this.endpoint = endpoint;
    }

    async apiCallSingle(request){
        console.log('Attempting to call server')
        const res = await axios.get(request);
  
        let data = res.data;
        console.log(data)
        return data;
    }
}