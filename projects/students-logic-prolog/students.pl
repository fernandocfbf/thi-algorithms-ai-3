% Define the colors of the doors
color(red).
color(green).
color(white).
color(yellow).
color(blue).

% Define the names
name(max).
name(bert).
name(ute).
name(monika).
name(rudolf).

% Define the subjects being studied
subject(ai).
subject(eit).
subject(mech).
subject(ba).
subject(cs).

% Define the different drinks
drink(tea).
drink(coffee).
drink(milk).
drink(oj).
drink(water).

% Define the different pets
pet(cat).
pet(budgie).
pet(dog).
pet(parrot).
pet(hamster).

% nth1(3, H, student(_, milk, _, _, _)), 

% Define the rules
rules(H) :- H = [_,_,_,_,_], 
	member(student(red, _, _, _, max), H), 
	member(student(_, tea, _, _, bert), H),
	member(student(_, _, cat, _, ute), H),
	left_of(student(green, _, _, _, _), student(white, _, _, _, _), H),
	member(student(green, coffee, _, _, _), H),
	member(student(_, _, budgie, eit, _), H),
	member(student(yellow, _, _, mech, _), H),
	H = [_, _, student(_, milk, _, _, _), _, _],
	next_to(student(_, _, _, ai, _), student(_, _, dog, _, _), H),
	next_to(student(_, _, parrot, _, _), student(_, _, _, mech, _), H),
	H = [student(_, _, _, _, monika)|_],
	member(student(_, oj, _, cs, _), H),
	member(student(_, _, _, ba, rudolf), H),
	next_to(student(_, _, _, _, monika), student(blue, _, _, _, _), H),
	next_to(student(_, _, _, ai, _), student(_, water, _, _, _), H).

% Define the ordering relation between two houses
% left_of(A, B, Houses) :- Houses = [A,B,_,_,_],[_,A,B,_,_],[_,_,A,B,_],[_,_,_,A,B].
left_of(X, Y, List) :- nth0(XIndex, List, X), nth0(YIndex, List, Y), XIndex + 1 =:= YIndex.

% Define the adjacency relation between two houses
next_to(A, B, Houses) :- left_of(A, B, Houses).
next_to(A, B, Houses) :- left_of(B, A, Houses).

% Define the student structure
student(color, drink, pet, subject, name).

solve(Houses) :- rules(Houses).

solution(H) :- solve(H), member(student(_,_,pet(hamster), _, _), H).
	
