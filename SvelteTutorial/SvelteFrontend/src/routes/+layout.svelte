<script>
    import { navigating } from "$app/stores";

    let previous;
    let start;
    let end;

    $: if ($navigating) {
        start = Date.now();
        end = null;
        previous = $navigating;
    } else {
        end = Date.now();
    }
</script>

<nav>
    <a href="/">home</a>
    <a href="/about" data-sveltekit-preload-data>about</a>
    <a href="/preloading" data-sveltekit-reload>preloading</a>
</nav>

<h1>Layout</h1>

<slot/>

{#if previous && end}
    <p>Navigated from {previous.from.url.pathname} to {previous.to.url.pathname} in <strong>{end - start}ms</strong></p>
{/if}