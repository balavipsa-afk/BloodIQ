% Diabetes
diabetes(high) :- glucose(X), X > 180.
diabetes(moderate) :- glucose(X), X > 140, X =< 180.
diabetes(low) :- glucose(X), X =< 140.

% Blood Pressure
bp(high) :- systolic(S), diastolic(D), (S > 140 ; D > 90).
bp(normal) :- systolic(S), diastolic(D), S =< 120, D =< 80.

% CBC
cbc(low) :- hemoglobin(H), H < 12.
cbc(normal) :- hemoglobin(H), H >= 12, H =< 16.
cbc(high) :- hemoglobin(H), H > 16.
