import http from 'k6/http';
import { sleep } from 'k6';

export const options = {

  // A number specifying the number of VUs to run concurrently.
  vus: 10,
  // A string specifying the total duration of the test run.
  duration: '30s',

};


export default function() {
  http.get('http://127.0.0.1:5000/sorted-people');
  sleep(1);
}
