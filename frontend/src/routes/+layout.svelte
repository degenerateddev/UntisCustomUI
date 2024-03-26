<script>
    import * as Menubar from "$lib/components/ui/menubar/index.js";
    import { ModeWatcher } from "mode-watcher";
    import "../app.pcss";
    import { toggleMode } from "mode-watcher";
    import Sun from "svelte-radix/Sun.svelte";
    import Moon from "svelte-radix/Moon.svelte";

</script>

<div class="flex flex-col justify-between min-h-screen text-primary-foreground bg-primary">
    <ModeWatcher />

    <div class="flex justify-center py-10">
        <Menubar.Root>
            <Menubar.Menu>
                <Menubar.Trigger on:click={toggleMode} class="text-black dark:text-white">
                    <Sun
                        class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
                    />
                    <Moon
                        class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
                    />
                    <span class="sr-only">Toggle theme</span>
                </Menubar.Trigger>

              <Menubar.Trigger>Edit</Menubar.Trigger>
              <Menubar.Content>
                <Menubar.Item>Schools</Menubar.Item>
                <Menubar.Separator />
                <Menubar.Item>Classes</Menubar.Item>
              </Menubar.Content>
            </Menubar.Menu>
        </Menubar.Root>
    </div>

    <div class="container mx-auto">
        <slot />
    </div>
</div>