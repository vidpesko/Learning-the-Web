<script>
    export let data;
</script>

<h1>Blog post</h1>

<ul>
    {#each data.summaries as {slug, title}}
        <li><a href="/blog/{slug}">{title}</a></li>
    {/each}
</ul>