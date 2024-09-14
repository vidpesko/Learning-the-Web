export async function load({ fetch }) {
    const response = await fetch("/ping");

    return {
        msg: 31,
        response: await response.text()
    };
    // throw new Error("Error");
}