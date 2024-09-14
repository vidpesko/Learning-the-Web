import { PASSWORD } from "$env/static/private";

export function load({ cookies }) {
    return {
        pass: PASSWORD
    };
}