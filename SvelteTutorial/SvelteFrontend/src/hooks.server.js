export async function handle({ event, resolve }) {

    event.locals.answer = 42;

    // return await resolve(event, {
    //     transformPageChunk: ({ html }) => html.replace("<body", "<body style='color: pink'")
    // });
    return await resolve(event);
}

export async function handleFetch({ event, request, fetch }) {
    const url = new URL(request.url);
    if (url.pathname === "/ping") {
        return await fetch("/about");
    }

    return await fetch(request);
}