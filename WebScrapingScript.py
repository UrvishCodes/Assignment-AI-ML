from imdb import IMDb 

def get_filmography(actor_name):
    ia = IMDb()
    people = ia.search_person(actor_name)
    if not people:
        print("Actor not found.")
        return
    
    actor = people[0]
    ia.update(actor, info=["filmography"])

    if "actor" in actor or "actress" in actor:
        roles = actor.get("actor", []) + actor.get("actress", [])
        movies = [
            (role.get("year"), role["title"]) 
            for role in roles if role.get("year") is not None
        ]
        movies.sort(reverse=True, key=lambda x: x[0])

        print(f"Filmography of {actor_name} in descending order:")
        for year, title in movies:
            print(f"{year}: {title}")
    else:
        print("No filmography found for this actor.")

actor_name = "Leonardo DiCaprio"
get_filmography(actor_name)
