import { getApiUrl } from "./env";


export async function authorize(username, password) {
    const authUrl = `${getApiUrl()}auth/login/`;
    let response = await fetch(authUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': getApiUrl(),
        },
        body: {
            'username': username,
            'password': password
        }
    });
    console.log(response);
}
