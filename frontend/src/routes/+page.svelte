<script>
    import CardFooter from "@/components/ui/card/card-footer.svelte";
    import CardHeader from "@/components/ui/card/card-header.svelte";
    import Card from "@/components/ui/card/card.svelte";

    export let data;

    const timetable = data.timetable;
</script>

<main>
    {#each Object.keys(timetable).reverse() as day}
        <h1>{day.toUpperCase()}</h1>

        {#each timetable[day] as schedule}
            <Card>
                <CardHeader>
                    <h2>{schedule.subject}</h2>
                </CardHeader>
                <CardFooter>
                    <div class="container">
                        <p>{schedule.startTime} - {schedule.endTime}</p>
                    </div>
                </CardFooter>
            </Card>
        {/each}
    {/each}
</main>