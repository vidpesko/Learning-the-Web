<script>
    import { enhance } from "$app/forms";
    import { fly, slide } from "svelte/transition";

	export let data;
    export let form;

    let creating = false;
    let deleting = [];
</script>

<div class="centered">
	<h1>todos</h1>

    {#if form?.error}
        <p class="error">{form.error}</p>
    {/if}

    <form method="post" action="?/create" use:enhance={() => {
        creating = true;

        return async ({ update }) => {
            await update();
            creating = false;
        }
    }}>
        <label>
            add a todo:
            <input disabled={creating} type="text" autocomplete="off" name="description" required />
        </label>
    </form>

	<ul class="todos">
		{#each data.todos.filter((todo) => !deleting.includes(todo.id)) as todo (todo.id)}
			<li in:fly={{ y: 20 }} out:slide>
                <form action="?/delete" method="post" use:enhance={() => {
                    deleting = [...deleting, todo.id];

                    return async ({ update }) => {
                        await update();
                        deleting = deleting.filter((id) => id !== todo.id);
                    };
                }}>
                    <input type="hidden" name="id" value="{todo.id}" />
                    {todo.description}
                    <button>X</button>
                </form>
			</li>
		{/each}

        {#if creating}
            <span class="saving">Creating...</span>
        {/if}
	</ul>
</div>

<style>
	.centered {
		max-width: 20em;
		margin: 0 auto;
	}

	label {
		width: 100%;
	}

	input {
		flex: 1;
	}

	span {
		flex: 1;
	}

	button {
		border: none;
		background-size: 1rem 1rem;
		cursor: pointer;
		height: 100%;
		aspect-ratio: 1;
		opacity: 0.5;
		transition: opacity 0.2s;
	}

	button:hover {
		opacity: 1;
	}

	.saving {
		opacity: 0.5;
	}
</style>
