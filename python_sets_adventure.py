our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def find_destinations():
    print(f'We share routes {', '.join(our_routes.intersection(competitor_routes))} with our competitor.')
    print(f'Routes {', '.join(our_routes.difference(competitor_routes))} are unique to us.')
    print(f'We do not share routes {', '.join(our_routes.symmetric_difference(competitor_routes))} with our competitors.')

if __name__ == "__main__":
    find_destinations()
