<script>
    import { message } from "$lib/index.js";

    export let data;

    let post = data.post;
</script>

<h1>{post.title}</h1>

<div>
    {@html post.content}
</div>


<h3>{message}</h3>


<h1>Other posts</h1>
<ul>
    {#each data.summaries as {slug, title}}
        <li><a href="/blog/{slug}">{title}</a></li>
    {/each}
</ul>