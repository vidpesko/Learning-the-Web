<script>
    import { page, navigating } from "$app/stores";
</script>

<h1>HELLo</h1>

<p>
    {$page.url.pathname}
</p>


<a href="/about">Home</a>

{#if $navigating}
<p>
    {$navigating.to.url.pathname}
    HERHEHREH
</p>
{/if}