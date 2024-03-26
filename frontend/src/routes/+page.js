/** @type {import('./$types').PageLoad} */
export async function load(event) {
    const response = await event.fetch('/timetables/timetable.json');
    const timetable = await response.json();
    
    return {
		timetable
	};
}