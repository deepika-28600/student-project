
import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = { vus: 10, duration: '30s' };

export default function () {
  const res = http.get('http://localhost:8000/');
  check(res, { 'status 200': (r) => r.status === 200 });
  sleep(1);
}
