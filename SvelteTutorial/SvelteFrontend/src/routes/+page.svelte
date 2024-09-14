<script>
    export let data;
    import { PUBLIC_PASSWORD } from "$env/static/public";
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<h3>{PUBLIC_PASSWORD}</h3>
<h3>{data.pass}</h3>