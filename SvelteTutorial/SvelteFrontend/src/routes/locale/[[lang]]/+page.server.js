const msg = {
    en: "hello",
    de: "halo",
    fr: "bonjour"
};

export function load({ params }) {
    return {
        greeting: msg[params.lang ?? "en"]
    };
}